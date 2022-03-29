import sys
from getopt import getopt

opts, args = getopt(sys.argv[1:], "f:m:t:")

print(f"args are {args}")
print(f"optional args are {dict(opts)}")