f=open("c:/data/stu.txt","w")
while True:
    score=f.readline()
    if score=='':
        break
    
    scorelist=score.split()
    name=scorelist[0]
    sum=0
    for i in range(1,4):
        sum=sum+int(scorelist[i])

    print(name+":"%sum/3)
f.close()