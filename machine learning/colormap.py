import numpy as np
import matplotlib.pyplot as plt

f1 = {'family':'serif','color':'blue','size':20}
f2 = {'family':'serif','color':'magenta','size':15}
x=np.array([1,2,6,4,4])
y=np.array([5,6,7,8,3])
c=np.array([11,1,5,7,4])
plt.scatter(x,y,cmap='nipy_spectral',c=c,s=105,alpha=0.9) #alpha is used for transparency
plt.colorbar() #displays colorbar
plt.show()