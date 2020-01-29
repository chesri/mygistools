#-------------------------------------------------------------------------------
# Name:        copytimer.py
# Purpose:
#
# Author:      chrism
#
# Created:     03/08/2016
# Copyright:   (c) chrism 2016
# Licence:     <your licence>
# Usage:       copytime.py -o output_folder
#-------------------------------------------------------------------------------
import datetime
import shutil
import os
import argparse
import tempfile
import time

def isWritable(path):
    try:
        testfile = tempfile.NamedTemporaryFile(dir = path)
        testfile.close()
    except OSError as e:
        if e.errno == errno.EACCES:  # 13
            return False
        e.filename = path
        raise
    return True

parser = argparse.ArgumentParser(description='sends a 100MB file',usage='copytimer.py -i <file_to_send>')
parser.add_argument('-i','--input_file',help='input file to copy', required=True)
parser.add_argument('-o','--output_folder',help='Output folder path', required=True)
parser.add_argument('-r','--repeat',help='Number of times to copy', required=False, type=int)
parser.add_argument('-s','--sleep',help='Seconds to sleep between iterations', required=False, type=int)
parser.add_argument('-l','--logfile',help='Logfile', required=False, type=int)
args = parser.parse_args()

src = args.input_file
dst = args.output_folder
rep = args.repeat
slp = args.sleep
logfile = args.logfile

tmp_dir = tempfile.gettempdir()
timeDeltaTotal = 0
sumSeconds = 0
sumBits = 0

# Test for the output folder
# This test doesn't work. Even when it says "True" I get errors on folder I know I can't write too.
if not isWritable(dst):
    print('Destination path ' + os.path.dirname + ' is not writable. Pick a directory you can write to.')
    quit()

# Get the size of the file.
SrcSize = os.path.getsize(src)
# Do some conversions
sizeBytes = SrcSize
sizeBits = SrcSize * 8.0
#   These next two are an area of concern. When I calculdate/convert Bytes from "getsize"
#   using 1024**2 the difference between Megabytes is significantly different
#   than the sizeBytes. For example, sizeBytes will show "99,999,744" and
#   the sizeMB will show "95 MB"; 5% difference. I'm using 998**2 to fudge it for now.
sizeMB = round(SrcSize / 998**2,0)
sizeMb = sizeBits / 998**2

print("Copying " + src + " (" + str(sizeMB) + " MB) to " + dst)
# Start the copy and timing.

for x in range(rep):
    src = args.input_file
    print 'Iteration: ' + str(x),
    output = tempfile.NamedTemporaryFile(dir = dst, delete = False)
    StartTime = datetime.datetime.now()
    shutil.copyfile(src, output.name)
    StopTime = datetime.datetime.now()

    # Get the difference between start/stop and convert to seconds.
    TimeDelta = StopTime - StartTime
    TimeDelta2 = TimeDelta.seconds + (TimeDelta.microseconds * .000001)

    # Determine copy speed.
    Mbps = round(sizeMb / TimeDelta2,3)
    MBps = round(sizeMB / TimeDelta2,3)

    # Print the results
    print(str(Mbps) + ' Mbps. TimeDelta = ' + str(TimeDelta2))

    sumSeconds = sumSeconds + TimeDelta2
    for s in range(slp):
        pass

    del src

##        time.sleep(1)

print("-"*80)
print "Total seconds for copy time: " + str(sumSeconds)
print "File Size: " + str(sizeMB) + "(MB), " + str(sizeMb) + "(Mb)"
