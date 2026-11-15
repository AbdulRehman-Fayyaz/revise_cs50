
# this will write the below code to a file named name.py

import sys
print(len(sys.argv))
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("Hello, my name is", sys.argv [1])
