#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      scot6739
#
# Created:     11/10/2018
# Copyright:   (c) scot6739 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy, os

file = r'C:\Box Sync\DS_Workspace\Army_SRP_MIM\MIMtoRaster_Test\Copy_of_FINAL_FTRILEYMIM_50K_2010.mxd'
file = r'C:\Box Sync\DS_Workspace\Army_SRP_MIM\FTRILEYMIM\FINAL_FTRILEYMIM_50K_2010.mxd'

##for name in os.listdir(file):
##    path = os.path.join(file, name)
##    if os.path.isfile(path):
##        basename, extension = os.path.splitext(path)
##        if extension == ".mxd":
##            mxd = arcpy.mapping.MapDocument(path)
##            print "MXD: " + path
##            brokelinks = arcpy.mapping.ListBrokenDataSources(mxd)
##            for brokelink in brokelinks:
##                print "\t" + brokelink.name
##del mxd

if os.path.isfile(file):
    mxd = arcpy.mapping.MapDocument(file)
    if len(arcpy.mapping.ListBrokenDataSources(mxd))> 0:
        arcpy.AddError("One or more layer data sources are broken. Fix the ")
        arcpy.AddMessage("data source or remove the broken layer, then try again.")

        for bl in arcpy.mapping.ListBrokenDataSources(mxd):
            print "\t" + bl.name
