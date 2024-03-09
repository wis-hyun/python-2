#사용자 입출력

#1
a=int(input('점수를 입력하세요 :'))

if a>=90:
    print('수')
elif 80<=a<90: print('우')
elif 70<=a<80: print('미')
elif 60<=a<70: print('양')
else: print('가')

#2
b=int(input('연도를 입력하세요 : '))

if (b%4==0 and b%100 !=0)or(b%400==0): print('윤년')
else: print('윤년이 아닙니다.')

#3
import random
a=random.randint(1,10)

if a%2==0: print('짝수')
else: print('홀수')

#4
import random
b=['봄','여름','가을','겨울']
random.shuffle(b)
print(b[0])

#5
import random
a=random.randint(1,3)
b=int(input('1부터 3중에서 하나의 숫자를 입력하세요 : '))

if a==b: print('승리')
else: print('패배')
