
def find_Seq(av,alloc,m,n,process):
    p,a,z=[],[],False
    av1=av
    for i in range(0,n):
        sumc=0
        for j in range(0,m):
            sumc=sumc+alloc[j][i]
        a.append(av[i]+sumc)
    finish=[False for i in range (0,m)]
    temp=[]
    print(need)
    print('need')
    while False in finish:
        o=0
        l=[]
        for i in range(m):
            if(need[i] not  in temp):
                print(temp,i)
                c=1
                for z in range(len(av)):
                    if(need[i][z]>av[z]):
                        c-=1
                        break               
                if(c==1):
                    p.append(process[i])
                    q=[]
                    for x in range(len(alloc[i])):
                        q.append(av[x]+alloc[i][x])
                    av=q                   
                    temp.append(need[i])
                    finish[i]=True
                    o+=1 
        m=m-len(l)
                   
        if(sum(av)==sum(a)):
            z=True
            break
        elif(sum(av)>sum(a)):
            break
    print(f"Process sequence {p}")
    print(f"Used {av}")
    print(f"Total Availability {[av[i]+av1[i] for i in range(0,len(av))]}")
    if z==True: print("Safe")
    else: print("Deadlock")

if __name__=='__main__':
    
    m=int(input("Enter number of process\n"))
    n=int(input("enter number of instances\n"))
    max,alloc,need=[],[],[]
    process=[f'P{i}' for i in range(m)]
    temp=input(f'Available instances ')    
    av=list(map(int,temp.split(' ')))
    # max=[[0, 0, 1, 2], [1, 7, 5, 0], [2, 3, 5, 6], [0, 6, 5, 2], [0, 6, 5, 6]]
    # alloc=[[0, 0, 1, 2], [1, 0, 0, 0], [1, 3, 5, 4], [0, 6, 3, 2], [0, 0, 1, 4]]
    # max=[[6,4,7,3],[4,2,3,2],[2,5,3,3],[6,3,3,2],[5,6,7,5]]
    # alloc=[[3,1,4,1],[2,1,0,2],[2,4,1,3],[4,1,1,0],[2,2,2,1]]

    for i in range(0,m):
        temp=input('max ')
        max.append(list(map(int,temp.split(' '))))
    for i in range(0,m):
        temp=input('allocated ')
        alloc.append(list(map(int,temp.split(' '))))
    for i in range(m):
        q=[]
        for  j in range (len(max[i])):
            q.append(max[i][j]-alloc[i][j])
        need.append(q)
    print(max,alloc)
    while True:
        op=int(input("1.Find_Seq\n2.Grant a Request\n3.Change Available\n4.Exit\n"))
        if(op==1):
            find_Seq(av,alloc,m,n,process)
        elif(op==2):
            print(f"Process {process} ")
            z=0
            o=int(input('Process Number '))-1
            temp=input('New request')
            new=list(map(int,temp.split(' ')))
            for i in range(0,n):
                if new[i]>need[o][i] and new[i]>av[i]:
                    print('Unsafe')
                    z+=1
                    break
            if(z==0):
                for i in range(0,n):
                    av[i]=av[i]-new[i]
                    alloc[o][i]=alloc[o][i]+new[i]
                    need[o][i]=need[o][i]-new[i]
            print("Safe")

        elif(op==3):
            temp=input(f'Available instances ')    
            av=list(map(int,temp.split(' ')))
        elif(op==4):
            break


