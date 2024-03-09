#0
    #1
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.selffirst+self.second
        return result
    def mul(self):
        result=self.first*self.second
    def sub(self):
        result=self.first-self.second
        
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
    def div(self):
        if self.second==0:
            return 0
        else:
            return self.first/self.second
        
a=MoreFourCal()
print(a.div())
print(a.add())

#1
    #1
al=input('숫자입력')
be= input('대체될 숫자')
ga=input('대체할 숫자')

def Num_replace(al, be, ga):
    c=al.replace('be', 'ga')
    return c

num = Num_replace(al,be,ga)
print(num)
    #2
a= list(input('숫자 입력'))

def Num_sort(a):
    a.sort()
    d=str(a)
    return d

num=Num_sort(a)
print(num)

#2
    #1
class Num_cal():
    def Num_Set(self,num):
        self.num=num
    def Num_replace(self, num, change):
        self.replace('num', 'change')
    def Num_sort(self, num):
        self.sort(num)

a=Num_cal()
a.Num_Set(1423)
b=a.Num_replace(4,2)
print(b)
c= a.Num_sort()
print(c)
    #2
class Num_cal_extend(Num_cal):
    def Num_reverse(self, num):
        self.sort(num)
        self.reverse(num)
a=Num_cal_extend()
a.Num_Set(1432)
b=a.Num_replace(4,2)
print(b)
c=a.Num_sort()
print(c)
d=a.Num_reverse()
print(d)
