#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      chrism
#
# Created:     15/08/2019
# Copyright:   (c) chrism 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os, sys, shutil, time
from datetime import datetime, timedelta

def timeDelta(begin_time, end_time):
    ##start_time = time.time()
    start_time = begin_time
    time.sleep(1)
    ##end_time = time.time()
    end_time = end_time

    uptime = end_time - start_time

    human_uptime = str(datetime.timedelta(seconds=int(uptime)))
    print human_uptime


## calculating time from Date field to a string/integer field.
from datetime import datetime
def makeit(input):
    dt = datetime.strptime(input, '%m/%d/%Y %H:%M:%S %p')
    return str(datetime.strftime(dt,"%H:%M:%S"))

#makeit(!receivedtime!)

timeDelta(datetime.strptime('9/14/2019 7:51:41 AM', '%m/%d/%Y %H:%M:%S %p'),datetime.strptime('9/14/2019 11:01:24 AM', '%m/%d/%Y %H:%M:%S %p'))