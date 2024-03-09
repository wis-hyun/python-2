import pandas as pd
import matplotlib.pyplot as plt
import csv
from datetime import datetime
import numpy as np
from matplotlib.ticker import AutoLocator

data=pd.read_csv('D:/Project_Data/Final_Project_Prob_1_data.csv',encoding='euc-kr')
dat=data['평균기온(℃)']
#평균기온과 표준편차 담을 리스트
yhigh=[]
ylow=[]

#1907년
aa=data[data['일시']=='1907-10-01'].index[0]
ab=data[data['일시']=='1907-12-31'].index[0]
ac=dat.loc[aa:ab]
ad=ac.mean()
ae=ac.std()
print('1907년 평균기온:',ad,'  1907년 표준편차:', ae)
yhigh.append(ad)
ylow.append(ae)

# 1908년부터 1949년
for year in range(1908, 1949):
    start_date = datetime.strptime(f'{year}-01-01', '%Y-%m-%d')
    end_date = datetime.strptime(f'{year}-12-31', '%Y-%m-%d')
    
    aa = data[data['일시'] == start_date.strftime('%Y-%m-%d')].index[0]
    ab = data[data['일시'] == end_date.strftime('%Y-%m-%d')].index[0]
    
    ac = data['평균기온(℃)'].loc[aa:ab]
    bd = ac.mean()
    be = ac.std()
    
    print(f'{year}년 평균기온: {bd},  {year}년 표준편차: {be}')
    yhigh.append(bd)
    ylow.append(be)
    
    

#1950년
aa=data[data['일시']=='1950-01-01'].index[0]
ab=data[data['일시']=='1950-08-31'].index[0]
ac=dat.loc[aa:ab]
cd=ac.mean()
ce=ac.std()
print('1950년 평균기온 : ',cd,'  1950년 표준편차 : ', ce)
yhigh.append(cd)
ylow.append(ce)
#1953년
aa=data[data['일시']=='1953-12-01'].index[0]
ab=data[data['일시']=='1953-12-31'].index[0]
ac=dat.loc[aa:ab]
dd=ac.mean()
de=ac.std()
print('1953년 평균기온 : ',dd,'  1953년 표준편차 : ', de)
yhigh.append(dd)
ylow.append(de)

# 1954년부터 2022년
for year in range(1954, 2023):
    start_date = datetime.strptime(f'{year}-01-01', '%Y-%m-%d')
    end_date = datetime.strptime(f'{year}-12-31', '%Y-%m-%d')
    
    aa = data[data['일시'] == start_date.strftime('%Y-%m-%d')].index[0]
    ab = data[data['일시'] == end_date.strftime('%Y-%m-%d')].index[0]
    
    ac = data['평균기온(℃)'].loc[aa:ab]
    ed = ac.mean()
    ee = ac.std()
    
    print(f'{year}년 평균기온: {ed},  {year}년 표준편차: {ee}')
    yhigh.append(ed)
    ylow.append(ee)
    
#2023년
aa=data[data['일시']=='2023-01-01'].index[0]
ab=data[data['일시']=='2023-05-22'].index[0]
ac=dat.loc[aa:ab]
fd=ac.mean()
fe=ac.std()
print('2023년 평균기온:',fd,'  2023년 표준편차:', fe)
yhigh.append(fd)
ylow.append(fe)

# plot 그리기
# 1907~2023년도 범위의 수열 생성
x = np.arange(1907, 2023)
# 제외할 년도
remove_years = np.array([1951, 1952])
# x 수열에서 remove_years에 있는 값을 제외
x = np.delete(x, np.where(np.in1d(x, remove_years))[0])

#평균기온 관련 그래프 그리기
plt.subplot(2,1,1)
plt.plot(x,yhigh,'r')
plt.title('Average temperature by year')
#표준편차 관련 그래프 그리기
plt.subplot(2,1,2)
plt.plot(x,ylow,'b')
plt.title('Standard deviation by year')

plt.gca().xaxis.set_major_locator(AutoLocator())
plt.show()
