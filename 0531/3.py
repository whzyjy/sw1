num=(1,4,6,5,4,3,2,0,1,2,4,6,7,9,4,0)
num_list=[]

for i in range(len(num)):
  if num[i] not in num_list:
    num_list.append(num[i])
    print(num[i],'**',num.count(num[i]))