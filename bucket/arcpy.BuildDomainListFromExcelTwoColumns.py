#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     26/02/2018
# Copyright:   (c) chrism 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy, os, xlrd, sys, linecache
from xlrd import open_workbook

def fixType(cell_obj,toType):
    if toType == 'number':
        if cell_obj.ctype == 0:  # empty
            return 0
        if cell_obj.ctype == 1:  # unicode string
            return 0
        if cell_obj.ctype == 2 or cell_obj.ctype == 3:  #float
            return cell_obj.value
        if cell_obj.ctype == 4:  # boolean
            if raw:
                return 1
            if not raw:
                return 0
        if cell_obj.ctype == 5:  # int
            return cell_obj.value
        if cell_obj.ctype ==6:# empty string
            return 0
    if toType == 'integer':
        if cell_obj.ctype == 0:  # empty
            return 0
        if cell_obj.ctype == 1:  # unicode string
            return 0
        if cell_obj.ctype == 2 or cell_obj.ctype == 3:  #float
            return int(cell_obj.value)
        if cell_obj.ctype == 3:
            d = datetime.datetime(*xlrd.xldate_as_tuple(cells[27].value,xls_book.datemode))
            y = int(d.strftime('%Y'))              #y = str(d.strftime('%m/%d/%Y %H:%M:%S'))
            return y
        if cell_obj.ctype == 4:  # boolean
            if raw:
                return 1
            if not raw:
                return 0
        if cell_obj.ctype == 5:  # int
            return cell_obj.value
        if cell_obj.ctype ==6:# empty string
            return 0
    if toType == 'string':
        if cell_obj.ctype == 0:  # empty
            return ''
        if cell_obj.ctype == 1:  # unicode string
            return str(cell_obj.value)
        if cell_obj.ctype == 2 or cell_obj.ctype == 3:  #float
            return str(int(cell_obj.value))
        if cell_obj.ctype == 3:
            d = datetime.datetime(*xlrd.xldate_as_tuple(cells[27].value,xls_book.datemode))
            y = str(d.strftime('%Y'))              #y = str(d.strftime('%m/%d/%Y %H:%M:%S'))
            return y
        if cell_obj.ctype == 4:  # boolean
            if raw:
                return 'True'
            if not raw:
                return 'False'
        if cell_obj.ctype == 5:  # int
            return str(cell_obj.value)
        if cell_obj.ctype ==6:# empty string
            return ''

def getCol(col_Alpha):
    dict = {'A':'0','B':'1','C':'2','D':'3','E':'4','F':'5','G':'6','H':'7','I':'8','J':'9','K':'10','L':'11','M':'12','N':'13','O':'14','P':'15','Q':'16','R':'17','S':'18','T':'19','U':'20','V':'21','W':'22','X':'23','Y':'24','Z':'25','AA':'26','AB':'27','AC':'28','AD':'29','AE':'30','AF':'31','AG':'32','AH':'33','AI':'34','AJ':'35','AK':'36','AL':'37','AM':'38','AN':'39','AO':'40','AP':'41','AQ':'42','AR':'43','AS':'44','AT':'45','AU':'46','AV':'47','AW':'48','AX':'49','AY':'50','AZ':'51','BA':'52','BB':'53','BC':'54','BD':'55','BE':'56','BF':'57','BG':'58','BH':'59','BI':'60','BJ':'61','BK':'62','BL':'63','BM':'64','BN':'65','BO':'66','BP':'67','BQ':'68','BR':'69','BS':'70','BT':'71','BU':'72','BV':'73','BW':'74','BX':'75','BY':'76','BZ':'77','CA':'78','CB':'79','CC':'80','CD':'81','CE':'82','CF':'83','CG':'84','CH':'85','CI':'86','CJ':'87','CK':'88','CL':'89','CM':'90','CN':'91','CO':'92','CP':'93','CQ':'94'}
    return int(dict[col_Alpha])

def openReadXLS(xls_book,xls_sheet,first, second):
    if xls_sheet in xls_book.sheet_names():
        sheet = xls_book.sheet_by_name(xls_sheet)
    else:
        print 'Sheet "{}" not found.'.format(xls_sheet)
        exit()

    sheet = xls_book.sheet_by_name(xls_sheet)
    print("Reading \"{}\"".format(xls_sheet))
    print("Rows: {}".format(sheet.nrows))

    xls_list = []
    header = []

    headers = sheet.row(0)
    rowx = 1
    while rowx < sheet.nrows - 1:
        tmp_row = []

        cells = sheet.row(rowx)
        print fixType(cells[getCol(first)],"integer"),fixType(cells[getCol(second)],"string")
        xls_list.append(tmp_row)
        del tmp_row
        rowx = rowx + 1
    return xls_list

excelFile = r'D:\Workspace\MCIEAST_IR_Project\Documents\esri_modified_source_data\Final Q1-Q4 Mitigation Plan 02202018_Inc_BuildDate_HistoricalCode.xlsx'
excel_book = 'Primary Mitigation Plan'

book = open_workbook(filename=excelFile)
cell_01 = 'R'
cell_02 = 'S'

xls_list = openReadXLS(book,excel_book, cell_01, cell_02)
