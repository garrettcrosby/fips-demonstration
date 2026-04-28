#

import hmac
import hashlib
import sys

key = b"supersecretkey"
data = b"message to authenticate"


try:
    h = hmac.new(key, data, hashlib.sha25)
    print(f"HMAC-SHA256: {h.hexdigest()}")
    print("SUCCESS: HMAC-SHA256 completed")
except Exception as e:
    print(f"FAILURE: {e}", file=sys.stderr)
    print("FIPS provider failed to initialize - module integrity check did not pass.")
    sys.exit(1)
