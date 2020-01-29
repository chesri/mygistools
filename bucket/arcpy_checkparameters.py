#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     12/12/2019
# Copyright:   (c) chrism 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy

p0 = arcpy.GetParameterAsText(0)
result = []
result.append(str(p0))
arcpy.AddMessage("Parameter 0 returned: {}".format(p0))
p0count = arcpy.GetCount_management(p0)

result.append(str(p0count))
rows = [row[0] for row in arcpy.da.SearchCursor(p0,"project_uid")]
result.append(rows)

arcpy.SetParameterAsText(1,result)


