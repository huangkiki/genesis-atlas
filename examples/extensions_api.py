"""Genesis 1.4.3 extension teaching functions; AST checked, never executed.

The caller owns an already-built scene. No init/build/step/backward or optimizer
is run here. The subscriber API is internal and pinned to the reviewed revision.
"""

from __future__ import annotations

from math import isfinite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import genesis as gs
    from genesis.engine.entities.mpm_entity import MPMEntity
    from genesis.engine.solvers.base_solver import Subscriber


def mpm_goal_loss(
    body: MPMEntity, goal_m: gs.Tensor, length_scale_m: float
) -> gs.Tensor:
    """Construct a dimensionless loss without severing the native gradient bridge.

    Preconditions: all body particles active, differentiable rollout recorded,
    goal shape (3,), and goal on the same device with no foreign Scene identity.
    Averaging weights every particle and environment equally. This is a teaching
    objective, not a task-success criterion or a verified optimization recipe.
    """
    if not isfinite(length_scale_m) or length_scale_m <= 0.0:
        raise ValueError("length_scale_m must be finite and positive")
    state = body.get_state()
    error = (state.pos - goal_m) / length_scale_m
    return error.square().sum(dim=-1).mean()


def watch_rigid_geometry(scene: gs.Scene) -> Subscriber:
    """Observe tagged geometry mutations, not every step or model-parameter edit.

    The caller checks the returned handle's pending property and calls clear()
    after consuming it. Lazy notification performs no simulation readback here.
    """
    from genesis.engine.solvers.base_solver import StateChange, Subscriber

    handle = Subscriber(to=frozenset({StateChange.GEOMETRY}))
    scene.rigid_solver.subscribe(handle)
    return handle
