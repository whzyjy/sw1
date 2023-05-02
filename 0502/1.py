s='123'
ch1=int(s)
ch2=list(s)
ch3=tuple(s)
ch4=set(s)

print('{}의 자료은{}'.format(ch1,type(ch1)))
print('{}의 자료은{}'.format(ch2,type(ch2)))
print('{}의 자료은{}'.format(ch3,type(ch3)))
print('{}의 자료은{}'.format(ch4,type(ch4)))

print()
num1=abs(-5)
num2=round(4.6)
num3=bin(10)
str1=chr(97)
str2=ord('A')

print('-5의 :',num1)
print('4.6 :',num2)
print('10 :',num3)
print('9 :',str1)
print('A :',str2)

print()

num10=[6,3,5,1,9,2,8]
print('num10 원소의 길이:',len(num10))
print('num10 원소 중 가장 큰값:',max(num10))
print('num10 원소 중 작은 값:',min(num10))
print('num10 원소들의 합게:',sum(num10))
print('num10 원소들 정렬:',sorted(num10))

print()

zip('123',('kim','lee','part'))
print(list(zip('123',('kim','lee','part'))))
