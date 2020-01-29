#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     26/02/2018
# Copyright:   (c) chrism 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy, re
from string import maketrans

##def hasNumbers(inputString):
##    for end in ('RD','ST','ND','TH'):
##        if inputString[-2:] == end:
##            return False
##        else:
##            return any(char.isdigit() for char in inputString)
##    return False

##def extractBldgNo(title):
##    dNo = [str(s) for s in re.sub('[^a-zA-Z0-9\n\.]', ' ', title).split() if hasNumbers(s)]
##    if len(dNo) > 0:
##        dNo = str(dNo[0])
##    else:
##        dNo = ''
##    return dNo
def pluckBldgNo(title):

    a = ['BUILDING ', 'DOCK ', 'BLDGS ', 'BLDG ','BLDG. ', 'STRUCTURE ', 'FACILITY ', 'RAMP ', 'SHED ', 'BDLG ', 'TOWER ', 'BRIDGE ']
    for ck in a:
        if title.find(ck) >= 0:
            start = title.find(ck)+len(ck)
            print "start: " + str(start) + "  stop: " + str(title.find(' ',start))
            if title.find(' ',start) > 0:
                bn = title[start:title.find(' ',start)]
            else:
                bn = title[start:]

            if bn.split(',') > 0:
                return bn.split(',')[0]
            else:
                return bn

    if len(title.split()) > 0:
        return extractBldgNo(title)



def extractBldgNo(title):

    dNo = [str(s) for s in re.sub('[^a-zA-Z0-9\n\.]', ' ', title).split() if any(char.isdigit() for char in s) and not s[-2:] in ('RD','ST','ND','TH')]

    if len(dNo) > 0:
        return str(dNo[0])
    return ''

def replaceSpecialCharacters(string):
    ch = ['!','@','#','$','%','^','&','*','(',')','<','>','/']
    for c in ch:
        string = str(string).replace(c,' ')

    return string


def fetchBldgNo(title):
    split_title = replaceSpecialCharacters(title).split()
    if title == None:
        return str('')
    for word in split_title:
##        if len(word.split(',')) > 1:
##            word = word.split(',')[0]
        if any(char.isdigit() for char in word) and not word[-2:] in ('RD','ST','ND','TH'):
            if len(word) > 0:
                return str(word).split(',')[0]
            return str('')

useCursor = True
if useCursor:
    table = r'D:\Workspace\MCIEAST_IR_Project\Data\MCI_IRDMv1.gdb\source_10'
    fields = ['Project_Title', 'Facility_Number']
    cursor = arcpy.da.SearchCursor(table,fields)

    for row in cursor:

        try:
            title = row[0]
            print "\n" + title
            print "\t    fetchBldg: " + fetchBldgNo(title)
            print "\textractBldgNo: " + extractBldgNo(title)
            print "\t  pluckBldgNo: " + pluckBldgNo(title)
        except:
            pass

    del cursor
else:
    #test_titles = ['DEMOLISH BUILDING 0997','','123, 345, 567','DEMOLISH BUILDING 4870','DEMOLISH UN290AS BRAVO ACCESS RD (2,364 SY GRAVEL ACCESS RD)', 'DEMOLISH STRUCTURE SAS4208', 'DEMOLISH BLDG #4870', 'BLDG. AS4110 INTERIOR/EXTERIOR REPAIR PROJECT', 'DEMOLISH MULTIPLE AREA STEAM PIT AND SUPPORT SYSTEM', 'DEMOLISH BLDG AS4100A (CONCRETE SLAB NW CORNER OF AS4100)', 'DEMOLISH UN371 PORTION OF CONCRETE VICINITY OF AS831', 'DEMOLISH 3RD BN DOCK 4581A','MODERNIZE FIRE ALARM SYSTEM IN BLDGS 418,728,729,1142,1623']
    #test_titles = ['BLDG. AS4110 INTERIOR/EXTERIOR REPAIR PROJECT', 'DEMOLISH MULTIPLE AREA STEAM PIT AND SUPPORT SYSTEM', 'DEMOLISH BLDG AS4100A (CONCRETE SLAB NW CORNER OF AS4100)', 'DEMOLISH UN371 PORTION OF CONCRETE VICINITY OF AS831', 'DEMOLISH 3RD BN DOCK 4581A','MODERNIZE FIRE ALARM SYSTEM IN BLDGS 418,728,729,1142,1623']
    test_titles = ['DEMOLISH A-RANGE OPS CENTER BLDG 786A']
    for title in test_titles:
        print "\n" + title
        try:
            print "\t    fetchBldg: " + fetchBldgNo(title)
            print "\textractBldgNo: " + extractBldgNo(title)
            print "\t  pluckBldgNo: " + pluckBldgNo(title)

        except:
            pass
