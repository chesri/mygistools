#-------------------------------------------------------------------------------
# Name:        arcpy_rw_csv_example.py
# Purpose:
#
# Author:      chrism
#
# Created:     21/06/2017
# Copyright:   (c) chrism 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy, csv, tempfile, os, uuid

# ##########################################
input = r'D:\Workspace\TSMO\TUD_2017\SIGINT_files\sigint_20160503_194056.csv'
##output = "in_memory\\" + str(uuid.uuid4())
output = tempfile.NamedTemporaryFile(prefix='tmp_',suffix='.csv',delete=False)
##print "output is: " + str(output.name)
#output.close()
ws = r'C:\Users\chrism\Documents\ArcGIS\Default.gdb'

data = []

with open(input, 'rb') as f:
    reader = csv.reader(f)
    clean_header = []
    index = 0
    for row in reader:
        if index == 0:
            header = row
            for h in range(0,len(row)):
                clean_header.append(arcpy.ValidateFieldName(row[h],ws))
            data.append(clean_header)
        elif index < 4:
            data.append(row)
        index = index + 1

f.close()

writer = csv.writer(output,delimiter=',')
for line in data:
    writer.writerow(line)
output.close()
print "output is: " + str(output.name)
