from statistics import variance


def standardize(x):
    m=sum(x)/len(x)
    variance=sum([(i-m)**2 for i in x])/len(l)
    std=variance**0.5
    n=[(i-m)/std for i in x]
    print(std,m,variance)
    return n;
l=[65,55,89,56,35,14,56,55,87,45,92]
a=standardize(l)
standardize(a)
