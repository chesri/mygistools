#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     12/09/2018
# Copyright:   (c) chrism 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os

scriptpath = os.path.dirname(__file__)
print __file__
print("Script Path: {}\n".format(scriptpath))

print(os.path.join(os.path.dirname(__file__),"srp_tif_transparency.lyr"))

##if os.path.isfile(os.path.join(arcpy.GetInstallInfo()['InstallDir'], 'Templates', 'ExportWebMapTemplates','A4 Landscape.mxd')):
##    mxd = arcpy.mapping.MapDocument(os.path.join(arcpy.GetInstallInfo()['InstallDir'], 'Templates', 'ExportWebMapTemplates','A4 Landscape.mxd'))
##    tif_file = r'C:\Workspace\Army_SRP_MIM\MIMLayout_to_Raster\MIM_500.tif'
##    tif_path = os.path.dirname(tif_file)
##    tif_fn = os.path.basename(tif_file).replace('.tif','')
##    arcpy.MakeRasterLayer_management(tif_file, tif_fn)
##    lyr = arcpy.mapping.Layer(tif_fn)
##
##    arcpy.SaveToLayerFile_management (lyr.name, tif_file.replace('.tif','.lyr'))