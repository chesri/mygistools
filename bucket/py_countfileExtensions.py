#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     18/06/2019
# Copyright:   (c) chrism 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os, sys
root_dir = r'C:\Temp'

file_count = 0
ext_dict = {}

for root, directories, files in os.walk(root_dir):
    for file in files:
        ext = os.path.splitext(file)[1]
        if not ext in ext_dict.keys():
            ext_dict[ext] = 1
        elif ext in ext_dict.keys():
            ext_dict[ext] += 1
        file_count += 1

##print("File count: {}".format(file_count))
##print("Unique Extensions: {}".format(ext_dict))