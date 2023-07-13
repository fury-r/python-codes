import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sn
sn.set()
df=pd.read_csv("./datasets/d.csv")
y=df['GPA']
x1=df['SAT']
x=sm.add_constant(x1)
result=sm.OLS(y,x).fit()
result.summary()
yhat=0.0017*x1+0.275 #coeff
fig=plt.plot(x1,yhat,lw=4,c='red',label='regression line')
plt.scatter(x1,y)
plt.xlabel('SAT',fontsize=20)
plt.ylabel('GPA',fontsize=20)
#plt.xlim(0)
#plt.ylim(0)
plt.show()
