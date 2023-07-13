

import sys
from typing import final


def bellmanford(arr,source):
    main=[arr[source-1][i] for i in range(len(arr))]

    for k in range(1,len(arr)-1):
        for i in range(0,len(arr)):
        
            main[i]=min([main[i]]+[min([main[j]+arr[j][i] for j in range(len(arr)) if source!=j and k!=j]) ])
    print(main)
infinity=sys.maxsize

arr=[
[0,4,6,infinity,infinity,],
[infinity,0,8,-3,infinity,],
[infinity,infinity,0,-2,11],
[infinity,infinity,infinity,0,infinity],
[2,infinity,infinity,8,0]
]
bellmanford(arr,4)