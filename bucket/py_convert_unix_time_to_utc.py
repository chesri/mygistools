#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     18/09/2019
# Copyright:   (c) chrism 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main(input):
    from datetime import datetime
    return datetime.utcfromtimestamp(int(input)/1000).strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    newdate = main('1568447501000')  # send unix/epoch time to main
    print newdate