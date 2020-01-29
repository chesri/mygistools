#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     24/10/2016
# Copyright:   (c) chrism 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy
from datetime import datetime, timedelta

# ##############################################################################
def countRows(tbl,timeField,begin,end):


    tor_field = arcpy.ListFields(tbl,timeField,"Date")[0]
    expression = "(%s >= \'%s\') and (%s <= \'%s\' )" % (tor_field.name, begin, tor_field.name, end)
    #arcpy.AddMessage("Counting rows in %s with %s" % (tbl.name,expression))

    rows = 0
    cursor = arcpy.da.SearchCursor(tbl,tor_field.name,expression)
    for c in cursor:
        rows = rows + 1
    del cursor
    return rows

def writeResultToFile():
    # open the log file and write GDB name in first line and then write the header
    for r in data:
        print r
        output.write(r + "\n")


def listLayerFromSource(theLyr):
    # lLyr = arcpy.mapping.ListLayers(mxd,theLyr,df)[0]
    commonLyrs = []
    for i in arcpy.mapping.ListLayers(mxd,"*",df):
        if i.supports("DATASETNAME"):
            if i.datasetName == theLyr.datasetName:
                commonLyrs.append(i)

    return commonLyrs

def groupByHourReport(gLyr):
    for i in range(totalHours + 1):
        # format to date format (human reaaable); for query and printing to screen
        begin = str((date_1 + timedelta(hours=i)).strftime('%m/%d/%Y %H:%M:%S'))
        end = str((date_1 + timedelta(hours=i+1)).strftime('%m/%d/%Y %H:%M:%S'))

        #lyr = arcpy.mapping.ListLayers(mxd,gLyr,df)[0]
        rows = countRows(gLyr,timeField,begin,end)
        #rows = 0

        #arcpy.AddMessage("\"%s\", %s,%s,%s, %s" % (gLyr.name,i,begin,end,rows))
        string = "\"%s\", %s,%s,%s, %s" % (gLyr.name,i,begin,end,rows)
        data.append(string)
#
# ##############################################################################
mxd = arcpy.mapping.MapDocument("CURRENT")
df = mxd.activeDataFrame

sourceLyr = arcpy.GetParameter(0)
if sourceLyr == '#' or not sourceLyr:
    sourceLyr = r'Database Connections\TENA_GEP_DB.sde\TENA_GEP_DB.sde.V_DF_ALL'

ws = sourceLyr.workspacePath
arcpy.env.workspace = ws

sourceFC = sourceLyr.dataSource.replace("%","")

timeField = arcpy.GetParameterAsText(1)
if timeField == '#' or not timeField:
    timeField = ['TimeOfReceipt']

processALL = arcpy.GetParameter(2)
#fields = ['Command', 'Unit', timeField]

outfile = arcpy.GetParameterAsText(3)
# set-up data list to collect results to write to file later
#global data
data = []
header = "\"Command, Unit\",Reference, BeginHr, EndHr, Tracks"
data.append(header)

# Use cursors with sorting to get minimum and maximum date/time.
myListAscending = sorted([row[0] for row in arcpy.da.SearchCursor(sourceFC,timeField)],reverse=False)
myListDescending = sorted([row[0] for row in arcpy.da.SearchCursor(sourceFC,timeField)],reverse=True)
#bigListAscending = sorted([row[0] for row in arcpy.da.SearchCursor(sourceFC,fields)],reverse=False)

# Use first record from result (lowest value and Highest value to determine time windows for data).
beginDT = myListAscending[0]
endDT = myListDescending[0]
TimeDelta = endDT - beginDT

# Get difference of dates in hours...
# Method 1
TimeDelta.total_seconds() / 3600     # returns total time difference in seconds
totalHours = int(TimeDelta.total_seconds() / 3600)
# OR, Method 2
dayHours = TimeDelta.days * 24
secHours = TimeDelta.seconds / 3600
totalHours = int(dayHours + secHours)

# set begin and end dates with new "rounded" numbers for "blocking" or "grouping" by hour break points.
date_1 = datetime(beginDT.year, beginDT.month, beginDT.day, beginDT.hour)
date_2 = datetime(endDT.year, endDT.month, endDT.day, endDT.hour)

arcpy.AddMessage("Minimum Time: " + str(beginDT))
arcpy.AddMessage("Maximum Time: " + str(endDT))
arcpy.AddMessage("-------------------------------")
arcpy.AddMessage("Grouping will start at: " + str(date_1) + " and increment 1 hour to " + str(totalHours) + " hours.")
arcpy.AddMessage("Grouping will end at: " + str(date_2))
#arcpy.AddMessage("Layer, Index, Begin, End, Rows")

# run through layers (pLyr = processing Layer).
if processALL:
    for pLyr in listLayerFromSource(sourceLyr):
        groupByHourReport(pLyr)
else:
    groupByHourReport(sourceLyr)  # to do just the one input


if outfile <> '#' or outfile:
    output = open(outfile, 'w')
    writeResultToFile()
    output.close()

for d in data:
    arcpy.AddMessage(d)

##for i in range(totalHours + 1):
##    # format to date format (human reaaable); for query and printing to screen
##    begin = str((date_1 + timedelta(hours=i)).strftime('%m/%d/%Y %H:%M:%S'))
##    end = str((date_1 + timedelta(hours=i+1)).strftime('%m/%d/%Y %H:%M:%S'))
##
##    #lyr = arcpy.mapping.ListLayers(mxd,pLyr,df)[0]
##    rows = countRows(pLyr,timeField,begin,end)
##    #rows = 0
##
##    arcpy.AddMessage("\"%s\", %s,%s,%s, %s" % (pLyr.name,i,begin,end,rows))

