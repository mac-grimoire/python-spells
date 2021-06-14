#!/usr/bin/python3
import sys
from jwcrypto import jwt,jwe

key = jwt.JWK()
            
try:
   with open("jwt.pub", "rb") as key_file:
      key_data = key_file.read()
   with open("claims.json") as cf:
      payload = cf.read().rstrip('\n')
except Exception as e:
      print("Error loading key file: %s" % str(e), file=sys.stderr)
      exit(1)
key.import_from_pem(key_data)

protected_header = {
   "typ": "JWE",
   "alg": "ECDH-ES+A256KW",
   "enc": "A256CBC-HS512",
   "kid": key.thumbprint(),
}

jwetoken = jwe.JWE(payload.encode('utf-8'),recipient=key,protected=protected_header)
enc = jwetoken.serialize()
print(enc)
