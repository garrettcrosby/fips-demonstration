import hashlib
import sys

password = b"supersecretpassword"

try:
    h = hashlib.md5(password)
    print(f"MD5 hash: {h.hexdigest()}")
except Exception as e:
    print(f"FAILURE: {e}", file=sys.stderr)
    print("Unable to use md5", file=sys.stderr)
    sys.exit(1)
