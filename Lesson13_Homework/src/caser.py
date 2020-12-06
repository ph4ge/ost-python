#
# caser.py
#

import sys

def capitalize(s):
    return s.capitalize()

def title(s):
    return s.title()

def upper(s):
    return s.upper()

def lower(s):
    return s.lower()

def exit():
    sys.exit()

d = {'capitalize':capitalize, 'title':title, 'upper':upper, 'lower':lower, 'exit':exit}

while True:
    inp = input("Enter a function name : ({0})".format(', '.join(d.keys())))
    if inp in d and inp != 'exit':
        inp2 = input("Enter a string:")
        print(d[inp](inp2))
    else:
        print("Goodbye for now!")
        d[inp]()
        