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
    import raylib as rl
    
    
    
    
    #// Initialization
    #//--------------------------------------------------------------------------------------
    screenWidth = 800;
    screenHeight = 450;
    
    rl.SetConfigFlags(rl.FLAG_MSAA_4X_HINT| rl.FLAG_WINDOW_RESIZABLE);  # Enable Multi Sampling Anti Aliasing 4x (if available)
    rl.InitWindow(screenWidth, screenHeight, b"raylib [shaders] example - basic lighting")
    platform.window.window_resize()
    
    camera = rl.ffi.new('struct Camera3D *', [
        [2, 12, 6],
        [0, .5, 0],
        [0, 1, 0],
        45,
        rl.CAMERA_PERSPECTIVE
    ])
    
    imBlank = rl.GenImageColor(1024, 1024, rl.BLANK)
    texture = rl.LoadTextureFromImage(imBlank)  #// Load blank texture to fill on shader
    rl.UnloadImage(imBlank);
    
    #// NOTE: Using GLSL 330 shader version, on OpenGL ES 2.0 use GLSL 100 shader version
    shader = rl.LoadShader(b"", b"resources/shaders/glsl330/cubes_panning.fs");
    
    time = rl.ffi.new("float *", 0.0)
    timeLoc = rl.GetShaderLocation(shader, b"uTime");
    rl.SetShaderValue(shader, timeLoc, time, rl.SHADER_UNIFORM_FLOAT);
        
    
    rl.SetTargetFPS(60)                      # // Set our game to run at 60 frames-per-second
    #//--------------------------------------------------------------------------------------
    
    #// Main game loop
    while not rl.WindowShouldClose():            #// Detect window close button or ESC key
        #// Update
        #//----------------------------------------------------------------------------------
        time[0] = rl.GetTime();
        rl.SetShaderValue(shader, timeLoc, time, rl.SHADER_UNIFORM_FLOAT);
    
        #//----------------------------------------------------------------------------------
    
        #// Draw
        #//----------------------------------------------------------------------------------
        rl.BeginDrawing()
    
        rl.ClearBackground(rl.RAYWHITE)
    
        rl.BeginShaderMode(shader)    #// Enable our custom shader for next shapes/textures drawings
        rl.DrawTexture(texture, 0, 0, rl.WHITE)  #// Drawing BLANK texture, all magic happens on shader
        rl.EndShaderMode()            #// Disable our custom shader, return to default shader
    
        rl.DrawText(b"BACKGROUND is PAINTED and ANIMATED on SHADER!", 10, 10, 20, rl.MAROON);
    
    
        rl.EndDrawing()
    #//----------------------------------------------------------------------------------
    
    
    #// De-Initialization
    #//--------------------------------------------------------------------------------------
    
    
    rl.UnloadTexture(texture)     #// Unload the texture
    
    rl.CloseWindow()              #// Close window and OpenGL context

asyncio.run(main())
