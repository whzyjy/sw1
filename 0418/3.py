x=int(input("접수"))
y=int(input("접수"))

if (y!=0):
     if(x>y & y!=0):
          print("접수",x/y)
     elif(x<y):
          print("접수",x+y)
          
     elif(x==y):
          print("접수",x*y)
else:
     print("찰못")
     
