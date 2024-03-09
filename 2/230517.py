#1
import math

b=int(input('삼각형의 밑변의 길이를 입력하시오->'))
a=int(input('삼각형의 높이의 길이를 입력하시오->'))
c=math.sqrt(a*a+b*b)
al = math.acos(b/c)
al = math.degrees(al)
be = math.acos(a/c)
be= math.degrees(be)
print(al,be)

#2
import sys
option = sys.argv[1]
if option == '-a':
    memo=sys.argv[2]
    f=open('memo.txt', 'a')
    f=write(memo)
    f=write('\n')
    f.close()
elif option == '-v':
    f=open('memo.txt')
    memo=f.read()