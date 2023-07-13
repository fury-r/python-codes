import pandas as pd
#Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10)
import numpy as np
import matplotlib.pyplot as plt


x=np.array([1,2,6,8])
y=np.array([3,8,1,10])
plt.plot(x,y,marker='o',lineStyle=':',c='g',mfc='r',mec='r')
plt.show()