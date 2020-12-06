#
# input_counter.py
#

d = {}
k = set()
kl = 0

while True:
    s = input("Enter text: ")
    l = s.strip().split()
    if not s:
        print("Finished")
        break
    for el in l:
        k.add(el)
        if len(k) != kl:
            kl = len(k)
            d[el] = kl
    for el in d.items():
        print(el[0], el[1])