# randomise camera position

from random import random
from math import pi, sin, cos
import bpy

def randomizeCamera():
    theta = random() * pi * 2
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

scene = bpy.context.scene
scene.render.image_settings.file_format='PNG'
for i in range(1, 4):
    randomizeCamera()
    scene.render.filepath='/Users/will/projects/blender_gen/kettle/kettle_' + str(i) + '.png'
    bpy.ops.render.render(write_still=1)
