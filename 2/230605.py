#1


#2
import numpy as np

y=np.array([1,-1,2])
a=np.array([[1,1,1],[2,1,3],[1,-1,2]])
x=np.linalg.solve(a,y)
print(a,y,x)