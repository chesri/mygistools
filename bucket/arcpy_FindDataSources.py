#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     05/06/2017
# Copyright:   (c) chrism 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy, os, string

def getFieldName(mxd_source, layer, field_wildcard):

    dsource = str(layer.dataSource)
    fnd = dsource.find('.sde')
    sub_str = dsource[:fnd +4]
    desc = arcpy.Describe(sub_str)
    cp = desc.connectionProperties
    dbms = cp.instance[cp.instance.find('sde')+4:7]

    if dbms == 'sql':
        ilAREAOID = "%s.AREAOID" % (str(in_layer.datasetName))
        natta, ilDB, ilFC, ilFld = arcpy.ParseFieldName(ilAREAOID).split(", ")
        in_layer_AREAOID = "%s.%s.%s.%s" % (natta,ilDB,ilFC,ilFld)
    elif dbms == 'ora':
        pass
    else:
        pass

    return dbms


def FindConnPropTbl(mxd_source):
    mxd = arcpy.mapping.MapDocument(mxd_source)
    for df in arcpy.mapping.ListDataFrames(mxd):
        tableList = arcpy.mapping.ListTableViews(mxd, "", df)
        for table in tableList:
            dsource = str(table.dataSource)
            fnd = dsource.find('.sde')
            sub_str = dsource[:fnd +4]
            desc = arcpy.Describe(sub_str)
            cp = desc.connectionProperties
            try:
                string =  "Table:{0},Server: {1}".format(table.name,cp.server)
            except:
                string =  "No server listed for table: {0}".format(table.name)
            arcpy.AddMessage(string)
            try:
                string =  "Table:{0},Database: {1}".format(table.name,cp.database)
            except:
                string =  "No database listed for table: {0}".format(table.name)
            arcpy.AddMessage(string)
            del table,dsource,fnd,cp,sub_str,desc
    del mxd,df,tableList

def FindConnPropFc(mxd_source):
    mxd = arcpy.mapping.MapDocument(mxd_source)
    for df in arcpy.mapping.ListDataFrames(mxd):
        layerList = arcpy.mapping.ListLayers(mxd, "", df)
        for layer in layerList:
            dsource = str(layer.dataSource)
            fnd = dsource.find('.sde')
            sub_str = dsource[:fnd +4]
            desc = arcpy.Describe(sub_str)
            cp = desc.connectionProperties
            dbms = cp.instance[cp.instance.find('sde')+4:7]
            #dbms = cp.instance
##            try:
##                string = "Layer:{0},Server: {1}".format(layer.name,cp.server)
##            except:
##                string =  "No server listed for layer: {0}".format(layer.name)
##            arcpy.AddMessage(string)
            try:
                string =  "Layer:{0},DBMS: {1}".format(layer.name,dbms)
            except:
                string =  "No database listed for layer {0}".format(layer.name)
            arcpy.AddMessage(string)
            del layer,dsource,fnd,cp,sub_str,desc
    del mxd,df,layerList

if __name__=="__main__":
    mxd = arcpy.mapping.MapDocument("CURRENT")
    mxd_source = mxd.filePath
    #FindConnPropTbl(mxd_source)
    FindConnPropFc(mxd_source)
