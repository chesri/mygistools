##-------------------------------------------------------------------------------
# Name:        Intersect Analysis.py
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
    ch = [' ','!','.','@','#','$','%','^','&','*','(',')','<','>','/']
    for c in ch:
        string = str(string).replace(c,'_')
    return string

# ########################################################
# BEGIN
buffers = r'D:\DATA\Cmac\RF_Repeaters\AmateurRadio_points.gdb\NCSC_2m_repeater_BUFERS'
arcpy.MakeFeatureLayer_management(buffers, "layer")

workspace = r'D:\DATA\Cmac\RF_Repeaters\AmateurRadio_points.gdb'
arcpy.env.workspace = workspace
scratch_workspace = r'D:\DATA\Cmac\RF_Repeaters\scratch.gdb'
arcpy.env.scratchWorkspace = scratch_workspace
arcpy.env.overwriteOutput = True

# Set local variables
out_path = workspace
out_name = "freq_conflicts"
geometry_type = "POLYGON"
template = buffers
has_m = "DISABLED"
has_z = "DISABLED"

# Use Describe to get a SpatialReference object
spatial_reference = arcpy.Describe(buffers).spatialReference

# Execute CreateFeatureclass
if not arcpy.Exists(out_name):
    arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template, has_m, has_z, spatial_reference)
arcpy.TruncateTable_management(os.path.join(out_path,out_name))
arcpy.MakeFeatureLayer_management(out_name, "output")


freqFields = ["Output_Freq"]
rf_list = set()

expression = '"%s" IS NOT NULL' % (freqFields[0])
cursor = arcpy.da.SearchCursor(buffers,freqFields,where_clause=expression)
for row in cursor:
    rf_list.add(row[0])
del cursor

myRFlist = sorted(list(set(rf_list)))
for f in myRFlist:
    for dis in range(10,81,10):
        expression = '"{}" = {:f} AND "{}" = {:d}'.format(freqFields[0],f,"distance",dis)
        print expression
        arcpy.SelectLayerByAttribute_management("layer","NEW_SELECTION",expression)
        count = arcpy.GetCount_management("layer")
        print "   Selected: " + str(count)
        output = os.path.join(scratch_workspace,"tmp_" + replaceSpecialCharacters(str(f)))
        arcpy.Intersect_analysis(["layer"],output)
        if int(arcpy.GetCount_management(output).getOutput(0)) > 0:
            arcpy.Append_management(output,"output","NO_TEST")
        arcpy.Delete_management(output)
        del output