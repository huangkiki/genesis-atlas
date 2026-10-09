"""Read Genesis E3 contact fields from an existing, already-stepped entity.

Source and syntax reviewed only; NOT executed. This file creates no scene,
advances no physics, and defines no experiment or success score. Call it at a
sampling point defined by the caller's existing protocol, with stepping paused.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import torch

if TYPE_CHECKING:
    from genesis.engine.entities.rigid_entity import RigidEntity


def inspect_latest_contact(entity: RigidEntity, env_id: int = 0) -> None:
    """Print the latest contact sample for one entity, excluding self contacts.

    The moment below is about the world origin and contains point-force moments
    only. Genesis's contact dictionary does not export the pure spin/rolling
    couples, so this is not a full six-axis wrench or a time-averaged force.
    """
    n_envs = entity.solver.n_envs
    if not 0 <= env_id < max(1, n_envs):
        raise ValueError("env_id must identify an existing environment.")

    # Padded mode has valid_mask even when scene.build used n_envs=0.
    raw = entity.get_contacts(exclude_self_contact=True, is_padded=True)
    sample = {
        key: (value[env_id] if n_envs else value).detach().clone()
        for key, value in raw.items()
    }
    valid = sample["valid_mask"]
    positions = sample["position"][valid]
    links_a = sample["link_a"][valid]
    belongs_to_a = (links_a >= entity.link_start) & (links_a < entity.link_end)
    forces = torch.where(
        belongs_to_a[:, None],
        sample["force_a"][valid],
        sample["force_b"][valid],
    )
    linear_force_world = forces.sum(dim=0)
    point_moment_at_world_origin = torch.linalg.cross(positions, forces, dim=-1).sum(dim=0)

    print("Valid external contact slots:", positions.shape[0])
    print("Latest sampled linear contact force [N, world]:", linear_force_world)
    print("Point-force moment only [N m, world origin]:", point_moment_at_world_origin)
    print("These are latest-substep samples, not whole-step impulse or mean force.")
