"""Program to split a sentence into words"""

s = input("Please enter a sentence: ")
while True:
    while s.startswith(" "):
        s = s[1:]
    pos = 0
    for c in s:
        if c == " ":
            print(s[:pos])
            s = s[pos+1:]
            print("rrrrrrrrrrrrr", s)
            break
        pos +=1
        print(pos)
    else:
        print(s)
        break