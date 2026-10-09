# Genesis Atlas

Understand Genesis through native APIs, physics concepts and versioned source code.

[中文](README.md) · [Introductory guide](docs/guide.md) · [Curriculum](docs/curriculum.md) · [Source map](docs/source-map.md) · [Versions](docs/versions.md) · [Roadmap](docs/roadmap.md) · [Series home](https://github.com/huangkiki/sim-atlas) · [Project tracker](https://github.com/users/huangkiki/projects/2)

Part of **[Sim Atlas](https://github.com/huangkiki/sim-atlas)**, an independent community learning series with two complete planned tracks: applications (modeling, control, robotics, sensing and data) and principles/source (dynamics, contact, solvers, integration and extensions).

The initial guide, pinned source map and [E1 modeling, frames, state and time lesson](docs/modeling-state-time.md) are available in Chinese. E1 covers rigid and multiphysics state layouts, asset and inertia conventions, reset versus checkpoint, and step/substep semantics. [Acceptance and limitations](docs/e1-acceptance.md) distinguish pinned-source review and syntax checks from unperformed runtime validation.

The [E2 control, robotics and task-interface lesson](docs/control-robotics-tasks.md) traces named-joint mapping, batched targets, actuator clipping, FK/Jacobian/IK contracts, native planning and task timing. Its [acceptance record](docs/e2-acceptance.md) lists source limitations and the unexecuted original two-joint example.

The [E3 contact, solvers and force-observation lesson](docs/contact-solvers-forces.md) connects material mixing, contact rows, Newton/CG, stopping rules, warm starts, integration and force sampling. It distinguishes rigid, multiphysics and coupler branches, including limitations of contact readback. Its [acceptance record](docs/e3-acceptance.md) documents source and syntax checks; native execution remains unperformed.

The full course is in development. This phase prioritizes understanding engine subsystems. Minimal snippets support explanation and are explicitly marked when unexecuted. No new simulation campaigns, benchmarks, training or scoring are included; later experimental material will reuse [DexLab](https://github.com/huangkiki/Dexlab) with its original version and workload boundaries.

[Pinned upstream source](https://github.com/Genesis-Embodied-AI/genesis-world/tree/216a708e06124595521a9d36a51fae5393fd4ff8) · [Attribution](THIRD_PARTY.md)
