#
# inputter.py
#

f_w = open('v:\exone.txt', 'a')
f_w.close()

f_r = open('v:\exone.txt', 'r').readlines()
if f_r:
        for el in f_r:
            print(el)

while True:
    input_string = input('Enter text : ')
    if not input_string:
        break
    if input_string:
        f_w = open('v:\exone.txt', 'a')
        f_w.write(input_string)
        f_w.close()
        f_r = open('v:\exone.txt', 'r').readlines()
        if f_r:
            for el in f_r:
                print(el)