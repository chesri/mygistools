#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     20/02/2018
# Copyright:   (c) chrism 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy, os
from datetime import datetime, timedelta

def getnewDate(in_date):
    tdelta = datetime.datetime.now() - in_date
    new_tor = datetime(tdelta.year, tdelta.month, tdelta.day, tdelta.hour)
    return new_tor


#Read feature class "TimeOfReceipt" column, send to getnewDate function.
fc = r'D:\Workspace\TSMO\Demo\FromTrackDataToInformation\geomn_scratch.gdb\_tmp_tracks'

cursor = arcpy.da.SearchCursor(fc,"TimeOfReceipt")
for row in cursor:
    print getnewDate(row[0])

del cursor
