#-------------------------------------------------------------------------------
# Name:        importXY2Point
# Purpose:
#
# Author:      chrism
#
# Created:     15/06/2018
# Copyright:   (c) chrism 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy, os

def PrintException(self):
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    string = 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)
    print string

    exit()

def getFieldInfo(fld,flds):
    for f in flds:
        if fld.name.upper() == f.name.upper():
            return f.length,str(f.type)
    return -1

def fetchFieldNamesAsText(table):
    fList = []
    fields = arcpy.ListFields(table)
    for field in fields:
        if field.type <> 'Geometry': #Skip Geometry/Shape fields
            fList.append(str(field.name))

    return fList


# #############################################################################
#
source_table = r'D:\DATA\AGS_Shared\MCI_IRDM.gdb\StatisticsInstallation'
source_fields = arcpy.ListFields(source_table)

coord_x_fld = 'WGS84_X'
coord_y_fld = 'WGS84_Y'
arcpy.env.overwriteOutput = True

output_fc = r'D:\DATA\AGS_Shared\MCI_IRDM.gdb\StatsInst_Points'



# Use SearchCursor to read and copy source data into a python list
sourceFieldNames = fetchFieldNamesAsText(source_table)
sourceFieldNames = ['ACTIVITY_UIC', 'Year', 'FREQUENCY', 'SUM_AREA', 'SUM_PlannedCalculatedCost', 'SUM_BudgetedProgrammedCost', 'OBJECTID_1', 'inst_name', 'inst_reg_d', 'Mainside', 'InstCode', 'Activity_UIC_1', 'WGS84_X', 'WGS84_Y']
print sourceFieldNames
data = []
expression = '(%s IS NOT NULL AND %s <> 0) AND (%s IS NOT NULL AND %s <> 0)' % (coord_x_fld,coord_x_fld,coord_y_fld,coord_y_fld)
cursor = arcpy.da.SearchCursor(source_table,sourceFieldNames,where_clause=expression)
for row in cursor:
    string = (row)
    data.append(string)
del cursor



# Prepare output feature class (to receive inputcursor writes)

ws = os.path.dirname(output_fc)
fc = os.path.basename(output_fc)
sr = arcpy.SpatialReference(3857)

if arcpy.Exists(output_fc):
    arcpy.Delete_management(output_fc)

arcpy.CreateFeatureclass_management(ws,fc,"POINT","","DISABLED","DISABLED",sr,)

for field in source_fields:
    ## AddField_management (in_table, field_name, field_type, {field_precision}, {field_scale}, {field_length}, {field_alias}, {field_is_nullable}, {field_is_required}, {field_domain})
    #print("testing {}".format(field.name))
    if field.name != 'OBJECTID':
        #print("adding field: {}".format(field.name))
        arcpy.AddField_management(output_fc, field.name, field.type,field.precision,field.scale,field.length,field.aliasName,field.isNullable,field.required,field.domain)

opf = arcpy.ListFields(output_fc)
field_names = fetchFieldNamesAsText(output_fc)
field_names = sourceFieldNames
field_names.append("SHAPE@XY")
print field_names
x_index = field_names.index(coord_x_fld)
y_index = field_names.index(coord_y_fld)
s_index = field_names.index("SHAPE@XY")


cursor = arcpy.InsertCursor(output_fc,field_names)
for d in data:
    row_values = []
    row = cursor.newRow()
    for c in range(0,len(field_names)-1):
        if opf[c+2].type == 'String':
##            tval = field_names[c] + ',' + str(d[c])
##            row.setValue(tval)
            row_values.append(str(d[c]))
        else:
##            tval = field_names[c] + ',' + d[c]
##            row.setValue(tval)
            row_values.append(d[c])

    # ...and adding XY tuple at end for "SHAPE@XY"
    xy = arcpy.Point(d[x_index],d[y_index])
    ##xy= (d[x_index],d[y_index])
    ##row.setValue("SHAPE@XY",xy)
    row_values.append(xy)
    print row_values

    try:
        cursor.insertRow(row_values)

    except arcpy.ExecuteError:
        for m in range(0,5):
            arcpy.AddError(arcpy.GetMessage(m))
        del cursor
        PrintException()

del cursor