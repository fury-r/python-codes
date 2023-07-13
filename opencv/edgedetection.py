import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('./test/4.3 pikachu.jpg')
#sobel
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combined=cv.bitwise_or(sobelx,sobely)
# cv.imshow('sobelx',sobelx)
# cv.imshow('sobely',sobely)

# cv.imshow('combined',combined)

#laplacian
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
#cv.imshow('lap',lap)

#canny
canny=cv.Canny(gray,150,175)
cv.imshow('canny',canny)
cv.waitKey(5000)