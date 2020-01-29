#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     27/04/2016
# Copyright:   (c) chrism 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Set Map Document
mxd = arcpy.mapping.MapDocument("CURRENT")

# Set Data Frame
adf = mxd.activeDataFrame
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]

# Set Layer to be Updated
lyr = arcpy.mapping.ListLayers(mxd,"1-6 IN...D CO",adf)[0]
updateLayer = arcpy.mapping.ListLayers(mxd, "1-6 IN...D CO", df)[0]

# Set Source Layer to use
lyrFile = r'D:\Workspace\TSMO\Layers\1-6 IN.lyr'
sourceLayer = arcpy.mapping.Layer(r'D:\Workspace\TSMO\Layers\1-6 IN.lyr')

#arcpy.mapping.UpdateLayer(adf,lyr,lyrFile,False)

arcpy.mapping.UpdateLayer(df, updateLayer, sourceLayer, False)

arcpy.RefreshTOC()
arcpy.RefreshActiveView()