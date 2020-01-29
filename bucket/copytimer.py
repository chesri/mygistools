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
        testfile = tempfile.TemporaryFile(dir = path)
        testfile.close()
    except OSError as e:
        if e.errno == errno.EACCES:  # 13
            return False
        e.filename = path
        raise
    return True

parser = argparse.ArgumentParser(description='sends a 100MB file',usage='copytimer.py -i <file_to_send>')
parser.add_argument('-o','--output_folder',help='Output folder path', required=True)
parser.add_argument('-r','--repeat',help='Number of times to copy', required=False, type=int)
parser.add_argument('-s','--sleep',help='Seconds to sleep between iterations', required=False, type=int)

args = parser.parse_args()
dst = args.output_folder
rep = args.repeat
slp = args.sleep

timeDeltaTotal = 0

# Test for the output folder
# This test doesn't work. Even when it says "True" I get errors on folder I know I can't write too.
if not isWritable(dst):
    print('Destination path ' + os.path.dirname + ' is not writable. Pick a directory you can write to.')
    quit()

# create a 100MB file to send
f = tempfile.NamedTemporaryFile(delete=False)
for x in range(0,1000000):
    f.write('X'*100)
src = f.name
f.close

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
    print ('Iteration: ' + str(x))
    StartTime = datetime.datetime.now()
    shutil.copy(src, dst)
    StopTime = datetime.datetime.now()

    # Get the difference between start/stop and convert to seconds.
    TimeDelta = StopTime - StartTime
    TimeDelta2 = TimeDelta.seconds + (TimeDelta.microseconds * .000001)

    # Determine copy speed.
    Mbps = round(sizeMb / TimeDelta2,3)
    MBps = round(sizeMB / TimeDelta2,3)

    # Print the results
    print("{:,}".format(sizeBits) + ' bits sent.')
    print("{:,}".format(sizeBytes) + ' Bytes sent.(' + str(sizeMB) + ' MB)')
    print(str(MBps) + ' MBps.')
    print(str(Mbps) + ' Mbps.')
    print(str(TimeDelta2) + '(sec) elapse time.')

    timeDeltaTotal = timeDeltaTotal + TimeDelta2
    print "sleeping " + str(slp) + " seconds.",
    for s in range(slp):
        time.sleep(1)
        print ".",
    print "."

print("-"*80)
avgMbps = timeDeltaTotal / rep
sumMbps = round(sizeMb / avgMbps,3)
print("Summary: " + str(sumMbps) + " Mbps")
# Delete the temporary file
del f
##os.remove(src)