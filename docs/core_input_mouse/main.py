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
    
    raylib [core] example - Mouse input
    
    """
    from pyray import *
    from raylib.colors import (
        RAYWHITE,
        DARKGRAY,
        MAROON,
        LIME,
        DARKBLUE,
        PURPLE,
        YELLOW,
        ORANGE,
        BEIGE,
    )
    from raylib import (
        MOUSE_BUTTON_LEFT,
        MOUSE_BUTTON_MIDDLE,
        MOUSE_BUTTON_RIGHT,
        MOUSE_BUTTON_SIDE,
        MOUSE_BUTTON_EXTRA,
        MOUSE_BUTTON_FORWARD,
        MOUSE_BUTTON_BACK
    )
    
    # Initialization
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 450
    
    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, 'raylib [core] example - mouse input')
    platform.window.window_resize()
    
    ball_position = Vector2(-100, -100)
    ball_color = DARKBLUE
    
    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    
    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        ball_position = get_mouse_position()
    
        if is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
            ball_color = MAROON
        elif is_mouse_button_pressed(MOUSE_BUTTON_MIDDLE):
            ball_color = LIME
        elif is_mouse_button_pressed(MOUSE_BUTTON_RIGHT):
            ball_color = DARKBLUE
        elif is_mouse_button_pressed(MOUSE_BUTTON_SIDE):
            ball_color = PURPLE
        elif is_mouse_button_pressed(MOUSE_BUTTON_EXTRA):
            ball_color = YELLOW
        elif is_mouse_button_pressed(MOUSE_BUTTON_FORWARD):
            ball_color = ORANGE
        elif is_mouse_button_pressed(MOUSE_BUTTON_BACK):
            ball_color = BEIGE
        # Draw
        begin_drawing()
    
        clear_background(RAYWHITE)
        draw_circle_v(ball_position, 40, ball_color)
        draw_text(
            'move ball with mouse and click mouse button to change color',
            10, 10, 20, DARKGRAY
        )
    
        end_drawing()
        await asyncio.sleep(0)
    
    # De-Initialization
    close_window()  # Close window and OpenGL context

asyncio.run(main())
