#1번

def ave_all(*args):
    result=0
    for i in args:
        result+=i
        a=result/len(args)
    return(a)
ave_all(1,2,3,4,5)

#2번
'''
    #1

def ad(a,b):
    result=0
    for i in range(a,b+1,1):
        result+=i
    return result

ad(2,5)
    #2
def div(a,b):
    re1=a/b
    re2=a%b
    re3=a//b

    return re1, re2, re3

div(3,5)
    #3-1
def  fibo(n):
    if n==1 or n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    #3-2
def fib(n):
    if n==0: return 0
    if n==1: return 1
    return fib(n-2)+fib(n-1)

for i in range(10):
               print(fib(i))
'''
#3번
    #1
text=input()
count=()
def ab(a,b):
    if b==0:
        return a*1
    return a*b
ab(3,5)

    #2
def ru(ar):
    if ar<0: return ar*-1
    else: return ar
    
ru(-5)
#4번
'''
a=20
def func1():
    global a
    a=10
    print('in func1(), a is %d' %a)

def func2():
    print('in func2(), a is %d' %a)
a=20
func1()
func2()
'''
