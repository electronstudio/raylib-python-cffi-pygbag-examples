# /// script
# dependencies = [
#     "cffi",
#     "inflection",
#     "raylib"
# ]
# ///
import asyncio
import platform
async def main():
    import pyray as pr
    
    W, H = 640, 480
    
    
    
    
    def make_cube(width, height, length):
        import numpy as np
    
        vertices = np.array([
            -width / 2, -height / 2, length / 2,
            width / 2, -height / 2, length / 2,
            width / 2, height / 2, length / 2,
            -width / 2, height / 2, length / 2,
            -width / 2, -height / 2, -length / 2,
            -width / 2, height / 2, -length / 2,
            width / 2, height / 2, -length / 2,
            width / 2, -height / 2, -length / 2,
            -width / 2, height / 2, -length / 2,
            -width / 2, height / 2, length / 2,
            width / 2, height / 2, length / 2,
            width / 2, height / 2, -length / 2,
            -width / 2, -height / 2, -length / 2,
            width / 2, -height / 2, -length / 2,
            width / 2, -height / 2, length / 2,
            -width / 2, -height / 2, length / 2,
            width / 2, -height / 2, -length / 2,
            width / 2, height / 2, -length / 2,
            width / 2, height / 2, length / 2,
            width / 2, -height / 2, length / 2,
            -width / 2, -height / 2, -length / 2,
            -width / 2, -height / 2, length / 2,
            -width / 2, height / 2, length / 2,
            -width / 2, height / 2, -length / 2
        ], dtype=np.float32)
    
        texcoords = np.array([
            0.0, 0.0,
            1.0, 0.0,
            1.0, 1.0,
            0.0, 1.0,
            1.0, 0.0,
            1.0, 1.0,
            0.0, 1.0,
            0.0, 0.0,
            0.0, 1.0,
            0.0, 0.0,
            1.0, 0.0,
            1.0, 1.0,
            1.0, 1.0,
            0.0, 1.0,
            0.0, 0.0,
            1.0, 0.0,
            1.0, 0.0,
            1.0, 1.0,
            0.0, 1.0,
            0.0, 0.0,
            0.0, 0.0,
            1.0, 0.0,
            1.0, 1.0,
            0.0, 1.0]
            , dtype=np.float32)
    
        normals = np.array([
            0.0, 0.0, 1.0,
            0.0, 0.0, 1.0,
            0.0, 0.0, 1.0,
            0.0, 0.0, 1.0,
            0.0, 0.0, -1.0,
            0.0, 0.0, -1.0,
            0.0, 0.0, -1.0,
            0.0, 0.0, -1.0,
            0.0, 1.0, 0.0,
            0.0, 1.0, 0.0,
            0.0, 1.0, 0.0,
            0.0, 1.0, 0.0,
            0.0, -1.0, 0.0,
            0.0, -1.0, 0.0,
            0.0, -1.0, 0.0,
            0.0, -1.0, 0.0,
            1.0, 0.0, 0.0,
            1.0, 0.0, 0.0,
            1.0, 0.0, 0.0,
            1.0, 0.0, 0.0,
            -1.0, 0.0, 0.0,
            -1.0, 0.0, 0.0,
            -1.0, 0.0, 0.0,
            -1.0, 0.0, 0.0
        ], dtype=np.float32)
    
        indices = np.concatenate([[4 * k, 4 * k + 1, 4 * k + 2, 4 * k, 4 * k + 2, 4 * k + 3] for k in range(0, 6)],
                                 dtype=np.int16)
    
        print(vertices, indices)
        return pr.Mesh(24, 12, vertices, texcoords,
                       None, normals, None, None, indices,
                       None, None, None, None, 0, None), (vertices, texcoords, normals, indices)
    
    
    pr.init_window(W, H, "Mesh creation")
    platform.window.window_resize()
    msh, refs_to_buffers_to_prevent_garbage_collection = make_cube(3, 4, 40)
    pr.upload_mesh(msh, False)
    matdefault = pr.load_material_default()
    eye = pr.matrix_identity()
    
    camera = pr.Camera3D()
    camera.position = pr.Vector3(30.0, 20.0, 30.0)  # Camera position
    camera.target = pr.Vector3(0.0, 0.0, 0.0)  # Camera looking at point
    camera.up = pr.Vector3(0.0, 1.0, 0.0)  # Camera up vector (rotation towards target)
    camera.fovy = 70.0  # Camera field-of-view Y
    camera.projection = pr.CameraProjection.CAMERA_PERSPECTIVE  # Camera projection type
    
    # Export so we can inspect it
    pr.export_mesh(msh, "test-cube-numpy.obj")
    
    while not pr.window_should_close():
        pr.update_camera(camera, pr.CameraMode.CAMERA_ORBITAL)
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)
        pr.begin_mode_3d(camera)
        pr.draw_grid(10, 5.0)
        pr.draw_mesh(msh, matdefault, eye)
        pr.end_mode_3d()
        pr.end_drawing()
        await asyncio.sleep(0)
    pr.close_window()

asyncio.run(main())
