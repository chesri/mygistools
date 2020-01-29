#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     01/04/2019
# Copyright:   (c) chrism 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy, os
import datetime

the_input = arcpy.GetParameterAsText(0)
dbc = arcpy.GetParameterAsText(1)
arcpy.env.workspace = dbc

if arcpy.Exists(os.path.join(dbc,'projects')):
    project_exists = True

now = datetime.datetime.now()
nd = now.strftime('%m/%d/%Y %H:%M:%S')

output = 'You entered "{}" at {}'.format(the_input,nd)
arcpy.AddMessage(output)
arcpy.SetParameterAsText(2, output)