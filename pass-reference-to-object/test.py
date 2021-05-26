#!/usr/bin/env python3
#
# Program that demonstrates that Python passes reference to objects
# as function arguments.
# dumbReverse fails because it does not take in account of this

import logging

#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def dumbReverse(arg):
   log.debug("entering dumbReverse function")
   log.debug("id arg={}".format(id(arg)))
   log.debug("id arg matches the id of months in main function")
   reverted=[]
   log.debug("id reverted={}".format(id(reverted)))
   i=len(arg)-1
   while i>=0:
      reverted.append(arg[i])
      i=i-1
   arg=reverted
   log.info("arg inside dumbReverse function")
   log.info("months={}".format(arg))
   log.debug("id arg={}".format(id(arg)))
   log.info("id arg changed - it matches the id of reverted:")
   log.debug("exiting dumbReverse function")

def reverse(arg):
   log.debug("entering reverse function")
   log.debug("id arg={}".format(id(arg)))
   log.debug("id arg matches the id of months in main function")
   reverted=arg[:]
   log.debug("id reverted={}".format(id(reverted)))
   arg.clear()
   i=len(reverted)-1
   while i>=0:
      arg.append(reverted[i])
      i=i-1
   log.info("months={}".format(arg))
   log.debug("id arg={}".format(id(arg)))
   log.info("id arg didnt change - it matches still the id of months in main function")
   log.debug("exiting ireverse function")


months = [ "Jan", "Feb", "Mar", "Apr", "Maj", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec" ]
log.info("This is the list we want to pass to a function that reverses it")
log.info("months={}".format(months))
log.debug("id months={}".format(id(months)))
dumbReverse(months)
log.info("Got back to main")
log.info("months={}".format(months))
log.info("SURPRISE: the list was reverted only inside the function - that's why this is the dumb version of the reverse function!")
reverse(months)
log.info("Got back to main")
log.info("months={}".format(months))
log.info("This time the list is inverted also in the main function")
