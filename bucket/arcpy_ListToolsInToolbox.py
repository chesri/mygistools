import arcpy

tbx = arcpy.GetParameterAsText(0)
wildcard = arcpy.GetParameterAsText(1)

if wildcard != "*":
    arcpy.ImportToolbox(tbx)
else:
    arcpy.ImportToolbox(tbx)
    
thetools = arcpy.ListTools(wildcard)
for t in thetools:
    arcpy.AddMessage(t)

