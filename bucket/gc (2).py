#-------------------------------------------------------------------------------
# Name:        GC.py
# Purpose:     scans a directory of JPG and AVI files and write metadata to XLS
#
# Author:      chrism
#
# Created:     19/12/2014
# Copyright:   (c) chrism 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import xlwt
import os, sys, xlwt
import getopt
import time
import datetime
import shutil

def get_creation_date(filename):
    m_date = round(os.stat(filename).st_mtime)
    c_date = round(os.stat(filename).st_ctime)

    if m_date > c_date:
        c = os.path.getctime(filename)
    else:
        c = os.path.getmtime(filename)

    return datetime.datetime.fromtimestamp(c)

def split_path(p):
    a,b = os.path.split(p)
    return (split_path(a) if len(a) and len(b) else []) + [b]

def get_yesno(question):
    yes = set(['yes','y', 'ye', ''])
    no = set(['no','n'])

    choice = raw_input(question).lower()
    if choice in yes:
       return True
    elif choice in no:
       return False
    else:
       sys.stdout.write("Please respond with 'yes' or 'no'")

if not len(sys.argv[1:]) == 3:
    print "usage: gc.py <output_folder> <input_dir> <output.xls>"
    exit()

output_folder = sys.argv[1]
input_dir = sys.argv[2]
output_xls = sys.argv[3]

# input_dir = r"E:\DCIM\100MEDIA"
# output_xls = os.path.join(os.getcwd(), "C:\DATA\GameCameras\gc_output.xls")
# output_xls = os.path.join(sys.argv[1], "new_gc_inputs.xls")
# output_xls = r"C:\DATA\GameCameras\new_gc_inputs.xls"

book = xlwt.Workbook()
sh = book.add_sheet('DirList')
date_format = xlwt.XFStyle()
date_format.num_format_str = 'm/d/yy h:mm;@'

c=0
for header in ['ID','DateTimeBegin','DateTimeEnd','FolderName','Fullpath','FileName','Location','WGS84_Y','WGS84_X','MediaType','Trigger','Activity','Direction','Comments','TimeOfDay','Hyperlink','Dow']:
    sh.write(0,c,header)
    c = c + 1

r = 1
c = 0
id = 1

for path, subdirs, files in os.walk(input_dir):

    for name in files:
        fullname = os.path.join(path, name)
        fnam, fext = os.path.splitext(name)

        thetime = get_creation_date(fullname)
        f_name_ymd = "GC_" + thetime.strftime('%y%m%d_%H%M_') + str(id).zfill(2)

        if fext in [".JPG", ".AVI"]:

            try:
                #if os.path.basename(name).find("_") > 0:
                #    location = os.path.basename(path).split("_")[1]
                if output_folder.find("_") > 0:
                    location = "_" + output_folder.split("_")[1]
            except:
                location = ""

            #newfile_full = os.path.join(r"C:\Users\Cmac\Pictures\Game Camera",output_folder, f_name_ymd + fext)
            newfile_full = os.path.join(output_folder, f_name_ymd + fext)

            sh.write(r,0,id)
            sh.write(r,1,get_creation_date(fullname), date_format)
            sh.write(r,3,output_folder)
            sh.write(r,4,os.path.join(r"C:\Users\Cmac\Pictures\Game Camera",output_folder))
            sh.write(r,5,f_name_ymd + fext)
            sh.write(r,6,location)
            if fext == ".AVI":
                sh.write(r,9,"video")
            elif fext == ".JPG":
                sh.write(r,9,"image")
            else:
                sh.write(r,9,"NA")
            sh.write(r,15,newfile_full)


##            if not os.path.exists(os.path.join(r"C:\Users\Cmac\Pictures\Game Camera",output_folder)):
##                os.mkdir(os.path.join(r"C:\Users\Cmac\Pictures\Game Camera",output_folder))
            if not os.path.exists(output_folder):
                os.mkdir(os.path.join(output_folder))

            if not os.path.isfile(newfile_full):
                print fullname + " to " + newfile_full
                shutil.copy2(fullname, newfile_full)

            id = id + 1
            r = r + 1

book.save(output_xls)

if get_yesno("DELETE source files (yes | no): "):
    shutil.rmtree(input_dir)

