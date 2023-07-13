import numpy as np
import matplotlib.pyplot as plt

f1 = {'family':'serif','color':'blue','size':20}
f2 = {'family':'serif','color':'magenta','size':15}
x=np.array([1,2,6,4,8,7])
y=np.array([5,6,7,8,9,14])
plt.plot(x,y)
plt.title("Placements",fontdict=f1,loc='right')
plt.xlabel("Placement rank",fontdict=f2)
plt.ylabel("Placement level",fontdict=f2)
plt.grid(color='green',linestyle=':')#axis= x or y
plt.show()