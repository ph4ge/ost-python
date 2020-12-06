import string, sys
try:
    f = open(sys.argv[1], "r").read()
    sp = tuple(string.punctuation)
    word_lst = f.split()
    word_lst_dict = {}
except:
    print("Problem occurred !")
    raise

for el in word_lst:
    x=0
    for e in el:
        if e in sp:
            x+=1
    #this condition is for avoiding  len == 1 punctuation to get in dict       
    if el not in sp:        
        word_lst_dict[len(el)-x] = word_lst_dict.get(len(el)-x, 0) + 1
        
for i, el in enumerate(sorted(word_lst_dict.items()), start=1):
    print(i, word_lst_dict[i])
    
print("\n"*2)
#print(len(word_lst_dict),"\n")
#print(word_lst_dict)
r= []
for el in range(0, 420, 20):
    r.append(el)
r.reverse()

t, tt=[], []
dd = {}
for i, el in enumerate(sorted(word_lst_dict.items()), start=1):
    t.append(round(word_lst_dict[i]/20))
    tt.append(round(word_lst_dict[i]/20))
    dd[i]=round(word_lst_dict[i]/20)

t.sort()
t.reverse()
t.insert(0,1)

i=13
j=260

while i>=0:
    if i in t and i!=1 and i==13:
        #print("{0:4s}{1:1s}{x}".format(str(j),'|', x='**'*t.index(i)))
        print("{0:4s}{1:1s}{x}".format(str(j),'|', x='***'*t.count(i)))
    elif i in t and i!=1:
        print("{0:4s}{1:1s}{x}".format(str(j),'|', x='***'*t.index(i)))
    i-=1
    j-=20

print("{0:4s}{1:3s}{2:3s}{3:3s}{4:3s}{5:3s}{6:3s}{7:3s}{8:3s}{9:3s}{10:3s}{11:3s}".format('', '+', str(2), str(3), str(4), str(5), str(6), str(7), str(8), str(9), str(10), str(11)))


