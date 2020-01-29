#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     07/02/2019
# Copyright:   (c) chrism 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import csv

classification = 'Unknown'

ts_file = r'C:\OneDrive - Esri\DS_Workspace\Yuma\ts_file_dev\M_GP12 22MAY18.txt'
lol = list(line for line in csv.reader(open(ts_file, 'rb'), delimiter='\t') if line)
##
##rIndex = 0
##st_id = -1
##bs_id = -1
##pt_id = -1
##for line in lol:
##    if line[0].lower() in ['classification', 'station id', 'backsight', 'pt id']:
##        last = line[0].lower()
##        print '-' * 80
##        while last == 'station id':
##            print ['STATION: '] + lol[rIndex]
##            rIndex += 1

with open(ts_file) as infile:
    for i, line in enumerate(infile):
        row = line.strip("\n\r\t :").split(':')
##        if row[0].lower() in ['classification']:
##            classification = infile[i + 1]
        print row
