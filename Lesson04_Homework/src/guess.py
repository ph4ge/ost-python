#
# guess.py
#

secret = 13
i = 4
while i>=0:
    i-=1
    in_s = input("Guess a number :")
    if int(in_s) < secret:
        print("Guess lower")
    elif int(in_s) > secret:
        print("Guess higher")
    elif int(in_s) == secret:
        print("Correct! Well done, the number was ",secret)
        i=7
        break
if i!=7:
    print("Sorry, the number was ",secret)