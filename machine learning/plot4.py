#Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10)
import numpy as np
import matplotlib.pyplot as plt


x=np.array([1,2,6,8])
y=np.array([3,8,1,10])

x1=np.array([1,2,7,8])
y1=np.array([3,2,1,10])
plt.plot(x)
plt.plot(y)
plt.plot(x1)
plt.plot(y1)
plt.show()