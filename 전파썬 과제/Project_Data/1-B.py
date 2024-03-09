#B
import pandas as pd
import matplotlib.pyplot as plt
import csv
from matplotlib.ticker import AutoLocator
       
data=pd.read_csv('D:/Project_Data/Final_Project_Prob_1_data.csv',encoding='euc-kr')
#일교차가 큰 해 구하기
m=data['일교차'].max()
m = data.loc[data['일교차'] == m]
year=m['일시']
print(year)

#월별로 평균기온과 표준편차 구하기
f=data.loc[12511:12541]
am=f['평균기온(℃)'].mean()
fs=f['평균기온(℃)'].std()
print('1월 평균기온 : ',am)
print('1월 표준편차 : ',fs)

f=data.loc[12542:12569]
bm=f['평균기온(℃)'].mean()
fs=f['평균기온(℃)'].std()
print('2월 평균기온 : ',bm)
print('2월 표준편차 : ',fs)

f=data.loc[12570:12600]
cm=f['평균기온(℃)'].mean()
fs=f['평균기온(℃)'].std()
print('3월 평균기온 : ',cm)
print('3월 표준편차 : ',fs)

f=data.loc[12601:12630]
dm=f['평균기온(℃)'].mean()
fs=f['평균기온(℃)'].std()
print('4월 평균기온 : ',dm)
print('4월 표준편차 : ',fs)

f=data.loc[12631:12661]
em=f['평균기온(℃)'].mean()
fs=f['평균기온(℃)'].std()
print('5월 평균기온 : ',em)
print('5월 표준편차 : ',fs)

f=data.loc[12662:12691]
fm=f['평균기온(℃)'].mean()
fs=f['평균기온(℃)'].std()
print('6월 평균기온 : ',fm)
print('6월 표준편차 : ',fs)

f=data.loc[12692:12722]
gm=f['평균기온(℃)'].mean()
fs=f['평균기온(℃)'].std()
print('7월 평균기온 : ',gm)
print('7월 표준편차 : ',fs)

f=data.loc[12723:12753]
hm=f['평균기온(℃)'].mean()
fs=f['평균기온(℃)'].std()
print('8월 평균기온 : ',hm)
print('8월 표준편차 : ',fs)

f=data.loc[12754:12783]
im=f['평균기온(℃)'].mean()
fs=f['평균기온(℃)'].std()
print('9월 평균기온 : ',im)
print('9월 표준편차 : ',fs)

f=data.loc[12784:12814]
jm=f['평균기온(℃)'].mean()
fs=f['평균기온(℃)'].std()
print('10월 평균기온 : ',jm)
print('10월 표준편차 : ',fs)

f=data.loc[12815:12844]
km=f['평균기온(℃)'].mean()
fs=f['평균기온(℃)'].std()
print('11월 평균기온 : ',km)
print('11월 표준편차 : ',fs)

f=data.loc[12845:12875]
lm=f['평균기온(℃)'].mean()
fs=f['평균기온(℃)'].std()
print('12월 평균기온 : ',lm)
print('12월 표준편차 : ',fs)

#월별 평균기온 막대그래프 그리기
x=[1,2,3,4,5,6,7,8,9,10,11,12]
y=[am,bm,cm,dm,em,fm,gm,hm,im,jm,km,lm]

plt.title('Average temperature in 1942')
plt.xlabel('month')
plt.ylabel('temperature')
plt.gca().xaxis.set_major_locator(AutoLocator())
plt.bar(x, y)

plt.show()
