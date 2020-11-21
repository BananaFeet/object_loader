import os

'''Loads maya files and exports out maya files
to be used in Blender or another 3d software'''

def get_blend_file_location(user_name):
    '''gets file path of object to import'''
    first = "C:/Users/"
    last = "/Documents"
    result = first + user_name + last
    return result

def blender_load():
    '''Loads obj files into Maya'''
    pass

def blender_export():
    '''Saves and exports as an obj.'''
    pass


