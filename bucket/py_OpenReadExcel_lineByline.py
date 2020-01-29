#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     27/11/2017
# Copyright:   (c) chrism 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
from xlrd import open_workbook

def main(thefile):
    book = open_workbook(filename=thefile)

    for name in book.sheet_names():
        print "\t\t", os.path.basename(thefile), "\\", name
        sheet = book.sheet_by_name(name)
        rowindex = 0
        while rowindex < sheet.nrows:
            ##print "reading row: {}".format(rowindex)
            cells = sheet.row(rowindex)
            print('row {}: {}'.format(rowindex,cells))
            rowindex = rowindex + 1

if __name__ == '__main__':

    rootpath = r'C:\OneDrive - Esri\Temp\Yuma_Temp'
    for root, dirs, files in os.walk(rootpath):

        for file in files:
            if file.endswith(".xlsx") or file.endswith(".xls"):
                print os.path.realpath(root)
                print "\t->" + file
                main(os.path.join(os.path.realpath(root), file))

