import numpy as np
import matplotlib.pyplot as plt


x=np.random.randint(5,10,200)
y=np.random.randint(10,20,200)
c=np.array([4,5,8,7,8,6,9,5])
plt.scatter(x,y)
plt.colorbar()
plt.show()