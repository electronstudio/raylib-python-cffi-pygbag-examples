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
    """
    
    Example converted to Python from:
    http://bedroomcoders.co.uk/raylib-fog/
    
         port to python completed by codifies - dont know who started it
    
    
    """
    
    import raylib as rl
    
    from raylib.colors import *
    import math
    
    from rlmath import *
    from light_system import *
    
    rl.SetConfigFlags(rl.FLAG_MSAA_4X_HINT | rl.FLAG_WINDOW_RESIZABLE)
    rl.InitWindow(1280, 768, b'Fog Test')
    platform.window.window_resize()
    
    camera = rl.ffi.new('struct Camera3D *', [
        [6, 2, 6],
        [0, .5, 0],
        [0, 1, 0],
        45,
        rl.CAMERA_PERSPECTIVE
    ])
    
    model = rl.LoadModelFromMesh(rl.GenMeshTorus(0.4, 1, 16, 32))
    model2 = rl.LoadModelFromMesh(rl.GenMeshCube(1, 1, 1))
    model3 = rl.LoadModelFromMesh(rl.GenMeshSphere(0.5, 32, 32))
    
    texture = rl.LoadTexture(b'resources/test.png')
    
    model.materials[0].maps[rl.MATERIAL_MAP_ALBEDO].texture = texture
    model2.materials[0].maps[rl.MATERIAL_MAP_ALBEDO].texture = texture
    model3.materials[0].maps[rl.MATERIAL_MAP_ALBEDO].texture = texture
    
    light = Light(LIGHT_POINT, [0, 4, 0], Vector3Zero(), WHITE)
    lightSystem = LightSystem([0.2, 0.2, 0.2, 1.0], light)
    
    fog_color = rl.ffi.new('float[]', [0.2, 0.2, 1.0, 1.0])
    fogC = rl.GetShaderLocation(lightSystem.shader, b'fogColor')
    rl.SetShaderValue(lightSystem.shader, fogC, fog_color, rl.SHADER_UNIFORM_VEC4);
    
    fogC = rl.GetShaderLocation(lightSystem.shader, b'fogColor')
    rl.SetShaderValue(lightSystem.shader, fogC, fog_color, rl.SHADER_UNIFORM_VEC4);
    
    fogD = rl.GetShaderLocation(lightSystem.shader, b'FogDensity')
    fogDensity = 0.12
    
    model.materials[0].shader = lightSystem.shader
    model2.materials[0].shader = lightSystem.shader
    model3.materials[0].shader = lightSystem.shader
    
    rl.SetTargetFPS(60)
    a = 0.0
    while not rl.WindowShouldClose():
    
        a += 0.01
        camera.position.x = math.sin(a) * 6
        camera.position.z = math.cos(a) * 6
        rl.UpdateCamera(camera)
    
        lightSystem.update(camera.position)
    
        model.transform = rl.ffi.cast("Matrix *", MatrixMultiply(model.transform, MatrixRotateX(-0.025)))[0]
        model.transform = rl.ffi.cast("Matrix *", MatrixMultiply(model.transform, MatrixRotateZ(0.012)))[0]
    
        if rl.IsKeyDown(rl.KEY_UP):
            fogDensity = min(fogDensity + 0.001, 1)
    
        if rl.IsKeyDown(rl.KEY_DOWN):
            fogDensity = max(fogDensity - 0.001, 0)
    
        rl.SetShaderValue(lightSystem.shader, fogD, rl.ffi.new('float[]', [fogDensity]), rl.SHADER_UNIFORM_FLOAT)
    
        rl.BeginDrawing()
    
        rl.ClearBackground([int(255 * i) for i in fog_color])
    
        if rl.IsKeyDown(rl.KEY_SPACE):
            rl.ClearBackground(BLACK)
    
        rl.BeginMode3D(camera[0])
        rl.DrawModel(model, [0] * 3, 1, WHITE)
        rl.DrawModel(model2, [-2.6, 0, 0], 1, WHITE)
        rl.DrawModel(model3, [2.6, 0, 0], 1, WHITE)
    
        for i in range(-20, 20, 2):
            rl.DrawModel(model, [i, 0, 2], 1, WHITE)
    
        # Raylib removed this function
        # rl.DrawGizmo([1000, 1000, 1000])
    
        rl.EndMode3D()
    
        rl.DrawFPS(10, 10)
        rl.DrawText(f'Up/Down to change fog density: {fogDensity}'.encode('utf-8'), 10, 30, 20, WHITE)
    
        rl.EndDrawing()
    
    rl.UnloadModel(model)
    rl.UnloadModel(model2)
    rl.UnloadModel(model3)
    rl.UnloadTexture(texture)
    rl.UnloadShader(lightSystem.shader)
    rl.CloseWindow()

asyncio.run(main())
