#논리연산자 날짜 확인하기
#1
import datetime
now=datetime.datetime.now()
a=now.hour
b=now.minute

if now.hour==15 and 0<=now.minute<30:
        print('15시 30분 이전입니다.')
elif 30<=now.minute<=59 and now.hour==15:
        print('15시 30분이 지났습니다.')
elif 16==now.hour and 0<=now.minute<=30:
        print('16시가 지났습니다.')
else:
    print('정해진 시간이 아닙니다.')


#2
if 0<=now.hour<=5:
    print('새벽')
elif 6<=now.hour<=11:
    print('오전')
elif 12<=now.hour<=17:
    print('오후')
elif 18<=now.hour<=23:
    print('저녁')
else:
    pass

#1-2
'''
if now.hour==15 or now.hour==16:
    if 0<=now.minute<30:
        print('15시 30분 이전입니다.')
        if 30<=now.minute:
            print('15시 30분이 지났습니다.')
            if n
            '''
#2-2
