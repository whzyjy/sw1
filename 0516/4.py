f=open("C:/data/text.txt","r")

print(f.read(10),end='')
print(f.read(10),end='')
print(f.read(10))

f.seek(0)

print(f.read(10),end='')
print(f.read(10),end='')
print(f.read(10))

f.close()
