"""Native API teaching functions for Genesis 1.4.3; syntax checked, never executed.

Call registration before building an existing all-rigid Scene with its main
Rasterizer. Call capture only after the caller's existing physics step. These
functions do not initialize, build, advance or score a simulation. The two camera
poses and geometry paths are intentionally not a calibrated RGB-D pair.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import genesis as gs
    from genesis.engine.entities.rigid_entity.rigid_entity import RigidEntity
    from genesis.engine.sensors.camera import RasterizerCameraSensor
    from genesis.engine.sensors.contact_force import ContactForceSensor
    from genesis.engine.sensors.depth_camera import DepthCameraSensor
    from genesis.vis.camera import Camera


def register_before_build(scene: gs.Scene, body: RigidEntity) -> tuple[
    Camera, RasterizerCameraSensor, DepthCameraSensor, ContactForceSensor
]:
    """Register native handles in a caller-owned Scene, using its full env batch."""
    import genesis as gs

    camera = scene.add_camera(
        res=(160, 120), pos=(2.0, -2.0, 1.5), lookat=(0.0, 0.0, 0.0), GUI=False
    )
    rgb_sensor = scene.add_sensor(
        gs.sensors.RasterizerCameraOptions(
            res=(160, 120), pos=(2.0, -2.0, 1.5), lookat=(0.0, 0.0, 0.0)
        )
    )
    depth_sensor = scene.add_sensor(
        gs.sensors.DepthCamera(
            pattern=gs.sensors.DepthCameraPattern(res=(160, 120)),
            pos_offset=(-2.0, 0.0, 1.0),  # Static sensor, +X forward.
            return_points=False,
            max_range=10.0,
            no_hit_value=-1.0,
            history_length=0,  # read_image does not reshape a history axis.
        )
    )
    force_sensor = scene.add_sensor(
        gs.sensors.ContactForce(entity_idx=body.idx, link_idx_local=0)
    )
    return camera, rgb_sensor, depth_sensor, force_sensor


def capture_after_step(
    scene: gs.Scene,
    camera: Camera,
    rgb_sensor: RasterizerCameraSensor,
    depth_sensor: DepthCameraSensor,
    force_sensor: ContactForceSensor,
) -> dict[str, object]:
    """Copy native readbacks; labels preserve geometry, frame and sampling source."""
    rgb, axial_depth, segmentation, _ = camera.render(
        rgb=True, depth=True, segmentation=True, colorize_seg=False, force_render=True
    )
    return {
        "global_step_at_read": scene.sim.cur_step_global,
        "dt_s": scene.dt,
        "vis_rgb_u8": rgb.copy(),  # Main Rasterizer returns NumPy arrays.
        "vis_axial_depth_m": axial_depth.copy(),
        "vis_segmentation_ids": segmentation.copy(),
        "vis_segmentation_mapping": dict(scene.visualizer.segmentation_idx_dict),
        "sensor_rgb_u8": rgb_sensor.read().rgb.clone(),
        "ray_range_m": depth_sensor.read_image().clone(),
        "contact_force_link_frame_N": force_sensor.read().clone(),
    }
