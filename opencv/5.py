import cv2 as cv
import numpy as np

img=cv.imread('./test/4.1 charmander.jpg')

blank=np.zeros(img.shape,dtype='uint8')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#threshold
ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
ret,thresh_inv=cv.threshold(gray,125,255,cv.THRESH_BINARY_INV)
adaptive=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,9)
#cv.imshow('adaptive',adaptive)

#contour Detection
canny=cv.Canny(gray,125,175)
contours,heirarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours(lines)')

#Draw Contours 
cv.drawContours(blank,contours,-1,(0,0,255),1)

#cv.imshow('blank',blank)
cv.waitKey(1000)
