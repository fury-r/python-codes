def Chaining(arr,size):
    table=[None]*size
    table_structure={}
    for i in arr:
        location=2*i+3
        location%=10
        index=location

        if not table[location]:
            table[location]=[i]
        else:
            table[location].append(i)
        table_structure[i]={
            'key':i,
            'location':index
        }
    print(table)
Chaining([3,2,9,6,11,13,7,12],10)