import numpy as np
import matplotlib.pyplot as plt

f1 = {'family':'serif','color':'blue','size':20}
f2 = {'family':'serif','color':'magenta','size':15}
x=np.array([1,2,6,4,8,7])
y=np.array([5,6,7,8,9,14])
plt.subplot(1,2,1)
plt.plot(x,y)
plt.grid(color='black')
plt.show()