import cv2 as cv
import numpy as np
import sys
blank=np.zeros((500,500,3),dtype=None)

#blank[200:300,300:400]=0,0,255
#rectangle
#cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1)
#circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,255,0),thickness=1)

#line
cv.line(blank,(100,250),(300,400),(255,255,255),thickness=3)
#text
cv.putText(blank,'Hello,my name is Fury',(0,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(1,255,0),2)
cv.imshow('TEXT',blank)
cv.waitKey(10000)