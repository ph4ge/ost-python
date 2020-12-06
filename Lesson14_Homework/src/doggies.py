#
# doggies.py
#
import sys

class Dog:
    
    def __init__(self, name , breed):
        self.name = name
        self.breed = breed

dogs = []

while True:
    inp = input("Name: ")
    if not inp:
        sys.exit()
    inp2 = input("Breed: ")
    a = Dog(inp, inp2)
    dogs.append(a)
    print("DOGS")
    for i, el in enumerate(dogs):
        print("{0}.  {1:12s}:{2:12s}".format(i, el.name, el.breed))
    if not inp and not inp2 :
        sys.exit()
    print("*"*52)