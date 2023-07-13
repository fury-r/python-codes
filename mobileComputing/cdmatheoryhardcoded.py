def CDMA(sender):

    singalspread1=[]
    singalspread2=[]
    for  q in sender:
        s=[]
        for i in range(len(q[0])):
            x=q[0][i]
            if x==1:x=1
            else:x=-1
            for j in range (len(q[2])):
                c=x*q[2][j]

                s.append(c)  
        singalspread1.append(s)

    waveForm=[]
    for i in range(len(singalspread1[0])):
        s=0
        for j in range(len(singalspread1)):
            s+=singalspread1[j][i]
        waveForm.append(s)

    l=[]
    for i in range(len(sender)):
        o=len(sender[i][1])
        x=sender[i][2]
        a=[x[k]*waveForm[k] for k in range(0,len(x))]
        l.append(int(sum(a)))
    print(f" INPUT {sender}")
    print(f" spread {singalspread1}")
    print(f" sumSpread {waveForm}")
    print(f" Decode {l}")
    print(f'Receiving')
    for i in range(0,len(l)):
        if l[i]>0:
            print(1)
        else:
            print(0)
if __name__=='__main__':
    signal=[]
    n=int(input('enter number of signals '))
    for i in range(0,n):
        a=input('Enter data ')
        senderA=list(map(int,a.split(' ')))
        a=input('Enter Spread ')
        spreadA=list(map(int,a.split(' ')))
        l=[]
        xor=[]
        for q in spreadA:
            if(q==0):
                l.append(-1)
                xor.append(1)
            else:
                xor.append(0)
                l.append(1)
        signal.append([senderA,spreadA,l,xor])

    CDMA(signal)