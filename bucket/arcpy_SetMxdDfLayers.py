import arcpy, os

mxd = arcpy.mapping.MapDocument("CURRENT")
df = mxd.activeDataFrame
layers = arcpy.mapping.ListLayers(mxd,"*",df)

webMXD = arcpy.mapping.MapDocument("CURRENT")
webDF = mxd.activeDataFrame
pLyrs = [prjlyr for prjlyr in arcpy.mapping.ListLayers(webMXD, 'Project*', webDF) if prjlyr.isFeatureLayer]

for pl in pLyrs:
    print("Name = {}".format(pl.name))
    print("datasetName = {}".format(pl.datasetName))
    print("dataSource = {}".format(pl.dataSource))
    print("isBroken = {}".format(pl.isBroken))
    print("workspacePath = {}\n".format(pl.workspacePath))
    print("supports \"DATASOURCE\" = {}\n".format(pl.supports("DATASOURCE")))

    if "projects" in pl.datasetName.split("."):
        print("Use {}   {}".format(pl.dataSource,pl.datasetName))


