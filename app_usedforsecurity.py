# A variation of our standard app that will work on FIPS crypto.
# This is because we set the usedforsecurity param, which tells 
# openssl to call the base provider and not the fips provider.
# The base provider is out of boundary, and has md5 available.

import hashlib
import sys

password = b"supersecretpassword"

try:
    h = hashlib.md5(password, usedforsecurity=False)
    print(f"MD5 hash: {h.hexdigest()}")
except Exception as e:
    print(f"FAILURE: {e}", file=sys.stderr)
    print("Unable to use md5", file=sys.stderr)
    sys.exit(1)
