""" Nested exception handling"""

def divide(a, b):
    """ Return result of dividing b by a """
    print("=" * 20)
    print("a: ", a, "/ b: ", b)
    try:
        return a/b
    except (ZeroDivisionError, TypeError):
            print("Something went wrong!")
            raise

if __name__ == "__main__":
    for arg1, arg2 in ((1, "string"), (2, 0), (123, 4)):
        try:
            print(divide(arg1, arg2))
        except Exception as msg:
            print("Problem: {0}".format(msg))
