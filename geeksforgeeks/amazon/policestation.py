def solve(x,N,a):
        x=sorted(x,reverse=True)
        result={
            'ans':0,
            
            'values':[]
        }
        for i in range(len(x)):
            res=(x[i]-a)
            j=i+1
            c=1
            print(x[i])
            while c<N and j<len(x):
                res+=(x[j]-a)
                print(x[j])
                j+=1
                c+=1
            print('---------')
            if res>result['ans']:
                result['ans']=res
        return result['ans']

print(solve([10,4,2,17],4,2))