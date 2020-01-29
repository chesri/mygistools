import arcpy, os, sys

def sendMessage(message):
    print(message)
    arcpy.AddMessage(message)

def interrogateLyr(lyr):

        sendMessage("Layer Name: %s" % (lyr.datasetName))

        lyrType = "Unknown"
        if lyr.isFeatureLayer:
            lyrType = "Feature Layer"
        if lyr.isGroupLayer:
            lyrType = "Group Layer"
        if lyr.isNetworkAnalystLayer:
            lyrType = "NetworkAnalystLayer"
        if lyr.isServiceLayer:
            lyrType = "Service Layer"
        sendMessage("  Layer Type: %s" % (lyrType))
        if len(lyr.description) > 0:
            sendMessage("  Description: %s"  % (lyr.description))
        if lyr.supports("DATASOURCE"):
            sendMessage("  Data Source: %s" % (lyr.dataSource))
        if len(lyr.definitionQuery) > 0:
            sendMessage("  Definition Query: %s" % (lyr.definitionQuery))

if __name__ == '__main__':

    as_Layer = arcpy.GetParameter(0)
    as_LayerText = arcpy.GetParameterAsText(1)
    as_String = arcpy.GetParameter(2)
    as_StringText = arcpy.GetParameterAsText(3)

    interrogateLyr(as_Layer)
    #interrogateLyr(as_LayerText)
    #interrogateLyr(as_String)
    #interrogateLyr(as_StringText)



##    # replaceDataSource (workspace_path, workspace_type, {dataset_name}, {validate})
##    # lyr.findAndReplaceWorkspacePath
##    #lyr.replaceDataSource(r'C:\DATA\Todd\scratch.gdb',"FILEGDB_WORKSPACE",lyr.datasetName,False)
##    ##    <bound method Layer.findAndReplaceWorkspacePath of <map layer u'points_of_interest'>>
##    #lyr.getExtent
##    ##    <bound method Layer.getExtent of <map layer u'points_of_interest'>>
##    #lyr.getExtent.im_self
##    ##    <map layer u'points_of_interest'>
##    #lyr.getSelectedExtent
##    ##    <bound method Layer.getSelectedExtent of <map layer u'points_of_interest'>>
##    #lyr.getSelectionSet
##    ##    <bound method Layer.getSelectionSet of <map layer u'points_of_interest'>>
##    lyr.isBroken
##    ##    False
##    lyr.isFeatureLayer
##    ##    True
##    lyr.isGroupLayer
##    ##    False
##    lyr.isNetworkAnalystLayer
##    ##    False
##    lyr.isServiceLayer
##    ##    False
##    lyr.labelClasses
##    ##    [<LabelClass object at 0x16d17c70[0x165911e8]>]
##    lyr.longName
##    ##    u'points_of_interest'
##    lyr.maxScale
##    ##    0.0
##    lyr.name
##    ##    u'points_of_interest'
##    lyr.save
##    ##    <bound method Layer.save of <map layer u'points_of_interest'>>
##    #lyr.save()
##    lyr.time
##    ##    <LayerTime object at 0x19609ab0[0x15f264d0]>
#mxd.saveACopy(r'C:\Users\Cmac\Desktop\Test2.mxd')

