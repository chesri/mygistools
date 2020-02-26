#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     10/02/2020
# Copyright:   (c) chrism 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy

def listAllFeatureClasses(ws):
    arcpy.env.workspace = ws
    if arcpy.Describe(ws).workspaceType == 'RemoteDatabase':
        return [fc.split('.')[2] for ds in arcpy.ListDatasets() for fc in arcpy.ListFeatureClasses("*","ALL",ds)]
    else:
        return [fc for ds in arcpy.ListDatasets() for fc in arcpy.ListFeatureClasses("*","ALL",ds)]

myList = listAllFeatureClasses(r'C:\Users\chrism\AppData\Roaming\Esri\Desktop10.6\ArcCatalog\clt-cmcguire10l-MCIEAST-OSA.sde')

for fc in myList:
    print(fc)
