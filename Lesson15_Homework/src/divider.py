#
# divider.py
#

import sys

print("Dividing 10 by an integer")
while True:
    try:
        inp = input("Provide an integer: ")
        if not inp:
            sys.exit()
        a = int(inp)
        print(str(10/a))
    except ValueError:
        print("Your input must be an integer")
    except ZeroDivisionError:
        print("Your input must not be zero (0)")
        