#
# multuple.py
#

#((1, 1), (2, 3), (3, 4))
#((1, 1), (2, 2), (12, 13), (4, 4))


#using a tuple to store the input treated
t = []
in_tup = input("\n")

#using a dict d to output easily with a good format
d = {}

i=0
while i<len(in_tup):
    #testing if one element and his next are digits if ok, store them in tuple t
    if in_tup[i].isdigit() and in_tup[i+1].isdigit():
        t.append(in_tup[i]+in_tup[i+1])
        i+=2
    if in_tup[i].isdigit():
        t.append(in_tup[i])
        i+=1
    i+=1

#this loop calculates the results and stores them in dict d, the key being the results of multiplying
i=0
while i<len(t):
    d[int(t[i])*int(t[i+1])] = (t[i], t[i+1])
    i+=2

#loop that outputs with the format needed
for k, val, in d.items():
    print("{0:3d}  =  {1:2s} x {2:3s}".format(k, val[0], val[1]))


#this was another temptation but not satisfying
"""
i=0
while i<len(t):
    print("{res}  =  {fel} x  {sel}".format(res=int(t[i])*int(t[i+1]), fel=t[i], sel=t[i+1]))
    i+=2  
print("\n"*2)
"""

                    