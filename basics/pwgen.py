#!/usr/bin/env python3

import argparse
import random
import string
import sys
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

class NoClassSpecifiedError(Exception):
  pass

def password_generator(values,length):
  components = list(values)
  random.shuffle(components)
  password = random.choices(components, k=length)
  password = ''.join(password)
  return password

parser = argparse.ArgumentParser(description='Password Generator')

parser.add_argument('-c', '--chars', action='store_true', help="include characters")
parser.add_argument('-d', '--digits', action='store_true', help="include digits")
parser.add_argument('-p', '--punctuation', action='store_true', help="include punctuation")
parser.add_argument('-l', '--length', type=int, default=16, help="lenght of the random password - 16 if omitted")

args = parser.parse_args()

if args.chars:
  letters = string.ascii_lowercase + string.ascii_uppercase
else:
  letters=''
if args.digits:
  digits = string.digits
else:
  digits = ''
if args.punctuation:
  punctuation = string.punctuation
else:
  punctuation = ''

values = f'{letters}{digits}{punctuation}'

try:
  if len(values)==0:
    raise NoClassSpecifiedError
  else:
    password=password_generator(values,args.length)
  print(password)
except NoClassSpecifiedError:
    log.error("\nERROR: You didn't specify any item class for the password to be generated (characters,digits,punctuations)\n")
    sys.exit(1)
