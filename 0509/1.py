num1=int(input(":"))
num2=int(input(":"))
sum=0
temp=0

if num1>num2:
    temp=num1
    num1=num2
    num2=temp

i=num1
while i<=num2:
    sum=sum+i
    i=i+1

print("".format(num1,num2,sum))