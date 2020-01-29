#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     19/09/2018
# Copyright:   (c) chrism 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os, arcpy, sys

# goal: C:\Users\chrism\AppData\Roaming\Esri\Desktop10.6\ArcCatalog
AppData = os.environ.get("APPDATA")
DTversion = arcpy.GetInstallInfo()["Version"]

conn_path = os.path.join(AppData,'Esri\Desktop' + DTversion[:4],'ArcCatalog')

##print(AppData)
##print(DTversion)

##if os.path.isdir(conn_path):
##    print (conn_path)


for root, dirs, files in os.walk(conn_path):
    for f in files:
        if f.endswith('.ags'):
            print(f)