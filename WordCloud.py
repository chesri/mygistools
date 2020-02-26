#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     04/02/2020
# Copyright:   (c) chrism 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

words = {'AGC':2440.07,'JSOC ':	89.25,'SRP ':	621.25,'USACE':	15.75,'DEVGRU':	343.5,'TSMO ':	53.93,'USACE':	502,'AZNG':	3047.53,'USACE':	303.25,'DEVGRU':	281,'SRP ':169.25,'JSOC':	374.5,'TSMO':	4731.11,'USACE':	495.5,'DCSG-9':	1482.09,'MING': 65,'NCNG': 258,'SOCOMHQ': 829.84,'10thSpecialForces':379.75,'64thGPC':310.75,'USSOCOMJ3I':522.5,'USACE':515.79,'USACE':430.51,'USAF':1266,'UTNG':349.75}

for customer in words.keys():
    for i in range(int(words[customer]/2)):
        print(customer)