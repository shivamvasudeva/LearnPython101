f = open("pythontest.txt")
#print (f.tell()) # Tells where the handler is

print(f.readline())
print(f.readline())

f.seek(3)
print(f.readline())
f.close()
#print (f.tell())