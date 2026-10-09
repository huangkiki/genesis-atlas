"""Genesis 1.4.3 data-ownership examples; AST checked, never executed.

No initialization, build, stepping loop, training environment or benchmark.
The caller owns the scene, task lifecycle, metadata and output paths.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import genesis as gs
    from genesis.engine.entities.rigid_entity.rigid_entity import RigidEntity
    from genesis.recorders.base_recorder import Recorder
    from numpy.typing import NDArray
    from torch import Tensor


def _owned_cpu_array(tensor: Tensor) -> NDArray:
    """Detach gradients and give the consumer independent host storage."""
    return tensor.detach().cpu().numpy().copy()


def copy_transition_before_reset(
    scene: gs.Scene,
    robot: RigidEntity,
    *,
    transition_index: int,
    episode_id: Tensor,
    obs: Tensor,
    action: Tensor,
    reward: Tensor,
    next_obs: Tensor,
    terminated: Tensor,
    truncated: Tensor,
) -> dict[str, object]:
    """Capture a fixed-batch task transition after step and BEFORE any reset.

    All tensors use the caller's current batch ordering. obs/action are retained
    from before the step; reward/next_obs/flags describe its result. The action
    here is the policy request; record delayed native commands separately when
    the task applies latency. This cannot recover a terminal observation already
    discarded by an auto-reset environment.
    """
    return {
        "transition_index": transition_index,
        "episode_id": _owned_cpu_array(episode_id),
        "obs": _owned_cpu_array(obs),
        "policy_action": _owned_cpu_array(action),
        "reward": _owned_cpu_array(reward),
        "next_obs_before_reset": _owned_cpu_array(next_obs),
        "terminated": _owned_cpu_array(terminated),
        "truncated": _owned_cpu_array(truncated),
        "next_env_time_s": _owned_cpu_array(scene.get_time()),
        "next_qpos": _owned_cpu_array(robot.get_qpos()),
        "next_dofs_velocity": _owned_cpu_array(robot.get_dofs_velocity()),
    }


def register_state_log_before_build(
    scene: gs.Scene, robot: RigidEntity, filename: str
) -> Recorder:
    """Register a small NPZ state log, not a transition/replay buffer.

    Supply a .npz filename. Native recording samples before a step and adds the
    final state on stop. The caller must eventually call scene.stop_recording().
    NPZ holds all samples until cleanup: this is a short-log teaching example,
    not a memory-bounded collector. Store episode IDs and model schema separately.
    """
    import genesis as gs

    capture_index = 0

    def read_state() -> dict[str, object]:
        nonlocal capture_index
        data = {
            "capture_index": capture_index,
            "env_time_s": _owned_cpu_array(scene.get_time()),
            "qpos": _owned_cpu_array(robot.get_qpos()),
            "dofs_velocity": _owned_cpu_array(robot.get_dofs_velocity()),
        }
        capture_index += 1
        return data

    return scene.add_recorder(
        data_func=read_state,
        rec_options=gs.options.recorders.NPZFile(filename=filename, hz=None),
    )
