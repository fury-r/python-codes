import math as m
def range(x):
    return max(x)-min(x)
def varian(x):
    variance= sum([(i-(sum(x)/len(x)))**2 for i in x ])/len(l)
    return variance
def standard_dev(x):
    return x**0.5 #**0.5 to get square root
l=[65,55,89,56,35,14,56,55,87,45,92]
r=range(l)
v=varian(l)
sv=standard_dev(v)
print(f"range: {r}\nvariance: {v}\nstandard of deviantion: {sv}")