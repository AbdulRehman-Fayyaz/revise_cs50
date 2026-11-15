
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
for a in sys.argv[1:]:
    print("Hello, my name is", a)
