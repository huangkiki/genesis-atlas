"""Genesis E1 native API reading example; syntax checked, NOT executed.

No physics step, experiment, asset download, or benchmark is included.
A local run would initialize Genesis and build a simple model.
"""

import genesis as gs


def main() -> None:
    gs.init(backend=gs.cpu, precision="64")
    scene = gs.Scene(
        sim_options=gs.options.SimOptions(dt=0.01, substeps=4),
        show_viewer=False,
    )
    body = scene.add_entity(
        morph=gs.morphs.Box(size=(0.2, 0.1, 0.1), pos=(0.0, 0.0, 1.0)),
        material=gs.materials.Rigid(rho=1000.0),
    )
    scene.build(n_envs=0)

    # Public entity getters omit the batch dimension for n_envs=0.
    q = body.get_qpos()
    v = body.get_dofs_velocity()
    print("n_qs, n_dofs:", body.n_qs, body.n_dofs)
    print("q, v shapes:", tuple(q.shape), tuple(v.shape))
    print("authored pose:", body.get_pos(), body.get_quat())
    print("solver origin:", body.get_pos(relative=False))

    # Getter tensors are copies: mutation requires an explicit setter.
    saved_q = q.clone()
    body.set_qpos(saved_q, zero_velocity=True)

    # A SimState is a basic state query, not a whole-program checkpoint.
    snapshot = scene.get_state()
    scene.reset(snapshot)  # Also registers snapshot as the next default init state.
    scene.reset()          # Resets to that registered state; time starts at zero.
    print("time after reset:", scene.get_time())


if __name__ == "__main__":
    main()
