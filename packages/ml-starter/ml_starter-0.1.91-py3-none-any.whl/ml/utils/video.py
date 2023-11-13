# mypy: disable-error-code="import"
"""Defines utilites for saving and loading video streams.

The main API for using this module is:

.. code-block:: python

    from ml.utils.video import read_video, write_video

    def frame_iterator() -> Iterator[Tensor]:
        for frame in read_video("/path/to/video.mp4"):
            yield frame

    write_video(frame_iterator(), "/path/to/other/video.mp4")

This just uses FFMPEG so it should be reasonably quick.
"""

import asyncio
import functools
import re
import shutil
import warnings
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import AsyncGenerator, Iterator, Literal

import av
import numpy as np
import torchvision.transforms.functional as F
from torch import Tensor

from ml.utils.image import as_uint8, standardize_image
from ml.utils.io import prefetch_samples


@functools.lru_cache()
def ffmpeg_python_available() -> bool:
    try:
        import ffmpeg

        assert ffmpeg is not None  # Silence unused import warning
    except ModuleNotFoundError:
        return False
    else:
        return True


@functools.lru_cache()
def mpl_available() -> bool:
    try:
        import matplotlib

        assert matplotlib is not None  # Silence unused import warning
    except ModuleNotFoundError:
        return False
    else:
        return True


@functools.lru_cache()
def cv2_available() -> bool:
    try:
        import cv2

        assert cv2 is not None  # Silence unused import warning
    except ModuleNotFoundError:
        return False
    else:
        return True


@dataclass
class VideoProps:
    frame_width: int
    frame_height: int
    frame_count: int
    fps: Fraction

    @classmethod
    def from_file_av(cls, fpath: str | Path) -> "VideoProps":
        container = av.open(str(fpath))
        stream = container.streams.video[0]

        return cls(
            frame_width=stream.width,
            frame_height=stream.height,
            frame_count=stream.frames,
            fps=Fraction(stream.average_rate),
        )

    @classmethod
    def from_file_opencv(cls, fpath: str | Path) -> "VideoProps":
        try:
            import cv2
        except ModuleNotFoundError as e:
            raise ModuleNotFoundError("Install OpenCV to use this function: `pip install opencv-python`") from e

        cap = cv2.VideoCapture(str(fpath))

        return cls(
            frame_width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            frame_height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
            frame_count=int(cap.get(cv2.CAP_PROP_FRAME_COUNT)),
            fps=Fraction(cap.get(cv2.CAP_PROP_FPS)),
        )

    @classmethod
    def from_file_ffmpeg(cls, fpath: str | Path) -> "VideoProps":
        try:
            import ffmpeg
        except ModuleNotFoundError as e:
            raise ModuleNotFoundError("Install matplotlib to use this function: `pip install ffmpeg-python`") from e

        probe = ffmpeg.probe(str(fpath))

        for stream in probe["streams"]:
            if stream["codec_type"] == "video":
                width, height, count = stream["width"], stream["height"], int(stream["nb_frames"])
                fps_num, fps_denom = stream["r_frame_rate"].split("/")
                return cls(
                    frame_width=width,
                    frame_height=height,
                    frame_count=count,
                    fps=Fraction(int(fps_num), int(fps_denom)),
                )

        raise ValueError(f"Could not parse video properties from video in {fpath}")


def _resample_video(
    video_chunks: Iterator[np.ndarray],
    *,
    prefetch_n: int = 1,
) -> Iterator[np.ndarray]:
    yield from prefetch_samples(video_chunks, prefetch_n)


def read_video_av(
    in_file: str | Path,
    *,
    target_dims: tuple[int | None, int | None] | None = None,
) -> Iterator[np.ndarray]:
    """Function that reads a video file to a stream of numpy arrays using PyAV.

    Args:
        in_file: The input video to read
        target_dims: If not None, resize each frame to this size

    Yields:
        Frames from the video as numpy arrays with shape (H, W, C)
    """
    container = av.open(str(in_file))

    for frame in container.decode(video=0):
        frame = frame.to_rgb().to_ndarray()
        if target_dims is not None:
            frame = F.resize(frame, target_dims[::-1])
        yield as_uint8(frame)


def read_video_ffmpeg(
    in_file: str | Path,
    *,
    output_fmt: str = "rgb24",
    channels: int = 3,
) -> Iterator[np.ndarray]:
    """Function that reads a video file to a stream of numpy arrays using FFMPEG.

    Args:
        in_file: The input video to read
        output_fmt: The output image format
        channels: Number of output channels for each video frame

    Yields:
        Frames from the video as numpy arrays with shape (H, W, C)
    """
    try:
        import ffmpeg
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError("Install matplotlib to use this function: `pip install ffmpeg-python`") from e

    props = VideoProps.from_file_ffmpeg(in_file)

    stream = ffmpeg.input(str(in_file))
    stream = ffmpeg.output(stream, "pipe:", format="rawvideo", pix_fmt=output_fmt, r=float(props.fps))
    stream = ffmpeg.run_async(stream, pipe_stdout=True)

    while True:
        in_bytes = stream.stdout.read(props.frame_width * props.frame_height * channels)
        if not in_bytes:
            break
        yield np.frombuffer(in_bytes, np.uint8).reshape((props.frame_height, props.frame_width, channels))

    stream.stdout.close()
    stream.wait()


async def read_video_with_timestamps_ffmpeg(
    in_file: str | Path,
    *,
    output_fmt: str = "rgb24",
    channels: int = 3,
    target_dims: tuple[int | None, int | None] | None = None,
) -> AsyncGenerator[tuple[np.ndarray, float], None]:
    """Like `read_video_ffmpeg` but also returns timestamps.

    Args:
        in_file: The input video to read
        output_fmt: The output image format
        channels: Number of output channels for each video frame
        target_dims: (width, height) dimensions for images being loaded, with
            None meaning that the aspect ratio should be kept the same

    Yields:
        Frames from the video as numpy arrays with shape (H, W, C), along with
        the frame timestamps
    """
    try:
        import ffmpeg
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError("Install matplotlib to use this function: `pip install ffmpeg-python`") from e

    props = VideoProps.from_file_ffmpeg(in_file)

    def aspect_ratio(x: int, a: int, b: int) -> int:
        return (x * a + b - 1) // b

    vf: list[str] = []
    if target_dims is not None:
        width_opt, height_opt = target_dims
        if width_opt is None:
            assert height_opt is not None, "If width is None, height must not be None"
            width_opt = aspect_ratio(height_opt, props.frame_width, props.frame_height)
        if height_opt is None:
            assert width_opt is not None, "If height is None, width must not be None"
            height_opt = aspect_ratio(width_opt, props.frame_height, props.frame_width)
        assert (width := width_opt) is not None and (height := height_opt) is not None
        vf.append(f"scale={width}:{height}")
    else:
        width, height = props.frame_width, props.frame_height
    vf.append("showinfo")

    stream = ffmpeg.input(str(in_file))
    stream = ffmpeg.output(stream, "pipe:", format="rawvideo", pix_fmt=output_fmt, r=float(props.fps), vf=",".join(vf))
    stream = ffmpeg.run_async(stream, pipe_stdout=True, pipe_stderr=True)

    async def gen_frames() -> AsyncGenerator[np.ndarray, None]:
        while True:
            in_bytes = stream.stdout.read(height * width * channels)
            if not in_bytes:
                await asyncio.sleep(10)
                raise StopAsyncIteration
            frame = np.frombuffer(in_bytes, np.uint8).reshape((height, width, channels))
            yield frame

    async def gen_timestamps() -> AsyncGenerator[float, None]:
        exp = re.compile(rb"n:\s*(\d+)\s*pts:\s*(\d+)\s*pts_time:\s*([\d\.]+)")
        while True:
            in_line = stream.stderr.readline()
            if not in_line:
                raise StopAsyncIteration
            exp_match = exp.search(in_line)
            if exp_match is None:
                continue
            _, _, pts_time = exp_match.groups()
            yield float(pts_time.decode("utf-8"))

    frame_iter, ts_iter = gen_frames(), gen_timestamps()

    try:
        while True:
            frame, ts = await asyncio.gather(frame_iter.__anext__(), ts_iter.__anext__())
            yield frame, ts

    except StopAsyncIteration:
        stream.stdout.close()
        stream.stderr.close()
        stream.wait()


def read_video_opencv(in_file: str | Path) -> Iterator[np.ndarray]:
    """Reads a video as a stream using OpenCV.

    Args:
        in_file: The input video to read

    Yields:
        Frames from the video as numpy arrays with shape (H, W, C)
    """
    try:
        import cv2
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError("Install OpenCV to use this function: `pip install opencv-python`") from e

    cap = cv2.VideoCapture(str(in_file))

    while True:
        ret, buffer = cap.read()
        if not ret:
            cap.release()
            return
        yield buffer


def write_video_opencv(
    itr: Iterator[np.ndarray | Tensor],
    out_file: str | Path,
    *,
    keep_resolution: bool = False,
    fps: int | Fraction = 30,
    codec: str = "MP4V",
) -> None:
    """Function that writes a video from a stream of numpy arrays using OpenCV.

    Args:
        itr: The image iterator, yielding images with shape (H, W, C).
        out_file: The path to the output file.
        keep_resolution: If set, don't change the image resolution, otherwise
            resize to a human-friendly resolution.
        fps: Frames per second for the video.
        codec: FourCC code specifying OpenCV video codec type. Examples are
            MPEG, MP4V, DIVX, AVC1, H236.
    """
    try:
        import cv2
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError("Install OpenCV to use this function: `pip install opencv-python`") from e

    Path(out_file).parent.mkdir(exist_ok=True, parents=True)

    first_img = standardize_image(next(itr), keep_resolution=keep_resolution)
    height, width, _ = first_img.shape

    fourcc = cv2.VideoWriter_fourcc(*codec)
    stream = cv2.VideoWriter(str(out_file), fourcc, fps if isinstance(fps, int) else round(fps), (width, height))

    def write_frame(img: np.ndarray) -> None:
        stream.write(as_uint8(img))

    write_frame(first_img)
    for img in itr:
        write_frame(standardize_image(img, keep_resolution=keep_resolution))

    stream.release()
    cv2.destroyAllWindows()


def write_video_av(
    itr: Iterator[np.ndarray | Tensor],
    out_file: str | Path,
    *,
    keep_resolution: bool = False,
    fps: int | Fraction = 30,
    codec: str = "libx264",
    input_fmt: str = "rgb24",
    output_fmt: str = "yuv420p",
) -> None:
    """Function that writes an video from a stream of numpy arrays using PyAV.

    Args:
        itr: The image iterator, yielding images with shape (H, W, C).
        out_file: The path to the output file.
        keep_resolution: If set, don't change the image resolution, otherwise
            resize to a human-friendly resolution.
        fps: Frames per second for the video.
        codec: The video codec to use for the output video
        input_fmt: The input pixel format
        output_fmt: The output pixel format
    """
    Path(out_file).parent.mkdir(exist_ok=True, parents=True)

    first_img = standardize_image(next(itr), keep_resolution=keep_resolution)

    output = av.open(out_file, "w", format="mp4")
    stream = output.add_stream(codec, rate=fps)
    stream.pix_fmt = output_fmt

    def write_frame(img: np.ndarray) -> None:
        frame = av.VideoFrame.from_ndarray(as_uint8(img), format=input_fmt)
        packet = stream.encode(frame)
        if packet is not None:
            output.mux(packet)

    write_frame(first_img)
    for img in itr:
        write_frame(standardize_image(img, keep_resolution=keep_resolution))

    packet = stream.encode()
    if packet is not None:
        output.mux(packet)

    output.close()


def write_video_ffmpeg(
    itr: Iterator[np.ndarray | Tensor],
    out_file: str | Path,
    *,
    keep_resolution: bool = False,
    fps: int | Fraction = 30,
    out_fps: int | Fraction = 30,
    vcodec: str = "libx264",
    input_fmt: str = "rgb24",
    output_fmt: str = "yuv420p",
) -> None:
    """Function that writes an video from a stream of numpy arrays using FFMPEG.

    Args:
        itr: The image iterator, yielding images with shape (H, W, C).
        out_file: The path to the output file.
        keep_resolution: If set, don't change the image resolution, otherwise
            resize to a human-friendly resolution.
        fps: Frames per second for the video.
        out_fps: Frames per second for the saved video.
        vcodec: The video codec to use for the output video
        input_fmt: The input image format
        output_fmt: The output image format
    """
    try:
        import ffmpeg
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError("Install matplotlib to use this function: `pip install ffmpeg-python`") from e

    Path(out_file).parent.mkdir(exist_ok=True, parents=True)

    first_img = standardize_image(next(itr), keep_resolution=keep_resolution)
    height, width, _ = first_img.shape

    stream = ffmpeg.input("pipe:", format="rawvideo", pix_fmt=input_fmt, s=f"{width}x{height}", r=float(fps))
    stream = ffmpeg.output(stream, str(out_file), pix_fmt=output_fmt, vcodec=vcodec, r=float(out_fps))
    stream = ffmpeg.overwrite_output(stream)
    stream = ffmpeg.run_async(stream, pipe_stdin=True)

    def write_frame(img: np.ndarray) -> None:
        stream.stdin.write(as_uint8(img).tobytes())

    # Writes all the video frames to the file.
    write_frame(first_img)
    for img in itr:
        write_frame(standardize_image(img, keep_resolution=keep_resolution))

    stream.stdin.close()
    stream.wait()


def write_video_matplotlib(
    itr: Iterator[np.ndarray | Tensor],
    out_file: str | Path,
    *,
    keep_resolution: bool = False,
    dpi: int = 50,
    fps: int | Fraction = 30,
    title: str = "Video",
    comment: str | None = None,
    writer: str = "ffmpeg",
) -> None:
    """Function that writes an video from a stream of input tensors.

    Args:
        itr: The image iterator, yielding images with shape (H, W, C).
        out_file: The path to the output file.
        keep_resolution: If set, don't change the image resolution, otherwise
            resize to a human-friendly resolution.
        dpi: Dots per inch for output image.
        fps: Frames per second for the video.
        title: Title for the video metadata.
        comment: Comment for the video metadata.
        writer: The Matplotlib video writer to use (if you use the
            default one, make sure you have `ffmpeg` installed on your
            system).
    """
    try:
        import matplotlib.animation as ani
        import matplotlib.pyplot as plt
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError("Install matplotlib to use this function: `pip install matplotlib`") from e

    Path(out_file).parent.mkdir(exist_ok=True, parents=True)

    first_img = standardize_image(next(itr), keep_resolution=keep_resolution)
    height, width, _ = first_img.shape
    fig, ax = plt.subplots(figsize=(width / dpi, height / dpi))

    # Ensures that there's no extra space around the image.
    fig.subplots_adjust(
        left=0,
        bottom=0,
        right=1,
        top=1,
        wspace=None,
        hspace=None,
    )

    # Creates the writer with the given metadata.
    writer_obj = ani.writers[writer]
    metadata = {
        "title": title,
        "artist": __name__,
        "comment": comment,
    }
    mpl_writer = writer_obj(
        fps=fps if isinstance(fps, int) else round(fps),
        metadata={k: v for k, v in metadata.items() if v is not None},
    )

    with mpl_writer.saving(fig, out_file, dpi=dpi):
        im = ax.imshow(as_uint8(first_img), interpolation="nearest")
        mpl_writer.grab_frame()

        for img in itr:
            im.set_data(as_uint8(standardize_image(img, keep_resolution=keep_resolution)))
            mpl_writer.grab_frame()


Reader = Literal["ffmpeg", "av", "opencv"]
Writer = Literal["ffmpeg", "matplotlib", "av", "opencv"]


def get_video_props(in_file: str | Path, *, reader: Reader = "av") -> VideoProps:
    if reader == "ffmpeg":
        if not shutil.which("ffmpeg"):
            warnings.warn("FFMPEG is not available in this system.")
            reader = "av"
        elif not ffmpeg_python_available():
            warnings.warn("FFMPEG Python is not installed; install with `pip install ffmpeg-python`")
            reader = "av"
        else:
            return VideoProps.from_file_ffmpeg(in_file)

    if reader == "opencv":
        if not cv2_available():
            warnings.warn("OpenCV is not installed; install with `pip install opencv-python`")
            reader = "av"
        else:
            return VideoProps.from_file_opencv(in_file)

    if reader == "av":
        return VideoProps.from_file_av(in_file)

    raise ValueError(f"Unknown reader {reader}")


def read_video(
    in_file: str | Path,
    *,
    prefetch_n: int = 1,
    reader: Reader = "av",
) -> Iterator[np.ndarray]:
    """Function that reads a video from a file to a stream of Numpy arrays.

    Args:
        in_file: The path to the input file.
        prefetch_n: Number of chunks to prefetch.
        reader: The video reader to use.

    Yields:
        The video frames as Numpy arrays.
    """
    if reader == "ffmpeg":
        if not shutil.which("ffmpeg"):
            warnings.warn("FFMPEG is not available in the system.")
            reader = "av"
        elif not ffmpeg_python_available():
            warnings.warn("FFMPEG Python is not installed; install with `pip install ffmpeg-python`")
            reader = "av"
        else:
            return _resample_video(
                read_video_ffmpeg(in_file),
                prefetch_n=prefetch_n,
            )

    if reader == "opencv":
        if not cv2_available():
            warnings.warn("OpenCV is not installed; install with `pip install opencv-python`")
            reader = "av"
        else:
            return _resample_video(
                read_video_opencv(in_file),
                prefetch_n=prefetch_n,
            )

    if reader == "av":
        return _resample_video(
            read_video_av(in_file),
            prefetch_n=prefetch_n,
        )

    raise ValueError(f"Invalid reader: {reader}")


def write_video(
    itr: Iterator[np.ndarray | Tensor],
    out_file: str | Path,
    *,
    fps: int | Fraction = 30,
    keep_resolution: bool = False,
    writer: Writer = "av",
) -> None:
    """Function that writes an video from a stream of input tensors.

    Args:
        itr: The image iterator, yielding images with shape (H, W, C).
        out_file: The path to the output file.
        fps: Frames per second for the video.
        keep_resolution: If set, don't change the image resolution, otherwise
            resize to a human-friendly resolution.
        writer: The video writer to use.

    Raises:
        ValueError: If the writer is invalid.
    """
    if writer == "ffmpeg":
        if not shutil.which("ffmpeg"):
            warnings.warn("FFMPEG is not available in the system.")
            writer = "av"
        elif not ffmpeg_python_available():
            warnings.warn("FFMPEG Python is not installed; install with `pip install ffmpeg-python`")
            writer = "av"
        else:
            write_video_ffmpeg(itr, out_file, fps=fps, keep_resolution=keep_resolution)
            return

    if writer == "matplotlib":
        if not shutil.which("ffmpeg"):
            warnings.warn("FFMPEG is not available in the system.")
            writer = "av"
        elif not mpl_available():
            warnings.warn("Matplotlib is not available in the system.")
            writer = "av"
        else:
            write_video_matplotlib(itr, out_file, fps=fps, keep_resolution=keep_resolution)
            return

    if writer == "opencv":
        if not cv2_available():
            warnings.warn("OpenCV is not installed; install with `pip install opencv-python`")
            writer = "av"
        else:
            write_video_opencv(itr, out_file, fps=fps, keep_resolution=keep_resolution)
            return

    if writer == "av":
        write_video_av(itr, out_file, fps=fps, keep_resolution=keep_resolution)
        return

    raise ValueError(f"Invalid writer: {writer}")
