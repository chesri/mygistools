#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     02/05/2019
# Copyright:   (c) chrism 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import logging
import os, sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('sample.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

class testMe:

    myParentname = sys._getframe().f_code.co_name
##    myname = cls.__name__

##    @classmethod
##    def whoAmI(cls):
##        print cls.myname

    def printMe(self):
        ##print 'test'
        ##print sys._getframe().f_code.co_name
##        help(self)
        help(self)
        print sys._getframe().f_code.co_name
        print self.__class__.__name__
        print self.myParentname


tm = testMe()
tm.printMe()