#matplotlib

#1
import matplotlib.pyplot as plt
import numpy as np
t=np.arange(0.,5.,0.2)
plt.plot(t,t,'r--',t,t**2, 'bs',t,t**3,'g^')
plt.show()


#2
x=np.linspace(0,2,100)
y1 = x
y2 = x**2
fig, (ax1, ax2) = plt.subplots(1,2,figsize=(5, 2.7))
ax1.plot(x,y1)
ax2.plot(x,y2)

plt.show()