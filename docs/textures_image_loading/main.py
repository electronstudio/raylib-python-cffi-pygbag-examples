# /// script
# dependencies = [
#     "cffi",
#     "inflection",
#     "raylib"
# ]
# ///
import asyncio
import platform
from raylib import *
from pyray import *
async def main():
    
    screenWidth = 800
    screenHeight = 450
    
    InitWindow(screenWidth, screenHeight, b"raylib [textures] example - image loading")
    platform.window.window_resize()
    
    image = LoadImage(b"resources/raylib_logo.png")
    texture = LoadTextureFromImage(image)
    
    UnloadImage(image)
    
    while not WindowShouldClose():
    
        BeginDrawing()
    
        ClearBackground(RAYWHITE)
    
        DrawTexture(texture, int(screenWidth/2 - texture.width/2), int(screenHeight/2 - texture.height/2), WHITE)
    
        DrawText(b"this IS a texture loaded from an image!", 300, 370, 10, GRAY)
    
        EndDrawing()
        await asyncio.sleep(0)
    
    UnloadTexture(texture)
    
    CloseWindow()               

asyncio.run(main())
