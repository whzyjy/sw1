sum=0
cnt=0
avg=0

while True:
    num=int(input(":"))
    cnt+=1
    sum+=num
    if sum>=1000:
        break
avg=sum/cnt

print(":"%sum,end="")
print(""%avg)