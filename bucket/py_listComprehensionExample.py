#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     23/02/2018
# Copyright:   (c) chrism 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##def list_doubler(lst):
##    doubled = []
##    for num in lst:
##        doubled.append(num*2)
##    return doubled

def list_doubler(lst):
    doubled = [num*2 for num in lst]

    return [num*2 for num in lst]


def long_words(lst):
    return [word for word in lst if len(word) > 5]

print list_doubler([12,4,202])

print long_words(['Chris','Esri','Charlotte','Treehouse'])


# dictionary comprehension
print {i : chr(65+i) for i in range(4)}

d = {(k, v): k+v for k in range(4) for v in range(4)}
print d