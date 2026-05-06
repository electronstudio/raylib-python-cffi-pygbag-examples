# Running in a web browser

[Pygbag](https://pypi.org/project/pygbag/) >=0.8.7 supports running in a web browser.  Sometimes the latest git version
is recommended.  Current version 0.9.3 works with Raylib 5.5.

Make a folder `my_project` with a file `main.py`:

```python
# /// script
# dependencies = [
#     "cffi",
#     "raylib"
# ]
# ///
import asyncio
import platform
from pyray import *

async def main():   # You MUST have an async main function
    init_window(500, 500, "Hello")
    platform.window.window_resize()  # You MAY want to add this line
    while not window_should_close():
        begin_drawing()
        clear_background(WHITE)
        draw_text("Hello world", 190, 200, 20, VIOLET)
        end_drawing()
        await asyncio.sleep(0) # You MUST call this in your main loop
    close_window()

asyncio.run(main())
```

Then to create the web files and launch a web server:

    python3 -m venv venv
    source venv/bin/activate
    python3 -m pip install pygbag
    python3 -m pygbag --PYBUILD 3.12 --ume_block 0 my_project

You might also need options `--ume_block 0` or `--git`.

Point your browser to http://localhost:8000

Some features may not work, so you can disable them like this:

```python
if platform.system() != "Emscripten":  # audio may not work on current version of emscripten
    init_audio_device()
```

This is all done by Pygbag rather than by me, so you should probably contact them with any issues.
Carefully read all their [documentation](https://pygame-web.github.io/).

It does work for most of [these examples](https://electronstudio.github.io/raylib-python-cffi-pygbag-examples/)
