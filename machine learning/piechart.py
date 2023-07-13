import numpy as np
import matplotlib.pyplot as plt

def normal(x):
    label=['Genshin Impact','BattleGroundsMobileIndia','Call of Duty']
    c=['cyan','orange','black']
    plt.pie(x,labels=label,startangle=90,colors=c,) #default start is at x axis
    plt.legend(title='Games')
    plt.show()
def wedge(x):
    myexplode = [0.2, 0, 0, ]

    label=['Genshin Impact','BattleGroundsMobileIndia','Call of Duty']
    plt.pie(x,labels=label,startangle=90,explode=myexplode,shadow=True) #default start is at x axis
    plt.legend()

    plt.show()
x=np.array([20,80,50])
normal(x)
wedge(x)
