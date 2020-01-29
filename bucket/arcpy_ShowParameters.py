#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     02/01/2020
# Copyright:   (c) chrism 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy, os, sys



arcpy.env.qualifiedFieldNames = True
arcpy.AddMessage(arcpy.GetParameter(0))
arcpy.AddMessage(arcpy.GetParameter(1))
desc = arcpy.Describe(arcpy.GetParameter(0))

fields = [field.name for field in desc.fields]
##for field in fields:
##    arcpy.AddMessage("desc.fields = {}".format(field))


guid = arcpy.ListFields(arcpy.GetParameter(0),"*GlobalID")[0]
pDate = arcpy.ListFields(arcpy.GetParameter(0),"*project_date")[0]
pName = arcpy.ListFields(arcpy.GetParameter(0),"*program_name")[0]
tOfficer = arcpy.ListFields(arcpy.GetParameter(0),"*test_officer")[0]

#project_fields = ['YUMA_Test.SDE.projects.GlobalID']   ## ['GlobalID','project_date', 'rtss_program_name', 'rtss_test_officer']
project_fields = [guid.name,pDate.name,pName.name,tOfficer.name]   ## ['GlobalID','project_date', 'rtss_program_name', 'rtss_test_officer']
projects = [prj for prj in arcpy.da.SearchCursor(arcpy.GetParameter(0),project_fields)]
arcpy.AddMessage("PROJECTS ------------------------")
for p in projects:
    print p

for r in [row[0] for row in arcpy.da.SearchCursor(arcpy.GetParameter(1),"*")]:
    arcpy.AddMessage(r)
