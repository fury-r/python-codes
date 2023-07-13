def formingMagicSquare(s):
    t=[]
    comb= [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
            ]
    for i in comb:
        for pr,sr in zip(i,s):
            z=0
            for q,r in zip(pr,sr):
                if not q==r:
                    z+=max([q,r])-min([q,r])
        t.append(z)
    return min(t)

print(formingMagicSquare([[4,8,2],[4,5,7],[6,1,6]])) 