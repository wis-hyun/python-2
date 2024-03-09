import numpy as np
import pandas as pd
#1
data = [1,2,3,4,5]
s1 = pd.Series(data, dytpe='float32')
print(s1)
#2
s=pd.Series(np.arange(5), index=list('abcde'))
print(s[0]); print(s['a']); print(s.iloc[0]); print(s.loc['a'])
print(s[0:3]); print(s['a':'c']); print(s.iloc[0]); print (s.loc['a':'c']); print(s.iloc[[0,1,2]]); print(s.loc[['a','b','c']])
#3
data={'fastfood':['kfc','subway','mom"s touch','quiznos'],'rating':[4.8, 4.2, 2.7, 4.8],'reviewer':[5,24,28,4]}
d=pd.DataFrame(data)
print('d')
print(d)