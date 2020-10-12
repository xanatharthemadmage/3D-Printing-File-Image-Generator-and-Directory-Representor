3D-Printing File Image Generator and Directory Representor is a tool designed to help 3d-print file collectors visualize their collections.

The program uses Blender to create a .pngimage for every .stl or .obj file in a directory. 
The generated .png is then placed in the same folder as the file. 

All the images generated over within in the run are combined into one image quilt which is placed in the main directory.

Additionally a quilt can be placed at every directory level which contains stl files. 



3D-Printing File Image Generator and Directory Representor is designed to work in blender and requires the python Pillow libarary. 

Requires Blender 2.8.3 
Requires Python 3.7.4
Requires Pillow 

##########Setup############ 



##Install: 
Install Blender 2.83
Install python 3.7.4 including system path
Rename blender's python folder to pythonBackup* (?:\Program Files\Blender Foundation\Blender\2.83\) 

Install pillow to system python.
To install Pillow open your system's terminal and run 

python -m ensure pip --default-pip 
python -m pip install -upgrade pip
python -m pip install wheel 
python -m pip install Pillow


*(Removing it will make blender default to system python)


####### Script and Blender Setup #########

To open the script simply open the blend file
 
####### Running the Script ################

Place the top directory you want to scan in the sript. 
StartPath = "C:\YOUR PATH\GOES HERE" 

Edit the path according to the instructions in the file. 
StartPath = "C:\\YOUR PATH\\GOES HERE"

Open Blenders System Console 
Window->Toggle system console 
(This is not absolutely necessary but it will update you with progress) 

Click "run script" at the top of the scripting editor.

Your main blender window will lockup while the script executes. 
Watch the system console for details.



https://github.com/python-pillow/Pillow
