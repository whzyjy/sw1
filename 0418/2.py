score1=int(input("접수1"))
score2=int(input("접수2"))
total=score2+score1

if (score1)>=75 & (score2)>=75:
     if(total)>=180:
          print("최우수")
     elif(total)>=160:
          print("우수")
     else:
          print("보통")
else:
     print("분발")
     