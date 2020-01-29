import arcpy, os

def checkSupports(lyrobj):
    supports_list = ['BRIGHTNESS', 'CONTRAST','DATASETNAME','DATASOURCE','DEFINITIONQUERY','DESCRIPTION','LABELCLASSES','LONGNAME','NAME','SERVICEPROPERTIES','SHOWLABELS','SYMBOLOGY','SYMBOLOGYTYPE','TIME','TRANSPARENCY','VISIBLE','WORKSPACEPATH']
    for sl in supports_list:
        if lyrobj.supports(sl):
            strings.append("\t{} supports {}".format(lyrobj.name,sl))


mxd = arcpy.mapping.MapDocument("CURRENT")
df = mxd.activeDataFrame
layers = arcpy.mapping.ListLayers(mxd,"*",df)
pLyrs = arcpy.mapping.ListLayers(mxd,"Project*",df)

strings = []

for pl in pLyrs:
    if pl.isFeatureLayer:
        strings.append("Name = {}".format(pl.name))
        strings.append("datasetName = {}".format(pl.datasetName))
        strings.append("dataSource = {}".format(pl.dataSource))
        strings.append("isBroken = {}".format(pl.isBroken))
        strings.append("workspacePath = {}\n".format(pl.workspacePath))
        #checkSupports(pl)

    elif pl.isGroupLayer:
        strings.append("Group Layer Name = {}\n".format(pl.name))

for s in strings:
    print(s)
    arcpy.AddMessage(s)