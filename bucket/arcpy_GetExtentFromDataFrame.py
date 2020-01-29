#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     25/05/2018
# Copyright:   (c) chrism 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy, os

def createTempMaskFC(poly,sr):
    # setup variable for create feature class
    out_name = os.path.basename(arcpy.CreateScratchName("tmp_","","FeatureClass",arcpy.env.scratchWorkspace))
    geometry_type = 'POLYGON'
    template = ""
    has_m = "DISABLED"
    has_z = "DISABLED"
    spatial_reference = sr

    arcpy.CreateFeatureclass_management(arcpy.env.workspace, out_name, geometry_type, template, has_m, has_z, spatial_reference)
    fc = os.path.join(arcpy.env.workspace,out_name)

    cursor = arcpy.da.InsertCursor(fc,'SHAPE@')
    cursor.insertRow([poly])
    del cursor
    return fc

# ############################################################################
# Start
# ############################################################################

mxd = arcpy.mapping.MapDocument(r'D:\Workspace\Army_SRP_MIM\FTRILEYMIM\Copy_of_FINAL_FTRILEYMIM_50K_2010.mxd')
df_list = arcpy.mapping.ListDataFrames(mxd)
df = arcpy.mapping.ListDataFrames(mxd,'Map Layers')[0]

# setup workspace
arcpy.env.workspace = r'D:\Workspace\Army_SRP_MIM\SRP_MIM_neatlines.gdb'
ws = arcpy.env.workspace
sr = df.spatialReference

# create the polygon using coordinates from Data Frame
# THIS IS NOT WORKING SINCE DATA FRAME RETURNS maxumium x, min x, max y, min y - the envelope as a rectangle.
#
# you can replace these df.extent.___ with user input coordinates.
array = arcpy.Array([(df.extent.lowerLeft),
                 (df.extent.upperLeft),
                 (df.extent.upperRight),
                 (df.extent.lowerRight)])
poly = arcpy.Polygon([array])  # creates a polygon object - may be able to use it w/o a feature class

arcpy.env.mask = createTempMaskFC(poly,sr)
string = 'Created {} for mask polygon.'
arcpy.AddMessage(string)

