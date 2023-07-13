import cv2 as cv
import numpy as np

img=cv.imread('./test/4.1 charmander.jpg')

#grayscale
#gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#blur
#blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)

#edge cascade
#canny=cv.Canny(img,125,175)

#dilated
#dilated=cv.dilate(img,(7,7),iterations=2)

#eroding
#erode=cv.erode(img,(7,7),iterations=3)

#resize
#resize=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)

#crop
#crop=img[50:200,200:400]

#translate
# def translate(img,x,y):
#     transMat=np.float32([[1,0,x,],[0,y,1]])
#     dimensions=(img.shape[1],img.shape[2])
#     return cv.warpAffine(img,transMat,dimensions)
# translated=translate(img,100,-100)    


#rotate
# def rotate(img,angle,rotPoint=None):
#     (height,width)=img.shape[:2]
#     if not rotPoint:
#         rotPoint=(width//2,height//2)
#     rotmat=cv.getRotationMatrix2D(rotPoint,angle,1.1) 
#     dimesion=(height,width)
#     return cv.warpAffine(img,rotmat,dimesion)
# rotated=rotate(img,-45)

#flip
flip=cv.flip(img,-1)


cv.imshow('flip',flip)
cv.waitKey(1000)