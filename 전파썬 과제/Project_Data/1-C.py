#c
import pandas as pd
import matplotlib.pyplot as plt
import csv
       
data=pd.read_csv('D:/Project_Data/Final_Project_Prob_1_data.csv',encoding='euc-kr')

#1961~1970년
data=data.loc[:,'일시':'평균기온(℃)']
cm = data.loc[(data['일시'] >= '1961-01-01') & (data['일시'] <= '1970-12-31')]
cm=cm['평균기온(℃)']
cm=list(cm)

ab=[]
bb=[]
cb=[]
# 각각의 조건에 맞게 리스트에 넣어줌
c=0
for c in cm:
    #10도 미만일때 ab리스트로
    if c<10:
        ab.append(c)
    #10도이상 20도 미만일때 bb리스트로
    elif 10<=c<20:
        bb.append(c)
    #20도 이상일때 cb리스트로
    elif 20<=c:
        cb.append(c)

#각각의 리스트의 길이를 통해 비율을 구함
ab=len(ab)
bb=len(bb)
cb=len(cb)
ratio = [ab,bb,cb]

#파이차트로 그리기
label=['Less than 10 (°C)', 'More than 10 (°C) and less than 20 (°C)', 'More than 20 (°C)']    
color=['r','g','b']
plt.title('Average temperature in 1961~1970')
plt.pie(ratio, labels=label, autopct='%.1f%%', colors=color)
plt.show()


#2011~2020년
cm = data.loc[(data['일시'] >= '2011-01-01') & (data['일시'] <= '2020-12-31')]
cm=cm['평균기온(℃)']
cm=list(cm)

ab=[]
bb=[]
cb=[]
# 각각의 조건에 맞게 리스트에 넣어줌
c=0
for c in cm:
    #10도 미만일때 ab리스트로
    if c<10:
        ab.append(c)
    #10도 이상 20도 미만일때 bb리스트로
    elif 10<=c<20:
        bb.append(c)
    #20도 이상일때 cb리스트로
    elif 20<=c:
        cb.append(c)
        
#각각의 리스트의 길이를 통해 비율을 구함
ab=len(ab)
bb=len(bb)
cb=len(cb)
ratio = [ab,bb,cb]

#파이차트 그리기
label=['Less than 10 (°C)', 'More than 10 (°C) and less than 20 (°C)', 'More than 20 (°C)']    
color=['r','g','b']
plt.title('Average temperature in 2011~2020')
plt.pie(ratio, labels=label, autopct='%.1f%%', colors=color)
plt.show()
