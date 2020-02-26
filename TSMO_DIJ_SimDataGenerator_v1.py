#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     25/02/2020
# Copyright:   (c) chrism 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy
import os
import math, random

class DIJ:

    def __init__(self):

        no_id = str(random.randint(100,999))
        self.bumper_number = getBumperNumber()
        fetchUnit = getUnitType()
        self.unit_type     = fetchUnit[0]
        ##self.channels      = fetchUnit[1]
        self.unit_unique_id      = fetchUnit[0][4] + no_id
        self.threat_1_unique_id  = getThreatCode()
        self.threat_1_active     = 0
        self.threat_2_unique_id  = getThreatCode()
        self.threat_2_active     = 0
        self.threat_3_unique_id  = getThreatCode() if self.unit_type == 'DIJ_M6' else ''
        self.threat_3_active     = 0
        self.threat_4_unique_id  = getThreatCode() if self.unit_type == 'DIJ_M6' else ''
        self.threat_4_active     = 0
        self.threat_5_unique_id  = getThreatCode() if self.unit_type == 'DIJ_M6' else ''
        self.threat_5_active     = 0
        self.threat_6_unique_id  = getThreatCode() if self.unit_type == 'DIJ_M6' else ''
        self.threat_6_active     = 0
        self.hasactivethreat     = 'false'


    def track(self):
        return (self.bumper_number,
                self.unit_type,
                self.unit_unique_id,
                self.threat_1_unique_id,
                self.threat_1_active,
                self.threat_2_unique_id,
                self.threat_2_active,
                self.threat_3_unique_id,
                self.threat_3_active,
                self.threat_4_unique_id,
                self.threat_4_active,
                self.threat_5_unique_id,
                self.threat_5_active,
                self.threat_6_unique_id,
                self.threat_6_active,
                self.hasactivethreat,
                self.shape)

def getThreatCode():
    threats = ['AAAA','BBBB','CCCC','DDDD','EEEE','FFFF','GGGG','HHHH','IIII','JJJJ','KKKK']
    return threats[random.randint(0,10)]

def getBumperNumber():
    ''' Generate random bumper number '''
    index = random.randint(1,24)
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    bumper_no = 'J' + abc[random.randint(1,24)] + abc[random.randint(1,24)] + abc[random.randint(1,24)] + '-' + str(random.randint(100,999))

    return bumper_no

def getUnitType():
    '''returns tuple of unit_type, #channels'''
    unit_types = {'DIJ_M6':6,'DIJ_DISMOUNT':2}
    return unit_types.items()[random.randint(0,1)]

def getGroupName():

    groups = ['101st Airborne','10th Mountain','1st Calavry','1st Infantry','75th Innovation','98th Training']
    return groups[random.randint(0,len(groups)-1)]


# #############################################################################
#


lyr_tracks = arcpy.GetParameter(0)  # line (roads) where vehicles traverse
lyr_dijs = arcpy.GetParameter(1)    # destination for generated point data (along lyr_tracks)
##lyr_tracks = r'C:\OneDrive - Esri\DS_Workspace\TSMO_DIJ\Development\sim_dijs\simdata.gdb\drive_tracks'
##lyr_dijs = r'C:\OneDrive - Esri\DS_Workspace\TSMO_DIJ\Development\sim_dijs\simdata.gdb\dijs'

mxd = arcpy.mapping.MapDocument("CURRENT")
df = mxd.activeDataFrame

##for d in range(0,5):
##    the_dij = DIJ()
##
##    print the_dij.__dict__

fields = ['message_receive_log_id','bumper_number','unit_type','unit_unique_id','threat_1_unique_id','threat_1_active','threat_2_unique_id','threat_2_active','threat_3_unique_id','threat_3_active','threat_4_unique_id','threat_4_active','threat_5_unique_id','threat_5_active','threat_6_unique_id','threat_6_active','hasactivethreat','SHAPE@']
sr = arcpy.Describe(lyr_tracks).spatialReference
interval = float(500)

icursor = arcpy.da.InsertCursor(lyr_dijs, fields)
with arcpy.da.SearchCursor(lyr_tracks, ['SHAPE@LENGTH', 'SHAPE@']) as cursor:
    for ri,row in enumerate(cursor):

        the_DIJ = DIJ()

        # retreive total lenght of line segment
        length = row[0]
        arcpy.AddMessage("Length: " + str(length))

        # create the number of stations by dividing spacing by total lenght of line
        arcpy.AddMessage("interval: " + str(interval))
        arcpy.AddMessage("length: " + str(length))
        noIntervals = int(math.floor(length / interval))
        arcpy.AddMessage('noIntervals = ' + str(noIntervals))

        # determine length of last segment ??
        lastSegLength = length - interval * noIntervals

        # loop through the count of intervals and add a point
        for x in range(1, noIntervals):
            newPt = row[1].positionAlongLine(interval * x)
            arcpy.AddMessage("Adding point at " + str(interval * x))
            the_DIJ.shape = newPt
            insert = (ri + x,) + the_DIJ.track()  ## message_receive_log_id is index of ...
            icursor.insertRow(insert)
        if lastSegLength < 500:
            arcpy.AddMessage("Adding last point at " + str(interval * noIntervals + lastSegLength))
            lastPt = row[1].positionAlongLine(interval * noIntervals + lastSegLength)
        else:
            lastPt = row[1].positionAlongLine(interval * noIntervals)
            the_DIJ.shape = lastPt
        icursor.insertRow(the_DIJ.track())

del row
del cursor
