def CDMA(sender):

    singalspread1=[]
    singalspread2=[]
    for  q in sender:
        s=[]
        for i in range(len(q[0])):
            for j in range (len(q[3])):
                c=0
                if (q[0][i]==1 and q[3][j]==1): c=0
                elif (q[0][i]==0 and q[3][j]==0): c=0
                elif (q[0][i]==0 and q[3][j]==1): c=1 
                elif (q[0][i]==1 and q[3][j]==0): c=1
                s.append(c)  
        singalspread1.append(s)
    for  q in singalspread1:
        s=[]
        for i in q:
                if i==0:s.append(-1)
                else:s.append(1)
        singalspread2.append(s)
    waveForm=[]
    for i in range(len(singalspread2[0])):
        s=0
        for j in range(len(singalspread2)):
            s+=singalspread2[j][i]
        waveForm.append(s)

    l=[]
    for i in range(len(sender)):
        o=len(sender[i][1])
        x=sender[i][2]
        a=[x[k]*waveForm[k] for k in range(0,len(x))]
        l.append(int(sum(a)))
    print(f" INPUT {sender}")
    print(f" spread {singalspread1}")
    print(f" sendingSignal {singalspread2}")
    print(f" Waveform {waveForm}")
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