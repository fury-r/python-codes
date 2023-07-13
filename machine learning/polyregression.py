import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x=np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y=np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

model=np.poly1d(np.polyfit(x,y,3))

print(model)

l=np.linspace(1,24,100)

plt.scatter(x,y)
plt.plot(l,model(l))
plt.show()