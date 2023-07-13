def plusMinus(arr):
    n=len(arr)
    l=[[i for i in arr if(i>0)],[i for i in arr if i<0],[i for i in arr if i==0]]
    for i in l:
        print("%.6f"%(len(i)/n)) #%.6f is  for setting precision


plusMinus([-4, 3, -9, 0, 4, 1])