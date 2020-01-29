import arcpy

def deleteFeatureClasses(wildcard):
    for delItem in arcpy.ListFeatureClasses(wildcard):
        arcpy.AddMessage("Deleting feature class: " + delItem)
        arcpy.Delete_management(delItem)
        #arcpy.AddMessage(delItem)

    for delItem in arcpy.ListTables(wildcard):
        arcpy.AddMessage("Deleting table: " + delItem)
        arcpy.Delete_management(delItem)
        #arcpy.AddMessage(delItem)
        
ws = arcpy.GetParameterAsText(0)
arcpy.env.workspace = ws

wc = arcpy.GetParameterAsText(1)

deleteFeatureClasses(wc)