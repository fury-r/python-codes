import numpy as np
from scipy import stats
test=[32,111,138,28,59,77,97]

mean=np.mean(test)

mid=np.median(test)

mode=stats.mode(test)
var=np.var(test)
dev=np.std(test)
per=np.percentile(test,75)
print(f"mean:{mean}\nmedian:{mid}\nmode:{mode}\ndeviation:{dev}\n Variance:{var}\npercentile:{per}")