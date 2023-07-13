import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
x=np.random.randint(1,10,100)
plt.hist(x,60)

plt.show()

x=np.random.uniform(1,10,100)
plt.hist(x,60)

plt.show()
x = np.random.normal(5.0, 1.0, 100000) #mean,deviation,value
plt.hist(x,60)

plt.show()