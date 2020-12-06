#
# secret_code.py
#

input_string = input('Message : ')
l = []

for el in input_string:
    l.append(chr(ord(el)+1))
l.reverse()
print(''.join(l))