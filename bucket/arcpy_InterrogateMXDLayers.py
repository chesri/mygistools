import arcpy, os, sys

def sendMessage(message):
    print(message)
    arcpy.AddMessage(message)

def interrogateMXD(the_mxd):
    if not arcpy.Exists(the_mxd):
        print("File %s does not exists." % (the_mxd))
        return

    mxd = arcpy.mapping.MapDocument(the_mxd)
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    sendMessage("Processing: %s" % (mxd.filePath))
    layers = arcpy.mapping.ListLayers(mxd)

    for lyr in layers:
        sendMessage("Layer Name: %s" % (lyr.name))

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

def breakDataSourcePaths(the_mxd, output):
    mxd = arcpy.mapping.MapDocument(the_mxd)
    sendMessage("Breaking paths for %s" % (mxd.filePath))
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    layers = arcpy.mapping.ListLayers(mxd)

    for lyr in layers:
        #sendMessage("Layer Name: %s" % (lyr.datasetName))
        if lyr.supports("DATASOURCE"):
            lyr.replaceDataSource(r'\no_path',"FILEGDB_WORKSPACE",lyr.datasetName,False)

    sendMessage("Saving as %s " % (output))
    mxd.saveACopy(output)
    return output

if __name__ == '__main__':
    if len(sys.argv) == 3:
        mxd_file = sys.argv[1]
        breakPaths = sys.argv[2]
        copy_name = sys.argv[3]
        if copy_name == "#" or not copy_name:
            copy_name = mxd_file.split(".mxd")[0] + "_BrokenPaths.mxd"
            sendMessage("New name: %s " % (copy_name))
    else:
        mxd_file = arcpy.GetParameterAsText(0)
        breakPaths = arcpy.GetParameter(1)
        copy_name = arcpy.GetParameterAsText(2)
        if copy_name == "#" or not copy_name:
            copy_name = mxd_file.split(".mxd")[0] + "_BrokenPaths.mxd"
            sendMessage("New name: %s " % (copy_name))

    interrogateMXD(mxd_file)

    if breakPaths:
        interrogateMXD(breakDataSourcePaths(mxd_file, copy_name))


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

