import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('./test/4.3 pikachu.jpg')

#plot image using matplotlib
# plt.imshow(img)
# plt.show()

#grayscale
grayscale=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#hsv
hsv=cv.cvtColor(img,cv.COLOR_HSV2BGR)

#bgr
bgr=cv.cvtColor(img,cv.COLOR_RGB2BGR)
# plt.imshow(bgr)
# plt.show()

#lab
lab=cv.cvtColor(img,cv.COLOR_RGB2Lab)

#split img channels 
# blank=np.zeros(img.shape[:2],dtype='uint8') 
# b,g,r=cv.split(img)
# blue=cv.merge([b,blank,blank])
# green=cv.merge([g,blank,blank])
# red=cv.merge([r,blank,blank])
# cv.imshow('blue',blue)
# cv.waitKey(500)
# cv.imshow('green',green)
# cv.waitKey(500)
# cv.imshow('red',red)
# cv.waitKey(500)


#average ways to blur img
average=cv.blur(img,(3,3))

#guassian Blur
gauss=cv.GaussianBlur(img,(5,5),0)

#median Blur
median=cv.medianBlur(img,5)

#bilateral
bilateral=cv.bilateralFilter(img,10,35,25)

#bitwise operations
blank=np.zeros((400,400),dtype='uint8')
rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)

# cv.imshow('rectangle',rectangle)
# cv.imshow('circle',circle)

bitwise_and=cv.bitwise_and(rectangle,circle)
bitwise_or=cv.bitwise_or(rectangle,circle)
bitwise_xor=cv.bitwise_xor(rectangle,circle)
bitwise_not=cv.bitwise_not(circle)


# cv.imshow('bitwise_and',bitwise_and)
# cv.imshow('bitwise_or',bitwise_or)
# cv.imshow('bitwise_xor',bitwise_xor)
#cv.imshow('bitwise_not',bitwise_not)

#Mask
blank=np.zeros(img.shape[:2],dtype='uint8')
rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)
mask=cv.bitwise_and(circle,rectangle)
masked=cv.bitwise_and(img,img,mask=mask)

cv.imshow('masked',masked)

cv.waitKey(5000)