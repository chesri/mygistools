import arcpy, os

# Search path (for MXDs)
folderPath = r"C:\OneDrive - Esri\Temp\Yuma_Temp"

# Target GDB - to replace current GDB path with this one.
newPath = r"C:\arcgisserver_mycustoms\clt-demo-db-Yuma19-sde.sde"

# Loop through all MXDs in the specified folder and change the layer's data source to the new path
for filename in os.listdir(folderPath):
    fullpath = os.path.join(folderPath, filename)
    if os.path.isfile(fullpath):
        basename, extension = os.path.splitext(fullpath)
        if extension.lower() == ".mxd":
            mxd = arcpy.mapping.MapDocument(fullpath)
            mxd.replaceWorkspaces ('', '', newPath, "SDE_WORKSPACE", False)
            mxd.saveACopy(os.path.join(folderPath,'copy.mxd'))

##for fileName in os.listdir(folderPath):
##    fullPath = os.path.join(folderPath, fileName)
##    if os.path.isfile(fullPath):
##        basename, extension = os.path.splitext(fullPath)
##        if extension == ".mxd":
##            mxd = arcpy.mapping.MapDocument(fullPath)
##            print "MXD: " + fileName
##            brknList = arcpy.mapping.ListBrokenDataSources(mxd)
##            for brknItem in brknList:
##                print "\t" + brknItem.name
print "done"


