'''
문제정의
    1~입력받은 숫자까지의 합게 구하기
문제분석
    변수
알고리즘
'''
num=int(input())
total=0

for i in range(1,num+1):
    total=total+i

print(''.format(num,total))