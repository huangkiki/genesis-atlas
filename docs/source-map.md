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

## E1 新增阅读入口

下面的文件身份已核对；阅读重点限定为最后一列，不代表完整算法均已审查。专题内给出固定行链接。

| 源码文件 | 阅读目的 |
|---|---|
| [genesis/options/morphs.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/options/morphs.py) | 姿态校验、offset/align、文件导入、固定 link 合并与几何选项 |
| [genesis/utils/geom.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/utils/geom.py) | 四元数乘法、旋转/平移变换与惯量换系 |
| [genesis/utils/urdf.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/utils/urdf.py) | URDF惯量读取、尺寸/质量/惯量缩放与固定关节合并 |
| [genesis/utils/mjcf.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/utils/mjcf.py) | joint维度映射、解析器来源和不支持项的警告 |
| [genesis/engine/states/solvers.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/engine/states/solvers.py) | 各solver查询状态、基础SimState与完整checkpoint类型 |
| [genesis/engine/states/entities.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/engine/states/entities.py) | 实体查询状态与粒子/顶点布局 |
| [genesis/engine/states/cache.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/engine/states/cache.py) | 查询状态缓存与梯度生命周期 |
| [genesis/engine/solvers/base_solver.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/engine/solvers/base_solver.py) | checkpoint数组复制、data默认能力边界 |
| [genesis/engine/entities/base_entity.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/engine/entities/base_entity.py) | Entity基类生命周期和归属 |
| [genesis/engine/entities/particle_entity.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/engine/entities/particle_entity.py) | 粒子实体与solver状态范围 |
| [genesis/engine/solvers/mpm_solver.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/engine/solvers/mpm_solver.py) | 多物理get_state/set_state的字段与envs_idx消费情况；完整checkpoint能力边界 |
| [genesis/engine/solvers/sph_solver.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/engine/solvers/sph_solver.py) | 多物理get_state/set_state的字段与envs_idx消费情况；完整checkpoint能力边界 |
| [genesis/engine/solvers/pbd_solver.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/engine/solvers/pbd_solver.py) | 多物理get_state/set_state的字段与envs_idx消费情况；完整checkpoint能力边界 |
| [genesis/engine/solvers/fem_solver.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/engine/solvers/fem_solver.py) | 多物理get_state/set_state的字段与envs_idx消费情况；完整checkpoint能力边界 |
| [genesis/engine/solvers/sf_solver.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/engine/solvers/sf_solver.py) | 多物理get_state/set_state的字段与envs_idx消费情况；完整checkpoint能力边界 |
| [genesis/engine/solvers/tool_solver.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/engine/solvers/tool_solver.py) | 多物理get_state/set_state的字段与envs_idx消费情况；完整checkpoint能力边界 |
| [genesis/engine/materials/rigid.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/engine/materials/rigid.py) | 密度来源和材质职责 |
| [genesis/engine/entities/rigid_entity/inertial.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/engine/entities/rigid_entity/inertial.py) | 质量/COM/惯量的几何估计、组合和显式值解析 |
| [genesis/engine/entities/rigid_entity/rigid_joint.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/engine/entities/rigid_entity/rigid_joint.py) | 配置与DOF索引、局部/全局地址 |
| [genesis/engine/entities/rigid_entity/rigid_link.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/engine/entities/rigid_entity/rigid_link.py) | link与inertial属性的表示入口 |
| [genesis/engine/solvers/rigid/abd/forward_dynamics.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/engine/solvers/rigid/abd/forward_dynamics.py) | 速度/位置积分、局部四元数增量、中点分支和隐式阻尼 |
| [genesis/engine/solvers/rigid/abd/forward_kinematics.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/engine/solvers/rigid/abd/forward_kinematics.py) | 配置到世界link姿态、DOF位置、空间速度的转换 |
| [genesis/engine/solvers/kinematic_solver.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/engine/solvers/kinematic_solver.py) | 公共getter的复制/转置和默认坐标语义 |
| [genesis/utils/array_class.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/utils/array_class.py) | 内部数组分类、STATE/WARMSTART/DERIVED与checkpoint集合 |

## E2 新增阅读入口

[驱动与机器人专题](control-robotics-tasks.md)以派生实体→solver→kernel核对接口，以下文件只声明表中范围的源码阅读。

| 源码文件 | 阅读目的 |
|---|---|
| [genesis/engine/solvers/rigid/abd/accessor.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/engine/solvers/rigid/abd/accessor.py) | 追踪控制模式/目标写入与当前控制力重算、限幅 |
| [genesis/engine/solvers/rigid/abd/inverse_kinematics.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/engine/solvers/rigid/abd/inverse_kinematics.py) | Jacobian行/列与frame，DLS/候选/限位分支，FK查询的临时写入恢复 |
| [genesis/utils/misc.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/utils/misc.py) | 目标shape广播和环境×DOF矩形写入 |
| [genesis/utils/path_planning.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/genesis/utils/path_planning.py) | 原生RRT/RRTConnect的关节限制、接触排除、有效性及状态恢复 |
| [examples/tutorials/control_your_robot.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/examples/tutorials/control_your_robot.py) | 官方名字映射及模式切换示例；仅阅读，不执行 |
| [examples/tutorials/IK_motion_planning_grasp.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/examples/tutorials/IK_motion_planning_grasp.py) | 官方IK→规划→驱动调用顺序；不将示例当抓取验收 |
| [examples/tutorials/batched_IK.py](https://github.com/Genesis-Embodied-AI/genesis-world/blob/216a708e06124595521a9d36a51fae5393fd4ff8/examples/tutorials/batched_IK.py) | 官方批量IK调用入口；不执行 |
