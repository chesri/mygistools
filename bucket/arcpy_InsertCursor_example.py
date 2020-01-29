#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      chrism
#
# Created:     20/06/2018
# Copyright:   (c) chrism 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

coord_table = "in_memory\\cctable"
coord_table = os.path.join(r'D:\Workspace\Army_SRP_MIM\FTRILEYMIM\scripting\scratch.gdb',os.path.basename(output).split(".")[0])
arcpy.CreateTable_management(os.path.dirname(coord_table), os.path.basename(coord_table))
arcpy.AddField_management(coord_table, 'coord_x',"Double",0,0,8,"longitude","NULLABLE","NON_REQUIRED","")
arcpy.AddField_management(coord_table, 'coord_y',"Double",0,0,8,"latitude","NULLABLE","NON_REQUIRED","")
cursor = arcpy.InsertCursor(coord_table,['coord_x','coord_y'])
for c in (UL,LL,LR,UR):
    row = cursor.newRow()
    row.setValue('coord_x',c[0])
    row.setValue('coord_y',c[1])
    cursor.insertRow(row)