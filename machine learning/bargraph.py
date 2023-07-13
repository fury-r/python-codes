import numpy as np
import matplotlib.pyplot as plt

x=np.array(['1','2','6','4','7'])
y=np.array([5,6,5,8,3])

plt.bar(x,y,color='hotpink',width=0.4) #barh for horizontal
plt.show()