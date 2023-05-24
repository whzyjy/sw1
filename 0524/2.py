score=[]
f=open("C:/data/score1.txt","r")

for i in range(10):
    score.append(f.readline().split())

for j in range(10):
    score[j][i]=float(score[j][i])

    if score[j][i]>=90:
       score[j].append("A")
    elif score[j][i]>=80:
        score[j].append("B")   
    elif score[j][i]>=70:
        score[j].append("C")      
    else: 
        score[j].append("D")

for i in range(10):
    print("{:<5}{:<5}".format(score([i][0]),score[i][2]))
f.close()