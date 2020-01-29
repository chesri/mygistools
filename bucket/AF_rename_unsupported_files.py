#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     20/09/2018
# Copyright:   (c) chrism 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os, sys

rename = False
if len(sys.argv) > 1:
    rename = sys.argv[1]
print('rename = ' + str(rename))

exit()
with open(r'C:\Users\chrism\Desktop\unsupported.txt') as file:
    data = file.readlines()

for line in data:
    line = line.rstrip('\n')
    folder = os.path.dirname(line)
    filen = os.path.basename(line)
    unreg = 'regsvr32 /u "' + line + '"'
    regit = 'regsvr32 /s "' + line + '"'
    if os.path.isfile(line):
        if rename:
            print("Unregistering {} and renaming it to {}".format(filen,'xx_' + filen))
            #os.system(unreg)
            os.rename(line,os.path.join(folder,'xx_' + filen))
        else:
            print("EXIST: " + filen + ' @ ' + folder)
    elif os.path.isfile(os.path.join(folder,'xx_' + filen)) and not rename:
        print("renaming {} to {}".format('xx_' + filen,filen))
        os.rename(os.path.join(folder,'xx_' + filen),line)
        #os.system(regit)
    else:
        print("NOT EXISTS: "+ line)
