
def counting_valleys(steps,path):
    s=v=0
    for i in path:
        if(i=='U'):
            s+=1
        else:
            s-=1
        if(i=='U' and s==0):
            v+=1            
    return v





print(counting_valleys(12,"DDUUDDUDUUUD"))


