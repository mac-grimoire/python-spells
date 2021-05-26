#!/usr/bin/env python3
from carcano.ansibleinventory import *

import os
import yaml
import logging
import logging.config
import argparse

parser = argparse.ArgumentParser(description='Create a YAML formatted Ansible Inventory')

parser.add_argument('-l', '--log-config-file', action='store', help='Path to the file configuring the logging subsystem', dest='logging_configurationfile', type=str)

args = parser.parse_args()


def configureLogging(configfile):
    try:
        if not configfile:
            configfile=os.path.dirname(os.path.realpath(__file__))+'/ansible_inventory_logging.conf'
        logging.config.fileConfig(fname=configfile, disable_existing_loggers=False)
    except:
        if configfile==os.path.dirname(os.path.realpath(__file__))+'/ansible_inventory_logging.conf' :
            # enable logging is only an optiononal feature, not enough to give up
            pass
        else:
            raise FileNotFoundError(configfile+" does not exists")

ntp=['ntp1.carcano.local', 'ntp2.carcano.local', 'ntp3.carcano.local']
dns=['172.16.10.11','172.16.11.11','172.16.10.12','172.16.11.12']
dns_search=['test.carcano.local","test.carcano.local','carcano.local']

configureLogging(args.logging_configurationfile)
logger = logging.getLogger(__name__)
try:
    logging.info(__file__+': started')
    i=Inventory()
    logging.debug(__file__+': gathering inventory information')
    # __placeholder __ insert here the code to fetch inventory data from external sources
    # the following code is only as an example 
    i.setVar('ntp_servers',ntp)
    i.setVar('dns_servers',dns)
    i.setVar('dns_search',dns_search)
    i.addGroup(Group('www_dc1_t1'))
    i.addGroup(Group('dc1_t1'))
    i.getGroupByName('dc1_t1').addGroup(i.getGroupByName('www_dc1_t1'))
    i.getGroupByName('www_dc1_t1').setVar('cluster_description','WWW Cluster Datacenter 1 Test 1')
    i.getGroupByName('www_dc1_t1').setVar('cluster_name','www_dc1_t1')
    i.getGroupByName('www_dc1_t1').setVar('environment','test')
    i.getGroupByName('www_dc1_t1').setVar('domain','carcano.local')
    #i.addHost(Host('www_dc1_t1.test.carcano.local'),i.getGroupByName('www_dc1_t1'))
    i.addHost(Host('www_dc2_t1.test.carcano.local'))

    logging.debug(__file__+': serializing inventory in YAML format')
    print (yaml.dump(i.raw(), default_flow_style=False))
    logging.info(__file__+': ended succesfully')
except ValueError as v:
    logging.error(v)
    logging.error(__file__+': ended with errors')
    exit(1)
