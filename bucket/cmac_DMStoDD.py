#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      chrism
#
# Created:     07/03/2019
# Copyright:   (c) chrism 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os, re, csv

def DMStoDD(inDMS):
    print("Length of inDMS: {}".format(len(inDMS)))
    debug_string = "inDMS: {}".format(inDMS)
    print(debug_string)
    dd = -1
    if len(inDMS) > 0:
        pstring =  ''.join(inDMS) + ": " + re.sub('\D', ' ', inDMS)
        string = str(re.sub('\D', ' ', inDMS.translate(None,' '))).strip()
        if len(string.split(' ')) == 3:
            dd = (float(string.split(' ')[0])/1) + (float(string.split(' ')[1])/60) + (float(string.split(' ')[2])/3600)
        if len(string.split(' ')) == 2:
            dd = (float(string.split(' ')[0])/1) + (float(string.split(' ')[1])/60)
        if len(string.split(' ')) == 1:
            dd = (float(string.split(' ')[0])/1)
    return dd

def testRE(inDMS):

    w = re.split("\D",inDMS)
    x = re.findall("[0-9]+", inDMS)
    y = re.search("\d+", inDMS)
    z = re.match(r"(\d)",inDMS)

    if y:
        y = y.string
    if z:
        z = z.groups()[0]

    return w,x,y,z

coords_file = r"C:\OneDrive - Esri\DS_Workspace\Yuma\ts_file_dev\angles_dms.txt"
file_data = (line for line in csv.reader(open(coords_file, 'rb'), delimiter='\t') if line)

##col0 = 15
##col1 = 15
##col2 = 15
##col3 = 15
##col4 = 14
header = "ORIGINAL,Match,Search,Findall,Split"
print header
##string = ("-" * col0).ljust(col0 ++ 1) + ("-" * col1).ljust(col1 ++ 1) + ("-" * col2).rjust(col2 ++ 1) + ("-" * col3).rjust(col3 ++ 1) + ("-" * col4).rjust(col4 ++ 1)
##print string

for line in file_data:
    w,x,y,z = testRE(line[0])
    print("\ninput: {}".format(line[0]))
    print("Split: {}".format(w))
    print("Findall: {}".format(x))
    print("Search: {}".format(y))
    print("Match: {}".format(z))