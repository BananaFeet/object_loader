import os
#import maya.cmds as cmds
'''Loads blender files and exports out maya files
to be used in Blender or another 3d software'''

def get_maya_file_location(user_name):
    '''gets file path of object to import'''
    first = "C:/Users/"
    last = "/Documents"
    result = first + user_name + last
    #print(result)
    return result

def maya_load():
    '''Loads obj files into Maya'''
    #main_path = " "
    pass



def maya_export():
    '''Saves and exports as an obj.'''
    pass


