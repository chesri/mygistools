#-------------------------------------------------------------------------------
# Name:        arcpy_AddMessage.py
# Purpose:     Used to push messages from python into Model Builder console.
#
# Author:      chrism
#
# Created:     08/07/2016
# Copyright:   (c) chrism 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy

string = arcpy.GetParameterAsText(0)
if string == '#' or not string:
    string = 'No String'

arcpy.AddMessage(string)