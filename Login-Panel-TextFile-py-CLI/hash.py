def hashing(encrypt):
  x= hashlib.md5(encrypt.upper().encode())
  hex_key = x.hexdigest()
  return hex_key
