#A
import pandas as pd
import matplotlib.pyplot as plt
import csv
from matplotlib.ticker import AutoLocator
       
data=pd.read_csv('D:/Project_Data/Final_Project_Prob_1_data.csv',encoding='euc-kr')
#4월 최고기온 구하기
data = data.loc[(data['일시'] >= '2023-04-01') & (data['일시'] <= '2023-04-30')]
mdata=data['최고기온(℃)']
#4월 최저기온 구하기
ndata=data['최저기온(℃)']

print('4월 최고기온 : ', mdata)
print('4월 최저기온 : ', ndata)

#4월 평균기온
data=data.loc[:,'일시':'평균기온(℃)']
x=data['일시']
y=data['평균기온(℃)']

#4월 평균기온 그래프 그리기
plt.plot(x,y)
plt.xlabel('day')
plt.ylabel('temperature')
plt.title('Average temperature in April')
#눈금 위치 자동 조정
plt.gca().xaxis.set_major_locator(AutoLocator())
plt.show()
