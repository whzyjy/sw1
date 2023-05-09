num=int(input(":"))
sum=0
i=0

while i<=100:
    i=i+1
    if i%num !=0:
        continue
    sum=sum+i

print("".format(num,sum))