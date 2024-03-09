'''
#except_Exception.py
try:
    a=[1,2]
    int(a)
except ZeroDivisionError as e:
    print(type(e),e)
except IndexError as e:
    print(type(e),e)
except Exception as e:
    print(type(e),e)

#except_finally_test1.py
def test():
    print("first line")
    try:
        print("enter try")
        return
        print("after return")
    except:
        print("enter except")
    else:
        print("enter else")
    finally:
        print("enter finally")
    print("last line")

test()

#except_finally_test2.py
print("start")

while True:
    try:
        print("enter try")
        break
        print("after break")
    except:
        print("enter except")
    finally:
        print("enter finally")
    print("last line")

print("finish")

#1
    #1
try:
    number_input=int(input('Number:'))
    print("Radius:", number_input)
    print("Area:",3.14*number_input**2)
except:
       print('숫자가 아닌것을 입력하였습니다.')
    #2
try:
    number_input=int(input('Number:'))
    print("Radius:", number_input)
    print("Area:",3.14*number_input**2)
except ValueError as e:
    print("Enter number")
    print("Value Error", e)

    #3
try:
    number_input=int(input('Number:'))
except:
    print('숫자가 아닌것을 입력하였습니다.')
else:
    print("Radius:", number_input)
    print("Area:", 3.14*number_input**2)
'''
#2
    #1
a=all([1,2, abs(-3)-3])
print(a)
    #2
b=list(filter(lambda x: x>0, [1,-2,3,-5,8,-3]))
print(b)
    #3
c=hex(234)
print(c)
