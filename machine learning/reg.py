import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sn
sn.set() #overides the style of matplotlib graphs
df=pd.read_csv("./datasets/d.csv")
y=df['GPA']
x1=df['SAT']
plt.scatter(x1,y)
plt.xlabel('SAT',fontsize=20)
plt.ylabel('GPA',fontsize=20)
plt.show()
x=sm.add_constant(x1)
result=sm.OLS(y,x).fit()
result.summary()