import bpy
from random import random, seed
from datetime import datetime
import os
from time import time

try:
    files = os.listdir('/tmp/mask')
    if len(files) <= 1:
        print('No files')
    files.sort()
    offset = int(files[-1].replace('mask', '').replace('.png', ''))
    print(offset)
except:
    offset = 0
    print('No files')
    

seed(int(datetime.now().timestamp()))

bpy.context.scene.use_nodes = True
tree = bpy.context.scene.node_tree

# Set render engine to Cycles
bpy.context.scene.render.engine = 'CYCLES'

# Set device to GPU
cpref = bpy.context.preferences.addons['cycles'].preferences
cpref.compute_device_type = 'CUDA'

# Enable all available GPU devices
for device in cpref.devices:
    device.use = True if device.type == 'CUDA' else False

start = time()
start_time = datetime.now()
print(start_time)
print(10000)
for i in range(10):
    _start = time()
    #new x location
    bpy.data.objects[3].location.x = -0.8+(1.6*random())
    
    #new y location
    bpy.data.objects[3].location.y = -0.8+(1.6*random())
    
    #new y rotation
    bpy.data.objects[3].rotation_euler.y = 3.141592*2*random()
    
    #new y rotation
    bpy.data.objects[3].rotation_euler.z = 3.141592*2*random()
    
    bpy.context.scene.frame_set(i+offset+1)

    bpy.ops.render.render()
    print(i, time() - _start, time() - start)
    
print(time() - start)
print(start_time)
print(datetime.now())
