'''#알고리즘
     1.현덤모들 추가
     2.비어있는 세트 변수
     '''
import random

num1=set()
num2=set()

while True:
    if len(num1)<10:
        num1.add(random.randint(1,100))
    if len(num2)<10:
        num2.add(random.randint(1,100))
    if len(num1)==10 and len(num2)==10:
        break
print("****",num1)
print("****",num2)

print("***",num1|num2)
print("***",num1&num2)
print("***",num1-num2)