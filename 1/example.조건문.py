import datetime
now=datetime.datetime.now()
print(now)

if now.hour<16:
    print('지하철을 타라')
else:
    print('택시')

if now.minute%now.hour<=5:
    print('abc')
else:
    print('def')
