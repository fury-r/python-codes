import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import stats
from sklearn import linear_model
df=pd.read_csv("./datasets/d.csv")
def conv(x):
    return int(x)
def func(x):
    return slope*x+intercept
x=df['GPA'].apply(conv)
y=df['SAT'].apply(conv)
print(len(x),len(y))
slope, intercept, r, p, std_err=stats.linregress(x,y)
model=list(map(func,x))
reg=linear_model.LinearRegression()
reg.fit(x,y)
predict=reg.predict([20,10])
print(predict)
plt.scatter(x,y)
plt.plot(x,model)
plt.show()