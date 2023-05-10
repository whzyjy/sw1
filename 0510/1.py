'''
문제정의
    입력받은 숫자가 소수인지 안니지 판별하는 프로그램
문제분석
    변수-숫자
알고리즘
    1.변수 초기화
    num에 정수 입력
    2.논리(반복안에 선택포함)
'''
num=int(input(":"))
for i in range(2,num+1):
    if num%i==0:
        break
if num==1:
    print("".format)