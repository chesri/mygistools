#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     26/04/2019
# Copyright:   (c) chrism 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy

dc = arcpy.GetParameterAsText(0)
ws = arcpy.GetParameterAsText(1)

arcpy.env.workspace = ws
desc = arcpy.Describe('projects')

string = ws + ';Describe returns: ' + desc.catalogPath

arcpy.SetParameterAsText(2,string)
arcpy.SetParameterAsText(3,ws)
arcpy.SetParameterAsText(4,dc)