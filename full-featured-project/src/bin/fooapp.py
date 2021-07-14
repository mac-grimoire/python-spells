#!/usr/bin/env python3
from carcano.foolist import *

import os
import logging
import logging.config

def configureLogging():
    try:
        configfile=os.path.dirname(os.path.realpath(__file__))+'/logging.conf'
        logging.config.fileConfig(fname=configfile, disable_existing_loggers=False)
    except FileNotFoundError:
        configfile = '/etc/fooapp/logging.conf'
        logging.config.fileConfig(fname=configfile, disable_existing_loggers=False)
        pass

configureLogging()
logger = logging.getLogger(__name__)

logging.info(__file__+': started')
d = Foolist()
d.append('RedHat',True)
d.append('Suse',True)
d.append('CentOS',False)
print("Print the list:")
for l in d:
    print(l)
print("Print the list in ascending order:")
for l in sorted(d):
    print(l)
d.remove('CentOS')
d.append('Rocky Linux',False)
print("Print the list - after the removal of CentOS:")
for l in d:
    print(l)

print("Print the list in descending order:")
for l in sorted(d,reverse=True):
    print(l)
logging.info(__file__+': finished')
