#list vs numpy

import numpy as np
#list
A = [1,2.3]; B=[-1,-2,-3];C=[]
print(A+B)

for a, b in zip(A,B):
    C.append(a+b)
print(C)

#numpy
A=np.array([1,2,3]); B=np.array([-1,-2,-3])
C= A+B
print(C)