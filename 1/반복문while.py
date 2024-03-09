#1번
'''
i=0

while i<=10:
    i+=1
    if i%2==0:
        print(i)
'''

#2번
'''
i=1 #i=0
result=0
while i<=10:
    #i+=1
    result+=i
    i+=1
print(result)
'''
#3번
'''
i=1
result=0

while i<=1000:
    if i%3==0:
        result+=i
    i+=1
print(result)
'''
#4번
'''
i=0

while i<=5:
    print('*'*i)
    i+=1
'''
#5번
'''
i=0

while i<=10:
    i+=1
    if i==4:
        continue
    if i%2==0:
        print(i)
'''
#6번

prompt = '''
1. add
2. quit

enter : 
'''

menu = '''
1.떡볶이(2500)
2.순대(2000)
3.튀김(3000)

enter :
'''

while True:
    print(prompt)
    pp=int(input())
    if pp==1:
        print(menu)
        mm=int(input())
        a=2500
        b=2000
        c=3000
        result=0
        if mm==1:
              a1=int(input('인분을 입력하세요!'))
              result+=a*a1
        if mm==2:
              b1=int(input('인분을 입력하세요!'))
              result+=b*b1
        if mm==3:
              c1=int(input('인분을 입력하세요!'))
              result+=c*c1
    elif pp==2:
        break

print('주문은 떡볶이는',a1,'개 이고, 순대는',b1,'개이고, 튀김은',c1,'개입니다. 총 가격은',result,'입니다.')

  
