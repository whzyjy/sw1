def dnumber(num,num_list):
    for i in range(1,num+1):
        if num%i==0:
            num_list.append(i)

num=int(input("**:"))
num_list=[]

if num>0:
    dnumber(num,num_list)
    print(num,"***",num_list)
else:
    print("****")