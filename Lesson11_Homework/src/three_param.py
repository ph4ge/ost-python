#
# three_param.py
#

def my_func(a, b="b was not entered", c="c was not entered"):
    print(" {0}\n {1}\n {2}\n".format(a, b, c))

my_func("test")
my_func("test", "test")
my_func("test", "test", "test")
print(my_func)