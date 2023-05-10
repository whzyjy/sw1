'''
문제정의
    입력받은 숫자가 소수인지 안니지 판별하는 프로그램
문제분석
    변수-숫자
알고리즘
    1.변수 초기화
    num에 정수 입력
    2.논리(층첩)
       (반복) for i in range(1,num+1):
          (반복)  for j in range(1,i+1):
'''

num=int(input(":"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
print("\n")   


num=int(input(":"))
for j in range(1,num+1):
    for i in range(1,i-1):
    
        print("*",end="")
    print()
print("\n")  