num= [[20001,20002,20003,20004,20005],[89,74,88,99,95],[91,75,68,98,88],[79,94,68,94,92]]

j=0

for i in range(len(num[0])):
    print(num[j][i],"****",num[j+1][i]+num[j+2][i]+num[j+3][i])