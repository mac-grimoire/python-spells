#!/usr/bin/python3

import sys
import json
from jwcrypto import jwt,jwe

key = jwt.JWK()
            
try:
   with open("jwt.key", "rb") as key_file:
      key_data = key_file.read()
   with open("jwe.json") as cf:
      jwe_data = cf.read().rstrip('\n')
except Exception as e:
      print("Error loading key file: %s" % str(e), file=sys.stderr)
      exit(1)
key.import_from_pem(key_data)

jwetoken = jwe.JWE()
try:
   jwetoken.deserialize(jwe_data, key=key)
except:
   print("FAILED - Decryption failed", file=sys.stderr)
   exit(1)

payload = jwetoken.payload

print(payload.decode("utf-8") )

