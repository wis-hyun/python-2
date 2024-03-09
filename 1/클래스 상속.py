#0
    #1
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first+self.second
        return result
    def mul(self):
        result=self.first*self.second
    def sub(self):
        result=self.first-self.second
    def div(self):
        result=self.first/self.second

a=FourCal()
a.setdata(4,2)
print(a.add())
    #2
class Counter:
    def make_Counter(self):
        self.count = 0
    def increment(self):
        self.count+=1

a=Counter()
a.make_Counter()

for i in range(10):
    a.increment()
print(a.count)

#1
class Account:
    def make_account(self):
        self.balance=0
    def deposit(self, a):
        self.balance +=a
       
    def withdrawal(self, a):
        self.balance -=a

c=Account()
c.make_account()

c.deposit(1000)
print(c.balance)
c.withdrawal(20000)
print(c.balance)

#2
    #1
class Account:
    def __init__(self):
        self.balance=0
    def deposit(self, a):
        self.balance +=a       
    def withdrawal(self, a):
        self.balance -=a

c=Account()
c.deposit(1000)
print(c.balance)
c.withdrawal(20000)
print(c.balance)
    #2
class Car:
    def __init__(self, color, mileage):
        self.color=color
        self.mileage=mileage
    def forward(self):
        self.mileage+=1

a=Car('red', 1000)
for i in range(10):
    a.forward()

print(a.color)
print(a.mileage)
