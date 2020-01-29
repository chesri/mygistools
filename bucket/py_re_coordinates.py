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
import csv, re

ts_file = r'C:\OneDrive - Esri\DS_Workspace\Yuma\ts_file_dev\angles.txt'
lol = list(line for line in csv.reader(open(ts_file, 'rb'), delimiter='\t') if line)

for line in lol:
    #p = re.compile('(^\d{,3}).?(\d+).?(\d+)\S')
    #print p.sub('COLOR',line)

    #string =  ''.join(line) + ": " + re.sub('\D', ' ', line[0])
    pstring =  ''.join(line) + ": " + re.sub('\D', ' ', line[0])
    string = str(re.sub('\D', ' ', line[0].translate(None,' '))).strip()
    if len(string.split(' ')) == 3:
        dd = (float(string.split(' ')[0])/1) + (float(string.split(' ')[1])/60) + (float(string.split(' ')[2])/3600)
    if len(string.split(' ')) == 2:
        dd = (float(string.split(' ')[0])/1) + (float(string.split(' ')[1])/60)
    if len(string.split(' ')) == 1:
        dd = (float(string.split(' ')[0])/1)

    print dd

##for line in lol:
##
##    b = ''.join(line)
##    #print b + "\t\d: " + str(bool(re.search("\d+?", b)))
##
##    pattern = re.compile('(^\d{,3}).?(\d+).?(\d+)\S')
##    matches = pattern.finditer(b)
##
##    for match in matches:
##        print b + "\t: " + (match).group(1)
##        print b + "\t: " + (match).group(2)
##        print b + "\t: " + (match).group(3)

##
##    matchObj = re.match( r'(\d)°(\d) (\d)', b, re.M|re.I)
##
##    if matchObj:
##       print "matchObj.group() : ", matchObj.group()
##       print "matchObj.group(1) : ", matchObj.group(1)
##       print "matchObj.group(2) : ", matchObj.group(2)
##    else:
##       print "No match!!"