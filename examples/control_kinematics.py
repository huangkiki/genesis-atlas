"""Genesis E2 native API reading example: syntax checked, NOT executed.

Uses an original two-joint URDF. It has no step loop or task benchmark.
Gains, limits and targets illustrate fields; they are not validated tuning.
"""

from pathlib import Path

import genesis as gs
import torch


def main() -> None:
    gs.init(backend=gs.cpu, precision="64")
    scene = gs.Scene(
        sim_options=gs.options.SimOptions(dt=0.005, substeps=2),
        rigid_options=gs.options.RigidOptions(batch_dofs_info=True),
        show_viewer=False,
    )
    robot = scene.add_entity(
        morph=gs.morphs.URDF(
            file=str(Path(__file__).parent / "assets" / "two_joint_arm.urdf"),
            fixed=True,
            merge_fixed_links=False,
        ),
    )
    scene.build(n_envs=2)
    joints = [robot.get_joint(name) for name in ("shoulder", "elbow")]
    if any(joint.n_qs != 1 or joint.n_dofs != 1 for joint in joints):
        raise ValueError("This reading example requires scalar joints.")
    dofs = [joint.dofs_idx_local[0] for joint in joints]
    qs = [joint.qs_idx_local[0] for joint in joints]
    tip = robot.get_link("forearm")
    tcp = (0.20, 0.0, 0.0)  # In the forearm link frame, in meters.

    # Model parameters have an environment dimension because batch_dofs_info=True.
    robot.set_dofs_kp([[20.0, 15.0], [18.0, 12.0]], dofs_idx_local=dofs)
    robot.set_dofs_kv([[2.0, 1.5], [1.8, 1.2]], dofs_idx_local=dofs)
    robot.set_dofs_force_range([-3.0, -3.0], [3.0, 3.0], dofs_idx_local=dofs)
    robot.control_dofs_position([[0.15, -0.30]], dofs_idx_local=dofs, envs_idx=[1])
    print("current recomputed control effort:", robot.get_dofs_control_force(dofs))

    jacobian = robot.get_jacobian(tip, local_point=tcp)
    print("Jacobian shape (batch, linear+angular, DOF):", tuple(jacobian.shape))
    candidate, error = robot.inverse_kinematics(
        link=tip,
        pos=[[0.32, 0.08, 0.30], [0.30, -0.10, 0.30]],
        local_point=tcp,
        dofs_idx_local=dofs,
        pos_tol=5e-4,
        rot_tol=5e-3,
        seed=0,
        return_error=True,
    )
    print("full q shape and residual:", tuple(candidate.shape), error)
    positions, quaternions = robot.solver.forward_kinematics_query(robot, candidate)
    print("candidate FK shapes:", tuple(positions.shape), tuple(quaternions.shape))

    # IK is a candidate, not success. Orientation is intentionally unconstrained here.
    acceptable = torch.isfinite(candidate).all(dim=-1)
    acceptable &= torch.isfinite(error).all(dim=-1)
    acceptable &= torch.linalg.vector_norm(error[..., :3], dim=-1) <= 5e-4
    lower, upper = robot.get_dofs_limit()
    acceptable &= ((candidate[:, qs] >= lower[:, dofs]) & (candidate[:, qs] <= upper[:, dofs])).all(dim=-1)
    selected = acceptable.nonzero(as_tuple=True)[0]
    if selected.numel():
        # Only scalar joints: convert absolute q to reference-relative DOF position.
        reference = torch.as_tensor(robot.init_qpos, dtype=gs.tc_float, device=gs.device)
        target = candidate[selected][:, qs] - reference[qs]
        robot.control_dofs_position(target, dofs_idx_local=dofs, envs_idx=selected)
    # No scene.step(): no dynamic tracking, collision, or grasping claim is made.


if __name__ == "__main__":
    main()
