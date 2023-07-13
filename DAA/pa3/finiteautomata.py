def finite_automata(table,p):
    start=0
    for i in p:
        start=table[start][i]
    if start==list(table.keys())[-1]:
        print("Accept")
    else:
        print('Reject')
    


table={
    0:{
        'a':1,'b':0,'c':0
    },
    1:{
        'a':1,'b':2,'c':0
    },2:{
        'a':3,'b':0,'c':0
    },3:{
        'a':1,'b':4,'c':0
    },
    4:{
        'a':5,'b':0,'c':0
    },5:{'a':1,'b':4,'c':6},6:{'a':7,'b':0,'c':0},7:{'a':1,'b':4,'c':0}
}
finite_automata(table,'ababaca')