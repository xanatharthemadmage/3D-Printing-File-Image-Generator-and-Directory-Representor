Uses Blender to create a .png for every file .stl or .obj file in a directory. Then places that .png in the same folder as the file. Finally combines all the images made in the session into one picture and places it in the root directory

Requires Blender 2.8.X Requires Pillow

Setup 

Install Blender 
Install Pillow within Blender python 
if this doesn't work install python 3.x.x to system, rename blender's python, then install pillow to system python.

Open the provided scene

Open the provided script in the sripting editor of blender

Save the scene to commit the changes.

Usage Place the top directory you want to scan in StartPath Open Blenders system Console (window->Toggle system console) (not necessary but it shows the progress) Click run script. Your main blender window will lockup while the script executes. Watch the system console for details
