#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     30/06/2017
# Copyright:   (c) chrism 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import inspect

##def currentLineNo():
##    frame = inspect.currentframe()
##    #return int(frame.f_lineno)
##    theLine = inspect.currentframe().frame.f_lineno
##    return theLine

if __name__ == '__main__':
    print "1"
    print "2"
    print inspect.currentframe().f_lineno


print inspect.currentframe().f_lineno




