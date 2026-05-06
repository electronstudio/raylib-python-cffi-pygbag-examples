# Written by AI

import os
import re
import shutil


def process_files(start_dir):
    for root, dirs, files in os.walk(start_dir):
        # Loop through the files that match the pattern '*.py'
        for file in files:
            if file.endswith(".py"):
                # Get the full path of the file
                file_path = os.path.join(root, file)
                # Get the file name without the extension
                file_name = os.path.splitext(file)[0]
                # Get the directory name of the file
                dir_name = os.path.basename(root)

                # Create a new directory with the same name as the file in the output directory
                new_dir = os.path.join(output_dir, file_name)
                os.mkdir(new_dir)
                # Copy the file into the new directory and rename it 'main.py'
                new_file = os.path.join(new_dir, "main.py")
                shutil.copy(file_path, new_file)
                convert(new_file)
                print(f"**** cp -R {start_dir}/resources {new_dir}")
                os.system(f"cp -R {start_dir}/resources {new_dir}")
                os.system(
                    "python3 -m pygbag --PYBUILD 3.12 --can_close 1 --ume_block 0 --build "
                    + new_file
                )
                os.system(f"rm -rf {new_dir}/resources")
                with open(file_path, "r") as f:
                    source_code = f.read()

                # Extract screen dimensions from source code
                width_match = re.search(
                    r"screen[_]?width\s*=\s*(\d+)", source_code, re.IGNORECASE
                )
                height_match = re.search(
                    r"screen[_]?height\s*=\s*(\d+)", source_code, re.IGNORECASE
                )

                screen_width = width_match.group(1) if width_match else "800"
                screen_height = height_match.group(1) if height_match else "450"

                with open(new_dir + "/index.html", "w") as index_file:
                    index_file.write(
                        f"""
                        <html><head>
                        <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" rel="stylesheet" />
                        <title>{file_name}</title>
                        </head>
                        <body>
                        <h1>{file_name}</h1>
                        <iframe src="build/web/index.html" width="{screen_width}px" height="{screen_height}px"></iframe>
                        <p><pre><code class="language-python">{source_code}</code></pre></p>
                        <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
                     <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>

                        </body></html>
                        """
                    )


def convert(file_name):
    with open(file_name, "r") as f:
        # Read the lines of the file
        lines = f.readlines()

    # Create a temporary file name
    temp_file_name = file_name + ".tmp"

    # Open the temporary file in write mode
    with open(temp_file_name, "w") as f:
        # Write the first line to define the main() function
        f.write("""# /// script
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
""")
        # Indent each line of the original file and write it to the temporary file
        for line in lines:
            if "from raylib import *" in line or "from pyray import *" in line:
                pass
            else:
                f.write("    " + line)

            indent = line[: len(line) - len(line.lstrip())]
            if "init_window" in line or "InitWindow" in line:
                f.write(indent + "    platform.window.window_resize()\n")
            if "end_drawing" in line or "EndDrawing" in line:
                f.write(indent + "    await asyncio.sleep(0)\n")

        # Write the last line to call the main() function
        f.write("\nasyncio.run(main())\n")

    # Delete the original file
    os.remove(file_name)

    # Rename the temporary file to the original file name
    os.rename(temp_file_name, file_name)


output_dir = "docs"
os.system(f"rm -rf {output_dir}")
os.mkdir(output_dir)

process_files("raylib-python-cffi/examples/audio")
process_files("raylib-python-cffi/examples/core")
process_files("raylib-python-cffi/examples/models")
process_files("raylib-python-cffi/examples/physics")
process_files("raylib-python-cffi/examples/raygui")
process_files("raylib-python-cffi/examples/shapes")
process_files("raylib-python-cffi/examples/textures")


os.system(f"touch {output_dir}/.nojekyll")

# Write the nav.html file with the list of links
with open(output_dir + "/nav.html", "w") as nav_file:
    nav_file.write("<html>\n<head>\n<title>Directory Index</title>\n</head>\n<body>\n")

    nav_file.write("<h1>Examples</h1>\n")

    nav_file.write("<ul>\n")
    sub_dirs = os.listdir(output_dir)

    # Sort the list of subdirectories in alphabetical order
    sub_dirs.sort()

    for sub_dir in sub_dirs:
        if os.path.isdir(os.path.join(output_dir, sub_dir)):
            nav_file.write(
                f"<li><a href='{sub_dir}/index.html' target='right'>{sub_dir}</a></li>\n"
            )

    nav_file.write("</ul>\n")

    nav_file.write("</body>\n</html>\n")

# Write the index.html file as a frameset
with open(output_dir + "/index.html", "w") as index_file:
    index_file.write("<html>\n<head>\n<title>Directory Index</title>\n</head>\n")
    index_file.write("<frameset cols='250,*'>\n")
    index_file.write("    <frame src='nav.html' name='left'>\n")
    index_file.write("    <frame name='right'>\n")
    index_file.write("</frameset>\n")
    index_file.write("</html>\n")
