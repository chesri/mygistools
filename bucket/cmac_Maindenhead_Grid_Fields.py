import os
import arcpy

def sendMessage(message, indent=0):

    if indent == 0:
        string = message
    if indent > 0 :
        string = "{} {}".format(" " * indent,message)

    arcpy.AddMessage(string)
    print(string)

def getFieldInfo(fld,flds):
    for f in flds:
        if fld.upper() == f.name.upper():
            return f.length,str(f.type)
    return -1

def fieldExists(tbl,field):
    if arcpy.Exists(tbl):
        for f in arcpy.ListFields(tbl):
            if field == f.name:
                return True

    return False


def checkCoords(x_coord,y_coord):
    findex=0
    for i in range(-180,180,20):
        if x_coord >= i and x_coord < (i + 20):
            field1 = 'ABCDEFGHIJKLMNOPQR'[findex]

            sindex = 0
            for s in range(i,i + 20,2):
                if x_coord > s:
                    square1 = '0123456789'[sindex]
                sindex = sindex + 1
        findex = findex + 1

    findex=0
    for i in range(-90,90,10):
        if y_coord >= i and y_coord < (i + 10):
            field2 = 'ABCDEFGHIJKLMNOPQR'[findex]
            sindex = 0
            for s in range(i,i + 10,1):
                if y_coord > s:
                    square2 = '0123456789'[sindex]
                sindex = sindex + 1

        findex = findex + 1

    grid = field1 + field2 + square1 + square2
    return grid


fc = r'D:\Workspace\Maidenhead_Grid\scratch.gdb\fn03'
#
# Create the Fishnet
if not arcpy.Exists(fc):
    arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)
    arcpy.CreateFishnet_management(fc, origin_coord="-180 -90", y_axis_coord="-180 90", cell_width="", cell_height="", number_rows="4320", number_columns="4320", corner_coord="180 90", labels="NO_LABELS", template="DEFAULT", geometry_type="POLYGON")
    #arcpy.DefineProjection_management(fc, '3395')

if not fieldExists(fc,'grid_field'):
    arcpy.AddField_management(fc, "grid_field","TEXT",0,0,2,"Field","NULLABLE","NON_REQUIRED","")
if not fieldExists(fc,'grid_squares'):
    arcpy.AddField_management(fc, "grid_squares","TEXT",0,0,2,"Square","NULLABLE","NON_REQUIRED","")
if not fieldExists(fc,'grid_subsquares'):
    arcpy.AddField_management(fc, "grid_subsquares","TEXT",0,0,2,"Subsquare","NULLABLE","NON_REQUIRED","")

desc = arcpy.Describe(fc)
oid = desc.OIDFieldName
fields = ['OID@','SHAPE@XY','grid_field','grid_squares','grid_subsquares']

# For each row print the WELL_ID and WELL_TYPE fields, and the
# the feature's x,y coordinates
with arcpy.da.UpdateCursor(fc, fields) as cursor:
    for row in cursor:
        oid = row[0]
        grid = checkCoords(row[1][0],row[1][1])
        print('{}: ({},{}) {}'.format(oid,row[1][0],row[1][1],grid))
        row[2] = grid[:2]
        row[3] = grid[2:]
        cursor.updateRow(row)

del cursor