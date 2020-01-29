#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     12/07/2017
# Copyright:   (c) chrism 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import datetime

def formatDateTime(split_date,split_time):
##    split_date = date.split("/")[2],date.split("/")[1],date.split("/")[0]
##    split_time = time.split(":")[0],time.split(":")[1],time.split(":")[2]
    r_date = datetime.datetime(int(split_date.split("/")[2]),int(split_date.split("/")[1]),int(split_date.split("/")[0]),int(split_time.split(":")[0]),int(split_time.split(":")[1]),int(split_time.split(":")[2]))
    return str(r_date.strftime('%m/%d/%Y %H:%M:%S'))

# READ IN FILE with dates in first column and time in second column
file = r'C:\OneDrive - Esri\DS_Workspace\TSMO_new\TUD\TUD_2017\SIGINT_files\sigint_20160504_170720.csv'

myfile = open(file,'r')
##x=0
for x, row in enumerate(myfile):
    the_cell = row.split(",")[1]

    if x != 0:
        the_date = the_cell.split(" ")[0]

        the_time = the_cell.split(" ")[1]

        print formatDateTime(the_date,the_time)

## print str(r_date.strftime('%m/%d/%Y %H:%M:%S'))
