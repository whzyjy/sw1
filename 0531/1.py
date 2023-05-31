import random
num=[]
for i in random(10):
    num.append(random.randint(1,100))
print(":",num)
print(":",max(num))
print(":",min(num))
print(":",sum(num))
num.sort()
print(":",num)
num.sort(reverse=True)
print(":",num)