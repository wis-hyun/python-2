
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# 데이터 불러오기
data = pd.read_csv('D:/Project_Data/Final_Project_Prob_2_data.csv', encoding='euc-kr', skiprows=1)
data.dropna(inplace=True)

# x,y 정하기
x = list(data['y1']) 
y = list(data['y2']) 

# 초기값 설정하기
a = 0.0
b = 0.0
learning_rate = 0.0001
num_iterations = 100000
n = len(x)

# 경사하강법 적용하기
for i in range(num_iterations):
    # 예측값 구하기
    predicted = a * np.array(x, dtype=np.float64) + b # x 리스트를 numpy 배열 객체로 변환
    # 오차 구하기
    difference = predicted - y
    # 기울기와 y절편 구하기
    derivative_a = (1 / n) * np.sum(difference * np.array(x, dtype=np.float64))
    derivative_b = (1 / n) * np.sum(difference)
    # 경사하강법 업데이트하기
    a = a - learning_rate * derivative_a
    b = b - learning_rate * derivative_b

# 최적의 a, b 구하기
optimal_a = a
optimal_b = b


# 예측값 생성하기
y_pred = optimal_a * np.array(x, dtype=np.float64) + optimal_b  # x 리스트를 numpy 배열 객체로 변환

# 시각화
plt.scatter(data['x1'], data['y1'], s=10, c='c', label='cyan')
plt.scatter(data['x2'], data['y2'], s=10, c='y', label='yellow')
plt.plot(x, y_pred, color='red')
plt.legend()
plt.show()

print('비용함수 결과 : ', y_pred, '기울기 : ',optimal_a,'y절편 : ', optimal_b)