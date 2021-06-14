#!/usr/bin/python3
import sys
import json
from jwcrypto import jwt,jws

key = jwt.JWK()
            
try:
   with open("jwt.pub", "rb") as key_file:
      key_data = key_file.read()
   with open("jws.json") as cf:
      jws_data = cf.read()
except Exception as e:
      print("Error loading key file: %s" % str(e), file=sys.stderr)
      exit(1)
key.import_from_pem(key_data)
jwstoken = jws.JWS()
jwstoken.deserialize(jws_data)
try:
   jwstoken.verify(key)
except:
   print("FAILED - Invalid signature", file=sys.stderr)
   exit(1)
payload = jwstoken.payload

print(payload.decode("utf-8") )
