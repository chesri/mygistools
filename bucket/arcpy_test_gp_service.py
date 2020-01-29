#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     01/04/2019
# Copyright:   (c) chrism 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy
import datetime

the_input = arcpy.GetParameterAsText(0)
now = datetime.datetime.now()
nd = now.strftime('%m/%d/%Y %H:%M:%S')

output = "You entered {} at {}".format(the_input,nd)
arcpy.SetParameterAsText(0, output)