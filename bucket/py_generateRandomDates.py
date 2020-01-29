#-------------------------------------------------------------------------------
# Name:        py_generateRandomDates.py
# Purpose:
#
# Author:      chrism
#
# Created:     25/10/2019
# Copyright:   (c) chrism 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random, datetime
####from datetime import datetime, timedelta, date
##
##def formatDateTime(in_date,in_time,addday=0):
##    r_date = datetime(int(in_date.split("/")[2]),int(in_date.split("/")[0]),int(in_date.split("/")[1])+addday,int(in_time.split(":")[0]),int(in_time.split(":")[1]),int(in_time.split(":")[2]))
##    return r_date, str(r_date.strftime('%m/%d/%Y %H:%M:%S'))
##
##def getnewDate(in_date):
##    tdelta = datetime.datetime.now() - in_date
##    new_tor = datetime(tdelta.year, tdelta.month, tdelta.day, tdelta.hour)
##    return tor
##
##def todayPlusDays():
##
##    return new_tor


def newDT():
    rn = random.randint(0,56)
    d = datetime.datetime.now( )
    d += datetime.timedelta(days=rn)

    if d.isoweekday() > 5:
        d += datetime.timedelta(days= random.randint(2,5))

    return d.strftime('%m/%d/%Y')

for i in range(0,5):
    print(newDT())

##from_date_input = "10/25/2019 14:47:00".split(" ")
##to_date_input = "12/20/2019 23:47:00".split(" ")
##
##fd, from_date = formatDateTime(from_date_input[0],from_date_input[1],0)
##td, to_date = formatDateTime(to_date_input[0],to_date_input[1],0)
##
##delta_days = td-fd
##delta_days = delta_days.days
##random_days = random.randint(0,delta_days)
##
##print(fd + timedelta(days=random_days))

##print("{} -> {}, ({})".format(td,fd,delta_days))
