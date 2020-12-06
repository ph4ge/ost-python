#
# guessing_game.py
#

import random

x = random.randint(1, 99)
i=0
while True:
    user_input = input("Guess a number: ")
    if int(user_input)<x:
        print("too low")
    elif int(user_input)>x:
        print("too high")
    else:
        print("You guessed it!\n")
        break
print("Secret number: "+str(x))