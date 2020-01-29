#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     08/08/2017
# Copyright:   (c) chrism 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def fetchBand(frequency):
    frequencies = {(3.525,3.6):'80 m',(7.025,7.125):'40 m',(21.025,21.2):'15 m',(28,28.5):'10 m',(50.1,54):'6 m',(144.1,148):'2 m',(222,225):'1.25 m',(420,450):'70 cm',(902,928):'33 cm',(1240,1300):'23 cm',(2.3,2.45):'13 cm'}
    for f in frequencies:
        if f[0] < frequency < f[1]:
            return frequencies[f]

print fetchBand(442.29)




##    frequencies = ['3.525,3.6','7.025,7.125','21.025,21.2','28,28.5','50.1,54','144.1,148','222,225','420,450','902,928','1240,1300','2.3,2.45']
##    bands = ['80 m', '40 m', '15 m','10 m','6 m', '2 m', '1.25 m', '70 cm', '33 cm', '23 cm', '13 cm']