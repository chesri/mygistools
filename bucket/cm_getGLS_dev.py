#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     10/08/2017
# Copyright:   (c) chrism 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math

lon, lat = -81.596257,36.304309
#lon, lat = -80.817719,35.048684
alpha = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
number = ('01234567890123456789')
gls_result = []

x = 0
for a in range(-180,180,20):
    print a,
    if lon > a:
        first = alpha[x]
        one = a
    x = x + 1
gls_result.append(first)
print "\n"

# SECOND CHARACTER (1st LATITIDE)
x=0
for b in range(-90,90,10):
    print b,
    if lat > b:
        second = alpha[x]
        two = b
    x = x + 1
gls_result.append(second)
print "\n"

# THIRD CHARACTER (2nd LONGITUDE, degrees 1-20) -20_0_20
if one < 0:
    one = one + 20
tmp3rd = int(math.fmod(lon,one))

x=0
for c in range(-20,20,2):
    print c,
    if int(lon) == c and lon < 0:
        third = number[x - 1]
    if int(lon) == c and lon > 0:
        third = number[x + 1]
    elif tmp3rd > c:
        third = number[x]

        x = x + 1
gls_result.append(third)
print "\n"

# FOURTH CHARACTER (2nd LATITUDE, degrees 1-10) -10_0_10
if two < 0:
    two = two + 10
tmp4th = abs(int(math.fmod(lat,two)))
x=0
for d in range(-10,10,1):
    print d,
    if tmp4th >= d:
        fourth = number[x]
    x = x + 1
gls_result.append(fourth)

print("\n")
print(gls_result)

##def fetchGLS(lat, lon):
##    first = {(-180,-160):'A',(-160,-140):'B',(-140,-120):'C',(-120,-100):'D',(-100,-80):'E',(-80,-60):'F',(-60,-40):'G',(-40,-20):'H',(-20,0):'I',(0,20):'J',(20,40):'K',(40,60):'L',(60,80):'M',(80,100):'N',(100,120):'O',(120,140):'P',(140,160):'Q',(160,180):'R'}
##    second = {(-90,-80):'A',(-80,-70):'B',(-70,-60):'C',(-60,-50):'D',(-50,-40):'E',(-40,-30):'F',(-30,-20):'G',(-20,-10):'H',(-10,0):'I',(0,10):'J',(10,20):'K',(20,30):'L',(30,40):'M',(40,50):'N',(50,60):'O',(60,70):'P',(70,80):'Q',(80,90):'R'}
##    third = {(-20,-18):'0',(-18,-16):'1',(-16,-14):'2',(-14,-12):'3',(-12,10):'4',(-10,-8):'5',(-8,-6):'6',(-6,-4):'7',(-4,-2):'8',(-2,0):'9',(20,18):'9',(18,16):'8',(16,14):'7',(14,12):'6',(12,10):'5',(10,8):'4',(8,6):'3',(6,4):'2',(4,2):'1',(2,0):'0'}
##
##    for l in lat:
##        if f[0] < frequency < f[1]:
##            return frequencies[f]

#print fetchBand(442.29)