##-------------------------------------------------------------------------------
# Name:        TSMO_MakeCommandUnitLayers(NTC_v08).py
# Purpose:     Reads data from V_DF_ALL (NESTS points) and created ArcMap Layers
#              in ArcMap to be used for analysis or publishing to ArcGIS Server.
#
# Author:      chrism
#
# Created:     05/07/2017
# Copyright:   (c) chrism 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Import arcpy module
import arcpy, os
import unicodedata

def replaceSpecialCharacters(string):
    ch = ['!','@','#','$','%','^','&','*','(',')','<','>','/']
    for c in ch:
        string = str(string).replace(c,'_')

    return string

def countCharacters(word):
    return (len({i:word.count(i) for i in str(word)}) - 2) # minus 2 removes the two quotes.

def fetchLayerFile(layerName):
    layerFilePath = r'D:\DATA\Cmac\RF_Repeaters'
    bDist = layerName.split("(")[1][:2]
    template = 'template_' + bDist + 'mile.lyr'

    arcpy.AddMessage("(fetchLayerfile) using symbols from : " + command_list[command])
    file_layer = os.path.join(layerFilePath,template)

    return arcpy.mapping.Layer(file_layer)

def createTheLayer(lyrname, group_name):
    outputLayer = "tmp_%s" % (lyrname)

    arcpy.MakeFeatureLayer_management(lyr.dataSource.replace("%",""), outputLayer, expression)
    newLyr = arcpy.mapping.Layer(outputLayer)
    newLyr.visible = False
    newLyr.name = newLyr.name.replace("tmp_", "")

    arcpy.Delete_management(outputLayer)
    del outputLayer

    newLyr.definitionQuery = expression

    hasGroup = False
    for gr in arcpy.mapping.ListLayers(mxd,"* Repeater",df):
        if gr.name == group_name:
            grLayer = gr
            hasGroup = True

    if hasGroup:
        arcpy.mapping.AddLayerToGroup(df, grLayer, newLyr, "BOTTOM")
    else:
        arcpy.mapping.AddLayer(df, newLyr, "TOP")

    if isinstance(newLyr,arcpy._mapping.Layer):
        arcpy.mapping.UpdateLayer(df, newLyr, fetchLayerFile(lyrname))

# ########################################################
# BEGIN
lyr = arcpy.GetParameter(0)
desc = arcpy.Describe(lyr)
RFreq_field = arcpy.GetParameterAsText(1)
buffer_field = arcpy.GetParameterAsText(2)

global mxd
global df
global command
global unit
global lyr

arcpy.SelectLayerByAttribute_management(lyr,"CLEAR_SELECTION")
mxd = arcpy.mapping.MapDocument("CURRENT")
df = mxd.activeDataFrame

workspace = lyr.workspacePath
arcpy.env.workspace = workspace
scratch_workspace = r'D:\DATA\Cmac\RF_Repeaters\scratch.gdb'
arcpy.env.scratchWorkspace = scratch_workspace
arcpy.env.overwriteOutput = True

freqFields = [RFreq_field, buffer_field]
output = set()
unique_freqs = set()
layer_list = []

expression = '"%s" IS NOT NULL' % (RFreq_field)
cursor = arcpy.da.SearchCursor(lyr,freqFields,where_clause=expression)
for row in cursor:
    output.add("%s|%s" % (row[0],row[1]))
    unique_freqs.add("%s" % row[0])
del cursor

mylist = sorted(list(set(output)))
myRFlist = sorted(list(set(unique_freqs)))
for g in myRFlist:
    rf = round(float(g.split("|")[0]),3)
    group_name = str(rf) + " Repeater"
    if not arcpy.Exists(group_name):
        newGroupLayer = arcpy.mapping.Layer(r'C:\DATA\Cmac\AmateurRadio\RF_Repeaters\New Group Layer.lyr')
        newGroupLayer.name = group_name
        arcpy.mapping.AddLayer(df, newGroupLayer, "BOTTOM")


for l in mylist:

    arcpy.AddMessage(" %s" % (l))
    rf = round(float(l.split("|")[0]),3)
    group_name = str(rf) + " Repeater"
    buf = int(float(l.split("|")[1]))
    expression = '%s = %s AND %s = %s' %  (RFreq_field, rf, buffer_field, buf)     # "\"Command\" LIKE '%s' and \"Unit\" LIKE '%s'" % (command, unit)
    arcpy.AddMessage(" %s" % (expression))
    result = arcpy.SelectLayerByAttribute_management(lyr,"NEW_SELECTION",expression)

    if result.maxSeverity < 2:
        lyrname = "%s (%s mile)" % (rf, buf)

        layer_list.append(lyrname)
        createTheLayer(lyrname, group_name)

arcpy.RefreshTOC()



