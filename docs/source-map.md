# genesis-atlas 固定版本源码入口

阅读基线：`216a708e06124595521a9d36a51fae5393fd4ff8`。以下入口已核对官方 Git 树与文件内容身份；不是全仓审查或运行验收记录。

本阶段先理解引擎架构、建模、步进、控制、接触/求解、传感器/渲染、性能与扩展。独立实验、基准、训练和评分暂不开展，后续复用 DexLab。

| 源码文件 | 阅读目的 |
|---|---|
| [genesis/__init__.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/__init__.py) | 核对对象职责、数据布局、参数与版本约定 |
| [genesis/engine/scene.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/engine/scene.py) | 追踪构建、步进、数据更新与生命周期 |
| [genesis/engine/simulator.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/engine/simulator.py) | 追踪构建、步进、数据更新与生命周期 |
| [genesis/options/solvers.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/options/solvers.py) | 识别算法、输入状态、配置与限制 |
| [genesis/engine/entities/rigid_entity/rigid_entity.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/engine/entities/rigid_entity/rigid_entity.py) | 核对对象职责、数据布局、参数与版本约定 |
| [genesis/engine/solvers/rigid/constraint/solver.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/engine/solvers/rigid/constraint/solver.py) | 识别算法、输入状态、配置与限制 |
| [genesis/engine/solvers/rigid/constraint/noslip.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/engine/solvers/rigid/constraint/noslip.py) | 识别算法、输入状态、配置与限制 |
| [genesis/engine/solvers/rigid/rigid_solver.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/engine/solvers/rigid/rigid_solver.py) | 识别算法、输入状态、配置与限制 |
| [genesis/vis/camera.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/vis/camera.py) | 区分传感数据、可视化与物理状态 |
| [genesis/options/sensors/tactile.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/options/sensors/tactile.py) | 核对对象职责、数据布局、参数与版本约定 |
| [examples/tutorials/hello_genesis.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/examples/tutorials/hello_genesis.py) | 理解官方最小使用顺序；本轮不执行 |
