phone=dict()

for i in range(5):
    id=int(input(str(i+1)+"***:"))
    pnum=input(str(i+1)+"***:")

    phone[p]=pnum
print("****")
id=int(input("**:"))

if id in phone:
    print("***:",phone[id])
else:
    print("***:")