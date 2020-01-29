#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     01/12/2017
# Copyright:   (c) chrism 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os,datetime,arcpy,time,sys
from arcpy import env

ms_connection = r'Database Connections\GIS_SRP-IDL-chrisvm.sde'
arcpy.env.workspace = ms_connection


featureClassList = []
for fc in arcpy.ListFeatureClasses():
    featureClassList.append(os.path.join(arcpy.env.workspace,fc))

datasetList = arcpy.ListDatasets("*", "Feature")
for dataset in datasetList:
    arcpy.env.workspace = os.path.join(ms_connection,dataset.split(".")[2])
    for fc in arcpy.ListFeatureClasses():
        featureClassList.append(os.path.join(arcpy.env.workspace,fc))

for i in featureClassList:
    if arcpy.Exists(i):
        print "{} exists.".format(i)
    else:
        print "{} does not exist".format(i)