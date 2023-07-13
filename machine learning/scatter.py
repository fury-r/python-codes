import numpy as np
import matplotlib.pyplot as plt

f1 = {'family':'serif','color':'blue','size':20}
f2 = {'family':'serif','color':'magenta','size':15}
x=np.array([1,2,6,4,4])
y=np.array([5,6,7,8,3])
plt.scatter(x,y,color='r')

c=np.array(["red","green","blue","yellow","pink"])

x=np.array([2,2,6,4,2])
y=np.array([5,6,7,8,7])
plt.scatter(x,y,color=c)
plt.show()
