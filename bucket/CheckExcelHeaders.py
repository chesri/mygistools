#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     05/08/2015
# Copyright:   (c) chrism 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import xlrd
import sys

##if len(sys.argv) < 1:
##    print("Expected an input Excel file name.")
##    exit()
##infile = sys.argv[1]

infile = r'C:\Users\chrism\Desktop\TESTING\SDSFIE Test 62\INPUT\SampleCrosswalk.xlsx'

book = xlrd.open_workbook(infile)
field_names = ['SourceFeatureDataset','SourceFeatureClass','SourceSubtype','SourceFCSelectionAttribute1','SourceFCSelectionAttribute1Value','SourceFCSelectionAttribute2','SourceFCSelectionAttribute2Value','SourceCrosswalkAttributeName','SourceCrosswalkAttributeValue','SourceCrosswalkWhereClause','TargetFeatureDataset','TargetFeatureClass','TargetCrosswalkAttributeName','TargetCrosswalkAttributeValue','attribute values','EXCEPTIONS (Orphans, etc.)','ISSUES, COMMENTS, etc.']
c = 0

for name in book.sheet_names():
    if name == 'FDS_FC_ATT_Utilities':
        sheet = book.sheet_by_name(name)
        cells = sheet.row(0)
        cols = sheet.ncols
        lencells = len(cells)
        lenx = len(field_names)
        if len(field_names) < 17:
            print "Inconsistent number of columns. Stopping check."
            exit()

        for i in cells:
            print "Does " + i.value + " = " + field_names[c],
            if i.value == field_names[c]:
                print "TRUE"
            else:
                print "FALSE"
            c = c + 1




