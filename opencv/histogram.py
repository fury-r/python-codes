import cv2 as cv


import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('./test/4.3 pikachu.jpg')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blank=np.zeros(img.shape[:2],dtype='uint8')
rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)
mask=cv.bitwise_and(circle,rectangle)
colors=('b','g','r')
gray_hist=cv.calcHist([gray],[0],mask,[256],[0,256])
plt.figure()
plt.title('Histogram')
plt.xlabel('Grayscale histogram')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
 