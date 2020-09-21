3D-Printing File Image Generator and Directory Representor is a tool designed to help 3d-print file collectors visualize their collections.

The program uses Blender to create a .png for every .stl or .obj file in a directory. 
The generated .png is then placed in the same folder as the file. 
Finall, all the images generated over within in the run are combined into one image quilt which is placed in the main directory

3D-Printing File Image Generator and Directory Representor is designed to work in blender and requires the python Pillow libarary. 

Requires Blender 2.8.X 
Requires Python Pillow

##########Setup############ 

Install Blender 2.8.x
Install Pillow within Blender's python interpreter or your system's python interpreter. 

##Install Method 1
#This method may not work
To install Pillow within Blender:
Locate you blender python interpreter (Blender python is in \Program Files\Blender Foundation\Blender [versionnum]\[versionnum]\)(in windows at least)
To install Pillow open your system's terminal and run 

.\python -m ensure pip --default-pip 
.\python -m pip install -upgrade pip
.\python -m pip install Pillow



If you get error "ImportError: cannot import name '_imaging' from 'PIL'"
Try install method two


##Install Method 2: 

Install python 3.x.x (the version should math whatever version your blender version is using)
Rename blender's python folder to pythonBackup*
then install pillow to system python.
To install Pillow open your system's terminal and run 

python -m ensure pip --default-pip 
python -m pip install -upgrade pip
python -m pip install Pillow


*(Removing it will make blender default to system python)



####### Script and Blender Setup #########

To run the script: 

First open the provided scene. 
Then open the provided script in the scripting editor of Blender
Save the scene to commit the changes.

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



*to install pillow open powershell/cmd and run 
"python -m pip install –upgrade pip"
"python -m pip install Pillow"
https://github.com/python-pillow/Pillow
