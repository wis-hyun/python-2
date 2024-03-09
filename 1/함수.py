#1번
    #1
def f(x):
     return x**2+2*x+2
        
print(f(2))
    #2
def di(a):
    if a%2==0: return('짝수')
    else: return('홀수')

print(di(5))
    #3
def af(a,b):
    return(a*b)

print(af(2, 4))

#2번
    #1
def pat(a):
    result=1
    for i in range(1,n+1):
        result*= i
    return result
    #1-2
def pat(a):
    if n==0:
        return 1
    else:
        return n*pat(n-1)
    #2
def hello():
    print('Hello World!')
    hello()

hello()
    #3
def  fibo(n):
    if n==1 or n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
#3번



    
    

