"""Defines an API for the most commonly used components.

This lets you just have a single import like `from ml import api` then use,
for example, `api.conf_field(...)` to access various components.

There wasn't an explicit dictating which functions to include here, it was just
whichever functions seemed like they would be generally useful to have on
hand quickly.
"""

__all__ = [
    "ActivationType",
    "add_project_dir",
    "as_cpu_tensor",
    "as_numpy_array",
    "assert_no_nans",
    "AsyncEnvironmentWorker",
    "AsyncIterableDataset",
    "AsyncWorkerPool",
    "atomic_save",
    "AudioFile",
    "AudioMagStftConverter",
    "AudioMfccConverter",
    "AudioProps",
    "AudioPyworldConverter",
    "AudioSarFileDataset",
    "AudioSarFileSpeakerDataset",
    "AudioStftConverter",
    "AudioToHifiGanMels",
    "autocast_all",
    "autocast_tensors",
    "base_device",
    "BaseEnvironmentWorker",
    "BaseLearningTrainer",
    "BaseLearningTrainerConfig",
    "BaseLRScheduler",
    "BaseLRSchedulerConfig",
    "BaseModel",
    "BaseModelConfig",
    "BaseODESolver",
    "BaseOptimizer",
    "BaseOptimizerConfig",
    "BaseTask",
    "BaseTaskConfig",
    "BaseTrainer",
    "BaseTrainerConfig",
    "Batch",
    "BiFPN",
    "BoolEnvVar",
    "cached_object",
    "cast_activation_type",
    "cast_beta_schedule",
    "cast_embedding_kind",
    "cast_init_type",
    "cast_norm_type",
    "cast_parametrize_norm_type",
    "cast_solver_type",
    "check_md5",
    "check_sha256",
    "ChunkSampler",
    "Clamp",
    "ClippifyDataset",
    "collate_non_null",
    "collate",
    "CollateMode",
    "colorize",
    "ColumnParallelLinear",
    "combine_grads",
    "compress_folder_to_sds",
    "conf_field",
    "configure_logging",
    "ConsistencyModel",
    "detect_device",
    "DictIndex",
    "DiffusionBetaSchedule",
    "drop_path",
    "DropPath",
    "ensure_downloaded",
    "Environment",
    "error_handling_dataset",
    "ErrorHandlingConfig",
    "EulerODESolver",
    "FiniteScalarQuantization",
    "format_timedelta",
    "fourier_embeddings",
    "FourierEmbeddings",
    "freeze_non_lora_",
    "from_args",
    "gated_residual",
    "GaussianDiffusion",
    "GenerativeAdversarialNetworkRoundRobinTask",
    "GenerativeAdversarialNetworkRoundRobinTaskConfig",
    "GenerativeAdversarialNetworkTask",
    "GenerativeAdversarialNetworkTaskConfig",
    "get_activation",
    "get_args",
    "get_audio_props",
    "get_cache_dir",
    "get_data_dir",
    "get_dataset_split_for_phase",
    "get_dataset_splits",
    "get_diffusion_beta_schedule",
    "get_distributed_backend",
    "get_eval_run_dir",
    "get_exp_name",
    "get_image_mask",
    "get_local_rank_optional",
    "get_local_rank",
    "get_local_world_size_optional",
    "get_local_world_size",
    "get_master_addr",
    "get_master_port",
    "get_model_dir",
    "get_norm_1d",
    "get_norm_2d",
    "get_norm_3d",
    "get_norm_linear",
    "get_ode_solver",
    "get_parametrization_norm",
    "get_positional_embeddings",
    "get_random_port",
    "get_rank_optional",
    "get_rank",
    "get_run_dir",
    "get_s3_data_bucket",
    "get_s3_runs_bucket",
    "get_state_dict_prefix",
    "get_type_from_string",
    "get_worker_info",
    "get_world_size_optional",
    "get_world_size",
    "HeunODESolver",
    "ImageGradLoss",
    "InfinitePrefetcher",
    "init_",
    "init_and_run",
    "init_dist",
    "init_empty_weights",
    "init_parallelism",
    "InitializationType",
    "instantiate_config",
    "IntEnvVar",
    "invert_grad",
    "is_debugging",
    "is_distributed",
    "is_master",
    "kl_div_pair_loss",
    "kl_div_single_loss",
    "KMeans",
    "launch_subprocesses",
    "LearnedPositionalEmbeddings",
    "load_model_and_task",
    "log_cosh_loss",
    "log_stft_magnitude_loss",
    "LookupFreeQuantization",
    "lora",
    "LoraConv1d",
    "LoraConv2d",
    "LoraConvTranspose1d",
    "LoraConvTranspose2d",
    "LoraEmbedding",
    "LoraGRU",
    "LoraLinear",
    "LoraLSTM",
    "loss_fn",
    "Loss",
    "LossFn",
    "LPIPS",
    "make_bold",
    "maybe_colorize",
    "maybe_lora_weight_norm",
    "maybe_lora",
    "MelLoss",
    "meta_to_empty_func",
    "MFCCLoss",
    "MultiheadAttention",
    "MultiIterDataset",
    "MultiIterDatasetInfo",
    "MultiprocessConfig",
    "MultiProcessLauncher",
    "MultiProcessLauncherConfig",
    "MultiResolutionSTFTLoss",
    "namespace_context",
    "NextTokenDiscriminator",
    "NormType",
    "nucleus_sampling",
    "ODESolverType",
    "open_atomic",
    "Output",
    "pad_all",
    "pad_sequence",
    "parallel_group_info",
    "ParallelEmbedding",
    "parallelism_is_initialized",
    "ParametrizationNormType",
    "parse_cli",
    "PathEnvVar",
    "Phase",
    "Prefetcher",
    "pseudo_huber_loss",
    "read_audio_random_order",
    "read_audio",
    "read_gif",
    "read_video",
    "rechunk_audio",
    "recursive_apply",
    "recursive_chunk",
    "register_logger",
    "register_lr_scheduler",
    "register_model",
    "register_optimizer",
    "register_task",
    "register_trainer",
    "ReinforcementLearningTask",
    "ReinforcementLearningTaskConfig",
    "ReinforcementLearningTrainer",
    "ReinforcementLearningTrainerConfig",
    "reset_lora_weights_",
    "reset_parallelism",
    "residual",
    "ResidualVectorQuantization",
    "RK4ODESolver",
    "rotary_embeddings",
    "RotaryEmbeddings",
    "RowParallelLinear",
    "RwkvAttention",
    "RwkvAttentionState",
    "RwkvBlock",
    "RwkvFeedForward",
    "RwkvFeedForwardState",
    "RwkvStack",
    "RwkvState",
    "scale_grad",
    "SdsDataPipe",
    "set_distributed_backend",
    "set_random_seed",
    "set_slurm_master_addr_and_port",
    "set_slurm_rank_and_world_size",
    "SinusoidalEmbeddings",
    "SlurmLauncher",
    "SlurmLauncherConfig",
    "spectral_convergence_loss",
    "SpectrogramToMFCCs",
    "spinnerator",
    "SSIMLoss",
    "stage_environment",
    "State",
    "stft_magnitude_loss",
    "STFTLoss",
    "streamable_cbr",
    "streaming_add",
    "streaming_conv_1d",
    "streaming_conv_transpose_1d",
    "StreamingConv1d",
    "StreamingConvTranspose1d",
    "StreamingDataset",
    "StreamingDatasetNoIndex",
    "StrEnvVar",
    "StrSetEnvVar",
    "SupervisedLearningTask",
    "SupervisedLearningTaskConfig",
    "SupervisedLearningTrainer",
    "SupervisedLearningTrainerConfig",
    "swap_grads",
    "SyncEnvironmentWorker",
    "SyncWorkerPool",
    "test_dataset",
    "test_environment",
    "test_task",
    "timeout",
    "Timer",
    "token_file",
    "TokenReader",
    "TokenWriter",
    "TransformerEncoder",
    "TransformerEncoderLayer",
    "transforms",
    "UNet",
    "VectorQuantization",
    "VideoFileDataset",
    "WorkerPool",
    "write_audio",
    "write_gif",
    "write_video",
]

from ml.core.common_types import Batch, Loss, Output
from ml.core.config import conf_field
from ml.core.env import (
    BoolEnvVar,
    IntEnvVar,
    PathEnvVar,
    StrEnvVar,
    StrSetEnvVar,
    get_cache_dir,
    get_data_dir,
    get_eval_run_dir,
    get_exp_name,
    get_model_dir,
    get_run_dir,
    get_s3_data_bucket,
    get_s3_runs_bucket,
    is_debugging,
)
from ml.core.registry import (
    add_project_dir,
    register_logger,
    register_lr_scheduler,
    register_model,
    register_optimizer,
    register_task,
    register_trainer,
)
from ml.core.state import Phase, State
from ml.launchers.mp import MultiProcessLauncher, MultiProcessLauncherConfig
from ml.launchers.slurm import (
    SlurmLauncher,
    SlurmLauncherConfig,
    set_slurm_master_addr_and_port,
    set_slurm_rank_and_world_size,
)
from ml.loggers.multi import namespace_context
from ml.lr_schedulers.base import BaseLRScheduler, BaseLRSchedulerConfig
from ml.models.activations import ActivationType, Clamp, cast_activation_type, get_activation
from ml.models.architectures.attention import (
    MultiheadAttention,
    TransformerEncoder,
    TransformerEncoderLayer,
    nucleus_sampling,
)
from ml.models.architectures.bifpn import BiFPN
from ml.models.architectures.rwkv import (
    RwkvAttention,
    RwkvAttentionState,
    RwkvBlock,
    RwkvFeedForward,
    RwkvFeedForwardState,
    RwkvStack,
    RwkvState,
)
from ml.models.architectures.unet import UNet
from ml.models.base import BaseModel, BaseModelConfig
from ml.models.embeddings import (
    FourierEmbeddings,
    LearnedPositionalEmbeddings,
    RotaryEmbeddings,
    SinusoidalEmbeddings,
    cast_embedding_kind,
    fourier_embeddings,
    get_positional_embeddings,
    rotary_embeddings,
)
from ml.models.init import InitializationType, cast_init_type, init_
from ml.models.kmeans import KMeans
from ml.models.lora import (
    LoraConv1d,
    LoraConv2d,
    LoraConvTranspose1d,
    LoraConvTranspose2d,
    LoraEmbedding,
    LoraGRU,
    LoraLinear,
    LoraLSTM,
    freeze_non_lora_,
    lora,
    maybe_lora,
    maybe_lora_weight_norm,
    reset_lora_weights_,
)
from ml.models.modules import (
    DropPath,
    StreamingConv1d,
    StreamingConvTranspose1d,
    combine_grads,
    drop_path,
    gated_residual,
    invert_grad,
    residual,
    scale_grad,
    streamable_cbr,
    streaming_add,
    streaming_conv_1d,
    streaming_conv_transpose_1d,
    swap_grads,
)
from ml.models.norms import (
    NormType,
    ParametrizationNormType,
    cast_norm_type,
    cast_parametrize_norm_type,
    get_norm_1d,
    get_norm_2d,
    get_norm_3d,
    get_norm_linear,
    get_parametrization_norm,
)
from ml.models.parallel import ColumnParallelLinear, ParallelEmbedding, RowParallelLinear
from ml.models.quantization.fsq import FiniteScalarQuantization
from ml.models.quantization.lfq import LookupFreeQuantization
from ml.models.quantization.vq import ResidualVectorQuantization, VectorQuantization
from ml.optimizers.base import BaseOptimizer, BaseOptimizerConfig
from ml.tasks.base import BaseTask, BaseTaskConfig
from ml.tasks.consistency import ConsistencyModel
from ml.tasks.datasets import transforms
from ml.tasks.datasets.async_iterable import AsyncIterableDataset
from ml.tasks.datasets.clippify import ClippifyDataset
from ml.tasks.datasets.collate import CollateMode, collate, collate_non_null, pad_all, pad_sequence
from ml.tasks.datasets.error_handling import ErrorHandlingConfig, error_handling_dataset
from ml.tasks.datasets.multi_iter import DatasetInfo as MultiIterDatasetInfo, MultiIterDataset
from ml.tasks.datasets.samplers import ChunkSampler
from ml.tasks.datasets.streaming import StreamingDataset, StreamingDatasetNoIndex
from ml.tasks.datasets.video_file import VideoFileDataset
from ml.tasks.diffusion import DiffusionBetaSchedule, GaussianDiffusion, cast_beta_schedule, get_diffusion_beta_schedule
from ml.tasks.environments.base import Environment
from ml.tasks.environments.utils import test_environment
from ml.tasks.environments.worker import (
    AsyncEnvironmentWorker,
    AsyncWorkerPool,
    BaseEnvironmentWorker,
    SyncEnvironmentWorker,
    SyncWorkerPool,
    WorkerPool,
)
from ml.tasks.gan.base import GenerativeAdversarialNetworkTask, GenerativeAdversarialNetworkTaskConfig
from ml.tasks.gan.round_robin import (
    GenerativeAdversarialNetworkRoundRobinTask,
    GenerativeAdversarialNetworkRoundRobinTaskConfig,
)
from ml.tasks.losses.audio import (
    MelLoss,
    MFCCLoss,
    MultiResolutionSTFTLoss,
    STFTLoss,
    log_stft_magnitude_loss,
    spectral_convergence_loss,
    stft_magnitude_loss,
)
from ml.tasks.losses.diffusion import pseudo_huber_loss
from ml.tasks.losses.image import LPIPS, ImageGradLoss, SSIMLoss
from ml.tasks.losses.kl import kl_div_pair_loss, kl_div_single_loss
from ml.tasks.losses.loss import LossFn, log_cosh_loss, loss_fn
from ml.tasks.ode import (
    BaseODESolver,
    EulerODESolver,
    HeunODESolver,
    ODESolverType,
    RK4ODESolver,
    cast_solver_type,
    get_ode_solver,
)
from ml.tasks.rl.base import ReinforcementLearningTask, ReinforcementLearningTaskConfig
from ml.tasks.sl.base import SupervisedLearningTask, SupervisedLearningTaskConfig
from ml.trainers.base import BaseTrainer, BaseTrainerConfig
from ml.trainers.learning import BaseLearningTrainer, BaseLearningTrainerConfig
from ml.trainers.rl import ReinforcementLearningTrainer, ReinforcementLearningTrainerConfig
from ml.trainers.sl import SupervisedLearningTrainer, SupervisedLearningTrainerConfig
from ml.utils.amp import autocast_all, autocast_tensors
from ml.utils.argparse import from_args, get_args, get_type_from_string
from ml.utils.atomic import atomic_save, open_atomic
from ml.utils.attention import NextTokenDiscriminator
from ml.utils.audio import (
    AudioFile,
    AudioProps,
    AudioSarFileDataset,
    AudioSarFileSpeakerDataset,
    get_audio_props,
    read_audio,
    read_audio_random_order,
    rechunk_audio,
    write_audio,
)
from ml.utils.augmentation import get_image_mask
from ml.utils.caching import DictIndex, cached_object
from ml.utils.checkpoint import (
    ensure_downloaded,
    get_state_dict_prefix,
    instantiate_config,
    load_model_and_task,
)
from ml.utils.checks import assert_no_nans
from ml.utils.cli import parse_cli
from ml.utils.colors import colorize, make_bold, maybe_colorize
from ml.utils.containers import recursive_apply, recursive_chunk
from ml.utils.data import (
    SdsDataPipe,
    check_md5,
    check_sha256,
    compress_folder_to_sds,
    get_dataset_split_for_phase,
    get_dataset_splits,
    get_worker_info,
)
from ml.utils.datetime import format_timedelta
from ml.utils.device.auto import detect_device
from ml.utils.device.base import InfinitePrefetcher, Prefetcher, base_device
from ml.utils.distributed import (
    get_local_rank,
    get_local_rank_optional,
    get_local_world_size,
    get_local_world_size_optional,
    get_master_addr,
    get_master_port,
    get_random_port,
    get_rank,
    get_rank_optional,
    get_world_size,
    get_world_size_optional,
    is_distributed,
    is_master,
)
from ml.utils.image import read_gif, write_gif
from ml.utils.large_models import init_empty_weights, meta_to_empty_func
from ml.utils.logging import configure_logging
from ml.utils.numpy import as_cpu_tensor, as_numpy_array
from ml.utils.parallel import init_parallelism, parallel_group_info, parallelism_is_initialized, reset_parallelism
from ml.utils.random import set_random_seed
from ml.utils.spectrogram import (
    AudioMagStftConverter,
    AudioMfccConverter,
    AudioPyworldConverter,
    AudioStftConverter,
    AudioToHifiGanMels,
    SpectrogramToMFCCs,
)
from ml.utils.staging import stage_environment
from ml.utils.testing import test_dataset, test_task
from ml.utils.timer import Timer, spinnerator, timeout
from ml.utils.tokens import TokenReader, TokenWriter, token_file
from ml.utils.torch_distributed import (
    MultiprocessConfig,
    get_distributed_backend,
    init_and_run,
    init_dist,
    launch_subprocesses,
    set_distributed_backend,
)
from ml.utils.video import read_video, write_video
