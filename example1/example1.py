import asyncio


async def main():
    import asyncio

    import pyray as pr
    import platform

    pr.init_window(800, 450, "Raylib texture test")
    try:
        platform.window.window_resize()
    except:
        pass
    pr.set_target_fps(60)

    image = pr.gen_image_color(800, 400, (0, 0, 0, 255))
    texture = pr.load_texture_from_image(image)
    pr.update_texture(texture, image.data)

    camera = pr.Camera3D([18.0, 16.0, 18.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0)
    image = pr.load_image("heightmap.png")
    texture = pr.load_texture_from_image(image)
    mesh = pr.gen_mesh_heightmap(image, (16, 8, 16))
    model = pr.load_model_from_mesh(mesh)
    model.materials.maps[pr.MaterialMapIndex.MATERIAL_MAP_ALBEDO].texture = texture

    pr.unload_image(image)

    while not pr.window_should_close():
        pr.update_camera(camera, pr.CAMERA_ORBITAL)
        pr.begin_drawing()
        pr.clear_background(pr.RAYWHITE)
        pr.begin_mode_3d(camera)
        pr.draw_model(model, (-8.0, 0.0, -8.0), 1.0, pr.RED)
        pr.draw_grid(20, 1.0)
        pr.end_mode_3d()
        pr.draw_text("This mesh should be textured", 190, 200, 20, pr.VIOLET)
        pr.end_drawing()
        await asyncio.sleep(0)

    pr.close_window()


asyncio.run(main())
