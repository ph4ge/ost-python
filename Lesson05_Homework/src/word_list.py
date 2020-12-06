#
# word_list.py
#

upc_list, noupc_list  = [], []

in_s = input("Input your text : ")
in_s = in_s.strip().split()

for el in in_s:
    if not el.islower():
        upc_list.append(el)
    else:
        noupc_list.append(el)
        
upc_list = upc_list + noupc_list

for el in upc_list:
    print(el)