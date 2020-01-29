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

arcpy.env.overwriteOutput = True

# Process: Make a table with input coordinates.
##  CreateTable_management (out_path, out_name, {template}, {config_keyword})
tbl = arcpy.CreateTable_management("in_memory", "tmp_XY_in")
arcpy.AddField_management(tbl,"Coord_X", "DOUBLE")
arcpy.AddField_management(tbl,"Coord_Y", "DOUBLE")

### Populate data in new feature class
searchPt_cursor = arcpy.da.InsertCursor(tbl, ['Coord_X', 'Coord_Y'])
row_to_insert = [search_X, search_Y]
searchPt_cursor.insertRow(row_to_insert)
del searchPt_cursor


##  ConvertCoordinateNotation_management (in_table, out_featureclass, x_field, y_field, input_coordinate_format, output_coordinate_format, {id_field}, {spatial_reference}, {in_coor_system}, {exclude_invalid_records})
arcpy.ConvertCoordinateNotation_management(tbl,"output_MGRS", "Coord_X", "Coord_Y", "DD_2", "MGRS")

lyr = arcpy.MakeFeatureLayer_management("output_MGRS", "output_MGRS").getOutput(0)
arcpy.mapping.AddLayer(df, lyr, "TOP")












### Process: Make Feature Layer out of the search point
####CreateFeatureclass_management (out_path, out_name, {geometry_type}, {template}, {has_m}, {has_z}, {spatial_reference}, {config_keyword}, {spatial_grid_1}, {spatial_grid_2}, {spatial_grid_3})
##searchFC = arcpy.CreateFeatureclass_management(arcpy.env.scratchWorkspace, 'tmp_search_point', 'POINT',"","","",df.spatialReference)
###Add Fields
####  AddField_management (in_table, field_name, field_type, {field_precision}, {field_scale}, {field_length}, {field_alias}, {field_is_nullable}, {field_is_required}, {field_domain})
#### http://pro.arcgis.com/en/pro-app/tool-reference/data-management/add-field.htm
##arcpy.AddField_management(searchFC,"MGRS", "TEXT", "", "", 20)
### Populate data in new feature class
##searchPt_cursor = arcpy.da.InsertCursor(searchFC, ['SHAPE@XY', 'MGRS'])
##row_to_insert = [(search_X, search_Y), '49P BP 57412 44779']
##searchPt_cursor.insertRow(row_to_insert)
### Add Layer to Map
##lyr = arcpy.MakeFeatureLayer_management(searchFC, "search_origin").getOutput(0)
##arcpy.mapping.AddLayer(df, lyr, "TOP")