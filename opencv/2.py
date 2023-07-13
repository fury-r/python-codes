import cv2 as cv
import numpy as np
import sys
blank=np.zeros((500,500,3),dtype=None)

blank[200:300,300:400]=0,0,255
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1)
cv.imshow('Rectangle',blank)
cv.waitKey(10000)