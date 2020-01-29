#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     01/07/2019
# Copyright:   (c) chrism 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os, sys, xlrd
from xlrd import open_workbook

topfolder = r'C:\Temp\Civil Surveys Version 1 (May19)'
filecounter = 0
itemcounter = 0
totalitems = 0

for rootdir, directory, files in os.walk(topfolder):
    for file in files:
        if os.path.splitext(file)[1] in [ '.xls', '.xlsx' ]:
            fullpath = os.path.join(rootdir,file)

            if os.access(fullpath, os.R_OK):

                try:
                    book = open_workbook(fullpath)
                    filecounter += 1

                    for name in book.sheet_names():

                        sheet = book.sheet_by_name(name)

                        while itemcounter < sheet.nrows:
                            itemcounter += 1
                            totalitems += 1
                        print("{},{},{},{}".format(file,name,itemcounter,fullpath))
                        itemcounter = 0

                except RuntimeError as e:
                    print str(e)
                except IOError as e:
                    print str(e)
                except Exception as e:
                    print str(e)

            else:
                print("Could not open {}".format(fullpath))

print("File Count: {}, Row Count: {}".format(filecounter,totalitems))