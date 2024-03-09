#2023.03.29
#1번
'''
for i in 'Hello!':
    print(i)
'''
#2번
'''
names=['홍길동','전우치','별주부','옹고집','배비장']
for i in names:
    name=i
    a=name[0]+'*'+name[-1]
    print(a)
 '''   
#3번
    #1
'''
a=range(2, 6)
b=list(a)
print(b)
'''
    #2
'''
for i in range(0,31,3): print(i)
'''
    #3
'''
for i in range(6,0,-1): print(i)
'''
    #4
'''
names=['홍길동','전우치','별주부','옹고집','배비장']
for i in range(len(names)):
    name = names[i]
    name = name[0]+'*'+name[2]
    print(name) 
 '''   
#4번
    #1
'''
num=0
for i in range(1,101):
    num+=i
    if num>1000:
        print(num)
        break
    else:
        continue
'''
'''
result=0
i=0
for i in range(1,101):
    result+=i
    if result >=1000:
        break
print(i)
'''
    #2
'''
num=0
for i in range(1,101):
    if i%3==0:
        continue
    num+=i
print(num)
'''
    #3
'''
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end='')
    print('   ')
  '''
'''
i=0
while i<=8:
    i+=1
    j=0
    while j<=8:
        j+=1
        print(i*j, end='')
    print(' ')
''' 
  
#5번
'''
numbers=[1,2,3,4,5]

result=[n*2 for n in numbers if n%2==1]
print(result)
'''

#6번
maxv=0
a=0
b=0
for i in range(1,100):
    for j in range(99,0,-1):
        current=i*j
        if maxv<current:
            a=i
            b=j
            maxv=current
print(a, b, maxv)


