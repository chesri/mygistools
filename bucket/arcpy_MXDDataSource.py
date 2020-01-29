#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     23/11/2016
# Copyright:   (c) chrism 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy, os


mxd = arcpy.mapping.MapDocument(r'C:\OneDrive - Esri\Temp\Yuma_Temp\basedemo_ls_8x11.mxd')

## replaceWorkspaces (old_workspace_path, old_workspace_type, new_workspace_path, new_workspace_type, {validate})
for layer in arcpy.mapping.ListLayers(mxd):
    print(layer.name)
##mxd.replaceWorkspaces