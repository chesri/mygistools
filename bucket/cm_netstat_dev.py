#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     09/08/2017
# Copyright:   (c) chrism 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import subprocess, sys

cmd = "netstat -p tcp -f inet"

p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)

##while True:
##    out = p.stderr.read(1)
##    if out == '' and p.poll() != None:
##        break
##    if out != '':
##        sys.stdout.write(out)
##        sys.stdout.flush()
