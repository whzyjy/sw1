import random
lotto=set()

cnt=0

while True:
    lotto.add(random.randint(1,45))
    cnt=cnt+1
    if len(lotto)==6:
        break
print('***',sorted(lotto))
print('***:',cnt-6)