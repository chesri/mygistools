#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     03/05/2019
# Copyright:   (c) chrism 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import logging, tempfile
import logging.handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  ## change to suit your needs. DEGUG, INFO, WARNING, ERROR, CRITICAL

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')   ## https://docs.python.org/3/library/logging.html#logrecord-attributes
logfile = tempfile.mktemp(suffix=".log")

file_handler = logging.handlers.RotatingFileHandler(logfile,maxBytes=50000)
#file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# send message to console, just like print
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.info("Log file: {}".format(logfile))

def main(message):
    # Use logger like print, the "stream_handler" will send message to screen at
    # same time it sends to file via file_handler.

    logger.debug(message + ' DEBUG' + ' ' + str(logging.DEBUG))    ##    logger.debug(msg, *args, **kwargs)
    logger.info(message + ' INFO' + ' ' + str(logging.INFO))      ##    logger.info(msg, *args, **kwargs)
    logger.warning(message + ' WARNING' + ' ' + str(logging.WARNING)) ##    logger.warning(msg, *args, **kwargs)
    logger.critical(message + ' CRITICAL' + ' ' + str(logging.CRITICAL)) ##    logger.critical(msg, *args, **kwargs)

    ##    logger.exception(msg, *args, **kwargs)
    #logger.exception(message + ' EXCEPTION' + ' ' + str(logging.EXCEPTION))
    ##    logger.log(level, msg, *args, **kwargs)
    logger.log(1, message + ' 1')

if __name__ == '__main__':
    message = 'This is my logger test message.'
    main(message)

##for lev in logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL:
##    logger.setLevel(lev)
##    print(lev, logger.level)