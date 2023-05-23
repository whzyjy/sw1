enter=[]

f=open("c:/data/out.txt","w")

while True:
    text=input(":")
    if text=='':
        break
    enter.append(text)
f.writelines(enter)
f.close()

print("out",enter)
print("out.txt")