"""Accept format strings from the user and format fixed data."""
i = 42
r = 31.97
c = 2.2 + 3.3j
s = "String"
digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
d = {"Steve": "Holden", "Guido":"van Rossum", "Tim":"Peters", "l":"string", 1:"integer"} 
while True:
    fmt = input("Format string : ")
    if not fmt:
        break
    fms = "{"+fmt+"}"
    print("Fromat:", fms, "output:", fms.format(i, r, c, s, lst=digits, dct=d))
    