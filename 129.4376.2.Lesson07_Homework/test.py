f = open('v:/example.txt', 'w')
f.write("my text")
f.close()

f = open('v:/example.txt', 'r')
print(f.read())
