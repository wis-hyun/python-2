#3번
import turtle
import random

#결승선
turtle.penup()
turtle.forward(300) #경주장의 길이는 300pixel
turtle.pendown()
turtle.left(90)
turtle.forward(350) #결승선을 그려줌
turtle.write('결승선', font=('Arial', 20))

#각각 거북이 준비
t1 = turtle.Turtle('turtle') #1번 거북이의 위치와 색상
t1.penup()
t1.goto(0,100)
t1.pencolor('red')
t2 = turtle.Turtle('turtle') #2번 거북이의 위치와 색상
t2.penup()
t2.goto(0,200)
t2.pencolor('blue')
t3 = turtle.Turtle('turtle') #3번 거북이의 위치와 색상
t3.penup()
t3.goto(0,300)
t3.pencolor('purple')

#임의로 트랙 순을 정함
turtles=[t1, t2, t3] #1,2,3번 거북이를 turtles리스트에 저장
random.shuffle(turtles) #turtles리스트를 무작위로 섞어줌

#트랙순으로 거북이 이동
for turtle in turtles: #각 거북이 한마리씩 실행
    for i in range(0, 12): #12번의 기회가 주어짐
        distance = random.randint(1, 6) #주사위 1부터 6까지 랜덤으로 한가지를 뽑음
        turtle.forward(distance * 10) #나온 주사위의 수에 10을 곱한만큼 이동
        if turtle.xcor()>=300: #만약 가장먼저 결승선을 통과한 거북이가 있다면 경주 종료
            break
    if turtle.xcor() < 300: #12회의 기회동안 어떤 거북이도 통과하지 못하면 경주 종료
        break

#결승선을 통과하지 못한 경우  fail 표시
if t1.xcor()<300:print(' red Turtle  :  fail')
if t2.xcor()<300:print(' blue Turtle  : fail')
if t3.xcor()<300:print('purple Turtle  : fail')
    
#결승선 통과한 거북이들을 이동거리와 트랙순서에 따라 정렬
#finishers 리스트안에 결승선을 통과한 거북이들을 저장
finishers = []
for turtle in turtles:
    if turtle.xcor() >=300:
        finishers.append(turtle)
#finishers 안에 있는 거북이들을 이동거리와 트랙순서에 따라 정렬해서 넣어줄 finishers_sorted 리스트 생성         
finishers_sorted = []
while finishers: #finishers에 거북이가 존재한다면, 참이라면
    max_turtle = finishers[0] #finishers에서의 최댓값(가장 멀리 이동한 거북이)를 초기 설정
    for turtle in finishers: #finishers에 있는 요소들을 하나씩 turtle에 넣어서 실행
        if turtle.xcor()>max_turtle.xcor(): #만약 turtle의 이동거리>max_turtle의 이동거리 라면
            max_turtle=turtle # turtle이 max_turtle이다.
        elif turtle.xcor() == max_turtle.xcor() and turtles.index(turtle) <turtles.index(max_turtle): # 만약 이동거리가 같고, 트랙순서(turtle에서의 위치)가 turtle < max_turtle이라면 
            max_turtle = turtle # turtle이 max_turtle이다.
    finishers_sorted.append(max_turtle) #finisher_sorted리스트에 max_turtle를 추가
    finishers.remove(max_turtle) #finisher리스트에 max_turtle를 제거

# 각 거북이의 순위 출력
colors=['red','blue','purple']  #colors 리스트 생성
#리스트 finishers_sorted에 있는 거북이들의 순서를 정하고, 각 거북이의 색상과 순위 출력
for i in range(len(finishers_sorted)):
    turtle = finishers_sorted[i]
    color = ''
    if turtle == t1:
        color = colors[0]
    elif turtle == t2:
        color = colors[1]
    elif turtle == t3:
        color = colors[2]
    print(f"{color} Turtle은  {i+1}등 입니다.")
