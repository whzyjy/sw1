import random
with open("C:/data/num.txt","w") as f:
    for i in range(5):
        for j in range(5):
            f.write(str(random.randint(1,100)))
            f.write('')
        f.write("\n")
with open("C:/data/num.txt","r") as f1:
     with open("C:/data/avg.txt","r") as f2:
         j=0
         while True:
             j=j+1
             score=f1.readline()
             if score=='':
                 break
             scorelist=score.split()

             sum=0
             for i in range(5):
                 sum=sum+int(scorelist[i])
             print(j,":",sum/5,file=f2)