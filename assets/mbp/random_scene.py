import bpy
from random import random, choice
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
    
def randomizeScreenshot():
    screen = bpy.data.objects["Screen"]
    
    mat = bpy.data.materials.new(name="New_Mat")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    texImage = mat.node_tree.nodes.new('ShaderNodeTexImage')
    
    screen_bg_paths = Path("/Users/will/projects/blender_gen/data/raw/screen_bg/")
    screen_bg_paths = [x for x in screen_bg_paths.iterdir()]
    random_bg = str(choice(screen_bg_paths))
    texImage.image = bpy.data.images.load(random_bg)
    
    mat.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])
    screen.data.materials[-1] = mat

randomizeLid()
randomizeCamera()
randomizeScreenshot()
