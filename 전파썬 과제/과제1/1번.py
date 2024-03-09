#1번
a=int(input('1~6중 하나의 숫자를 입력하세요=>'))
b=int(input('금액을 입력하세요=>'))
import random
c=random.randint(1,7)

if (a+c)%2==0: 
  print('입력값 :',a,'\n뽑힌값 :',c, '\n금액 :',2*b)
  if a==c: 
    print('입력값 :',a,'\n뽑힌값 :',c, '\n돈을 반환하지 않습니다.') 
else: print('입력값 :',a,'\n뽑힌값 :',c, '\n돈을 반환하지 않습니다.')

