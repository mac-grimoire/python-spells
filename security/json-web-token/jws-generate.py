#!/usr/bin/python3
import sys
from jwcrypto import jwt,jws
from jwcrypto.common import json_encode

key = jwt.JWK()
            
try:
   with open("jwt.key", "rb") as key_file:
      key_data = key_file.read()
   with open("claims.json") as cf:
      payload = cf.read().rstrip('\n')
except Exception as e:
      print("Error loading key file: %s" % str(e), file=sys.stderr)
      exit(1)
key.import_from_pem(key_data)

jwstoken = jws.JWS(payload.encode('utf-8'))
jwstoken.add_signature(key, None, json_encode({"alg": "ES384"}), json_encode({"kid": key.thumbprint()}))
sig = jwstoken.serialize()
print(sig)
