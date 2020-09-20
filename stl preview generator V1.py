import bpy
import os
from pathlib import Path
import PIL
from PIL import Image


#moduleName = 'helloModule'
#importlib.import_module(moduleName)

#INFO#
# Edit>Preferecnes>Add-ons search import images as planes



######Start Path############
#Place Starting path inside quotes 
#Due to the way python handles strings you must double back slashes
#Example StartPath = "C:\\3dfiles\\models"
StartPath = "D:\\Documents\\3d prints\\PreSupported Models\\Amazons"


##############
## Options  ##
##############

#Render size
#set the resolution of the output png. Default is 320
renderSize = 640
 
#Material Color
#Set the color of the model

#Background Color 
#Set the color of the background 


#Make a final quilt of all images 
#yes = True 
#no = False
#finalQuilt = True

#########################################################################
#########################################################################
#########################################################################
#########################################################################
#########################################################################
#########################################################################
#########################################################################
#########################################################################
#########################################################################
#########################################################################
#########################################################################
#########################################################################
#########################################################################

#Don't touch this stuff!

#GLOBAL VARS (Don't tell mama)
imageArray = []
ModelData = bpy.data.objects['Model Text']    


########RENDER FUNC#########

#Render function. Takes the starting diretory, the current path, and the name of the file that was passed into the workspace as arguments, outputs the png

def Render(startDir, inputPath, inputFile):
    #call the approriate method for the type of model
    print("Starting import")
    

    print(os.path.join(inputPath,inputFile))
    ModelData.data.body = str(os.path.join(inputPath,inputFile))
    
    if ".stl" in (os.path.join(inputFile)).lower():
        bpy.ops.import_mesh.stl(filepath= os.path.join(inputPath,inputFile), filter_glob='*.stl', files='', directory='', global_scale=1.0, use_scene_unit=False, use_facet_normal=False)
    if ".obj" in (os.path.join(inputFile)).lower():
        bpy.ops.import_scene.obj(filepath= os.path.join(inputPath,inputFile))
        #for some reason .obj files import and are then no seleceted but "active"
        #This workaround searches for the only mesh object and selects it
        #We cannot just search by the file name incase the file name does not match the m
        for ob in bpy.data.objects:
            if ob.type == "MESH": 
                bpy.ops.object.select_all(action='DESELECT') # Deselect all objects
                bpy.context.view_layer.objects.active = ob   # Make the model the active object
                ob.select_set(True)
        
        
    #name the imported model
    bpy.context.object.name = "TheModel"
    #get the models size by bounding box
    SizeOf = bpy.context.object.dimensions
    #find bigest dimension of the model in any direction
    ScaleDenominator = max(SizeOf)
    
    #set scale factor (what fits nicely in the camera in blend units/largest dimension of the model
    ScaleFactor = 2.8/ScaleDenominator
    #If the model is pretty small scale it up.
    #Really I found that most models were well in eccess of the size of window
    #I set up. So most things need to be scaled down.
     
    if  ScaleFactor < 0.8: 
        bpy.ops.transform.resize(value =[ScaleFactor,ScaleFactor,ScaleFactor])
    
    #set the objects center at the center of it's geometry
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center ='BOUNDS')
    #set at the object at the global centerd
    bpy.ops.object.location_clear()
    
    ####Take and export photo######
    #Make the model camera the active camera
    ob = bpy.context.scene.objects["ModelCamera"]       
    bpy.context.scene.camera = ob
    #Set render size 
    bpy.context.scene.render.resolution_x = renderSize
    bpy.context.scene.render.resolution_y = renderSize
    #Set the filetype to PNG 
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    #set export location, gets most of it, cut of the original file type,
    #replace it with png
    bpy.context.scene.render.filepath = (os.path.join(startDir, inputPath,inputFile))[:-3] + "png"
    #add the image path to the image arraya
    imageArray.append((os.path.join(startDir, inputPath,inputFile))[:-3] + "png")
    bpy.ops.render.render(write_still = 1)
    #remove the object from the scene
    ob = bpy.context.scene.objects["TheModel"]       # Get the model
    bpy.ops.object.select_all(action='DESELECT') # Deselect all objects
    bpy.context.view_layer.objects.active = ob   # Make the model the active object
    ob.select_set(True)                          # Select the cube
    bpy.ops.object.delete()



#####Main######## 

#convert userstring to path type 
StartPath = Path(StartPath)
#set current directory to user path
os.chdir(StartPath)
for root, dirs, files in os.walk(".", topdown=False):
    for name in dirs: 
        if ".stl" in name or ".obj" in name.lower():
            print(os.path.join(root,name))
            Render(StartPath,root, name)
            #break #Debug
    for name in files: 
        if ".stl" in name or ".obj" in name.lower():
            print(os.path.join(root,name))
            Render(StartPath,root, name)
            #break #Debug
       
#DEBUG print(imageArray)

#delete this later 
tileNumber = len(imageArray)

#####Canvas setup for image quilt and quilting#####
#This should probably be it's own function
#Set canvas size
print("Preparing Canvas")
if tileNumber < 5:
    horizontalSize = tileNumber * renderSize
    verticalSize = renderSize
else:
    horizontalSize = 5 * renderSize
    #Roof the result without having to import math 
    roof = tileNumber%5
    if roof != 0:
        verticalSize= renderSize * int((tileNumber/5)+1)  
    else:
        verticalSize= renderSize * int(tileNumber/5)  


for x in imageArray:
    print("Image " + x + " loaded")
    x = Image.open(x)
#load the images at each colum
    
#incriment to next row after five images have been added
    print("Exporting Quilt")
#when done export image to user provided desinationgz
#create appropriately sized canvas
canvas = Image.new('RGB',(horizontalSize,verticalSize))

#Counters
xMod = 0
yMod = 0

#Paste Images into canvas
for x in imageArray:
    print("Image " + x + " loaded")
    img = Image.open(x)
    #calculate position to paste
    #default set to a 5 by y grid
    if xMod > 4:
        xMod = 0
        yMod += 1
        
    #print("x=" + str(xMod*renderSize) +"y=" +str(yMod*renderSize)) 
    canvas.paste(img,(xMod*renderSize,yMod*renderSize))
    #print(xMod)
    xMod +=1
    #print(os.path.join(StartPath).split("\\")[len(os.path.join(StartPath).split("\\"))-1])
    #print(StartPath)
    #save to the root directory as well as name the file
canvas.save(os.path.join(StartPath, os.path.join(StartPath).split("\\")[len(os.path.join(StartPath).split("\\"))-1] + "-Quilt.png"))