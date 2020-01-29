#-------------------------------------------------------------------------------
# Name:        arcpy_ReturnMGRS
# Purpose:
#
# Author:      chrism
#
# Created:     31/01/2017
# Copyright:   (c) chrism 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def createPointFC(input_X, input_Y, sr):

    return searchFC

# =============================== BEGIN =========================================
##arcpy.env.workspace = "Database Connections\\DPAAW as sde on dpaa-db.esri.com.sde"
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd)[0]

#0 & #1 - XY Location
##search_X = arcpy.GetParameter(0)
##search_Y = arcpy.GetParameter(1)
search_X = 108.770777
search_Y = 12.155829
input_MGRS = '49P BP 57412 44779'
arcpy.env.overwriteOutput = True

runInMemory = arcpy.GetParameter(5)

if search_X and search_Y and not input_MGRS:

    # Process: Make a table with input coordinates.
    ##  CreateTable_management (out_path, out_name, {template}, {config_keyword})
    if runInMemory:
        tbl = arcpy.CreateTable_management("in_memory", "tmp_XY_in")
    else:
        tbl = arcpy.CreateTable_management(arcpy.env.scratchWorkspace, "tmp_XY_in")

    arcpy.AddField_management(tbl,"Coord_X", "DOUBLE")
    arcpy.AddField_management(tbl,"Coord_Y", "DOUBLE")

    ### Populate data in new feature class
    searchPt_cursor = arcpy.da.InsertCursor(tbl, ['Coord_X', 'Coord_Y'])
    row_to_insert = [search_X, search_Y]
    searchPt_cursor.insertRow(row_to_insert)
    del searchPt_cursor

    ##  ConvertCoordinateNotation_management (in_table, out_featureclass, x_field, y_field, input_coordinate_format, output_coordinate_format, {id_field}, {spatial_reference}, {in_coor_system}, {exclude_invalid_records})
    if runInMemory:
        out_Featureclass = "in_memory\\outputMGRS"
    else:
        out_Featureclass = "outputMGRS"

    arcpy.ConvertCoordinateNotation_management(tbl,out_Featureclass, "Coord_X", "Coord_Y", "DD_2", "MGRS")
    lyr = arcpy.MakeFeatureLayer_management(out_Featureclass, "output_MGRS").getOutput(0)
    searchPt_cursor = arcpy.da.SearchCursor(out_Featureclass, ['Coord_X', 'Coord_Y',"MGRS"])

    arcpy.mapping.AddLayer(df, lyr, "TOP")

    for row in searchPt_cursor:
        arcpy.AddMessage("MGRS: " + row[2])
    del searchPt_cursor

else:

    # Process: Make a table with input coordinates.
    ##  CreateTable_management (out_path, out_name, {template}, {config_keyword})
    if runInMemory:
        tbl = arcpy.CreateTable_management("in_memory", "tmp_XY_in")
    else:
        tbl = arcpy.CreateTable_management(arcpy.env.scratchWorkspace, "tmp_XY_in")

    arcpy.AddField_management(tbl,"MGRS", "TEXT")

    ### Populate data in new feature class
    searchPt_cursor = arcpy.da.InsertCursor(tbl, ['MGRS'])
    row_to_insert = [input_MGRS]
    searchPt_cursor.insertRow(row_to_insert)
    del searchPt_cursor

    if runInMemory:
        out_Featureclass = "in_memory\\outputXY"
    else:
        out_Featureclass = "outputXY"

    ##  ConvertCoordinateNotation_management (in_table, out_featureclass, x_field, y_field, input_coordinate_format, output_coordinate_format, {id_field}, {spatial_reference}, {in_coor_system}, {exclude_invalid_records})
    arcpy.ConvertCoordinateNotation_management(tbl,out_Featureclass, "MGRS", "MGRS", "MGRS", "DD_2")

    lyr = arcpy.MakeFeatureLayer_management(out_Featureclass, "output_XY").getOutput(0)
    arcpy.mapping.AddLayer(df, lyr, "TOP")

    searchPt_cursor = arcpy.da.SearchCursor(out_Featureclass, ['DDLat', 'DDLon',"MGRS"])
    for row in searchPt_cursor:
        arcpy.AddMessage("Coordinates: " + str(row[1]) + ", " +str(row[0]) + " DD")
    del searchPt_cursor