#!/usr/bin/env python3
from carcano.foolist import *

import os
import logging
import logging.config

log_config_paths = [ os.path.dirname(os.path.realpath(__file__))+'/logging.conf', '/etc/fooapp/logging.conf' ]

log_enabled = False

for log_config_file in log_config_paths:
    if os.path.isfile(log_config_file):
        log_enabled = True
        break
if log_enabled == True:
    logging.config.fileConfig(fname=log_config_file, disable_existing_loggers=False)
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
if log_enabled == True:
    logging.info(__file__+': finished')
