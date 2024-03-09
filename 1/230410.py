#0
f=open('D:/secondpython/새파일.txt','w')
for i in range(1,11):
    data='%d번째 줄입니다.\n' %i
    f.write(data)
f.close()

f=open('D:/secondpython/새파일.txt','r')
line=f.readline()
print(line)
f.close()

f=open('D:/secondpython/새파일.txt','r')
while True:
    line=f.readline()
    lf not line
        break
    print(line)
f.close()

#1
    #1
f=open('D:/secondpython/test1.txt','w')
data='Life is too short\n You need JAVA'
f.write(data)
f.close()

    #2
f=open('D:/secondpython/test2.txt','a')
a=input('입력=>')
f.write(a)
f.write('\n')
f.close()


    #3
f=open('test1.txt','r')
data=f.read()
f.close()
data=data.replace('JAVA', 'PYTHON')
f=open('test1.txt','w')
f.write(data)
f.close()

#2
    #1
import random
f=open('quiz1.txt','w')
for i in range(20):
    a=random.randint(60,100)
    data='%d\n' %a
    f.write(data)
f.close()
    #2
f=open('quiz1.txt','r')
score=[]
while True:
    line=f.readline()
    if 'a' in line: continue
    if not line: break
    data=int(data)
    score.append(data)

num=0
for i in range(1, 20):
    num+=score[i]
result=num/20
print(num)
print(result)
f.close()    
