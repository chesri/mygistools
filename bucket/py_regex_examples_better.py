#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     05/03/2019
# Copyright:   (c) chrism 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os, re, csv
## reference: https://www.w3schools.com/python/python_regex.asp

##the_path = 'C:\Temp\SOFPREP_FS\cib\sof_cib\sofcib_1\cb01na174k1_sofcib\rpf,rpf'
#the_path = "this is sentence with cib in the text and cibtwo in too."

##d_dir = r'C:\Temp'
##for root, dirs, files in os.walk(d_dir):
##    print root, dirs, files

###the_string = re.sub('[:|]', '', the_path)
##z = re.match(r".+(cib)",the_path)
##y = re.search("cib", the_path)
##x = re.findall("cib", the_path)
##w = re.split("cib",the_path)
##
##if z:
##    print "z: {}".format(z.groups()[0])
##    print "y: {}".format(y.string)
##    #print "y: {}".format(y)
##    print "x: {}".format(x)
##    print "w: {}".format(w)


in_file = r'C:\OneDrive - Esri\DS_Workspace\Yuma\from_customer\combined\M_GP12 22MAY18.txt'
file_data = list(line for line in csv.reader(open(in_file, 'rb'), delimiter='\t') if line)
for line in file_data:
    x = re.findall("[\w]+", unicode(line))
    print "x: {}".format(x)