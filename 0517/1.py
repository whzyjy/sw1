with open("C:/data/linetest.txt","r") as f:
    for line in f:
        print(line,end='')


print()

with open("C:/data/linetest.txt","r") as f:
    while True:
        line=f.readline()
        print(line,end='')

        if line=='':
            break
        
#readlines():한 줄씩 읽어서 리스트형으로 반환
with open("C:/data/linetest.txt","r") as f:
    textlists=f.readlines()
    print(type(textlists))
    print(textlists)

#print()
f=open("C:/data/ptest.txt","w")

print("aaaaaaa",file=f)
print("bbbbbbb",file=f)
print("ccccccc",file=f)

f.close()
