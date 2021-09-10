import bpy
from random import random
from math import pi, sin ,cos

def randomizeLid():
    col = bpy.data.collections["Top"]

    theta = ((random() * (110 - -52)) - 52) * 2 * pi / 360

    for obj in col.objects.values():
        obj.rotation_euler.x = theta
        obj.rotation_euler.y = 0
        obj.rotation_euler.z = 0
    
def randomizeCamera():
    theta = random() * pi
    phi = random() * pi * 2
    
    r = 0.8
    p_x = r * cos(theta) * sin(phi)
    p_y = r * cos(theta) * cos(phi)
    p_z = r * sin(theta)

    r_x = - pi / 2 + theta
    r_y = 0
    r_z = phi
    
    camera = bpy.data.objects['Camera']

    camera.location.x = p_x
    camera.location.y = p_y
    camera.location.z = p_z

    camera.rotation_euler.x = r_x
    camera.rotation_euler.y = -r_y
    camera.rotation_euler.z = -r_z
    
randomizeLid()
randomizeCamera()
scene = bpy.context.scene
scene.render.image_settings.file_format='PNG'
scene.render.filepath='/Users/will/projects/blender_gen/object_detection/macbook_random.png'
bpy.ops.render.render(write_still=1)

