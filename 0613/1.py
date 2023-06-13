def findmax(a,b,c):
    if a>b:
        biggist=a
    else:
        biggist=b

    if biggist<c:
        biggist=c
    
    return biggist
num1=int(input("**1:"))
num2=int(input("**2:"))
num3=int(input("**3:"))

biggist_number=findmax(num1,num2,num3)

print("******",biggist_number)
