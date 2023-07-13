import cv2 as cv
import numpy as np
import sys
r=cv.imread("./test/4.1 charmander.jpg")

if r is None:
    sys.exit("Could not Read Image")
cv.imshow("Display window",r)
k=cv.waitKey(0)
if k==ord('s'):
    cv.imwrite("./image.png",r)

blank=np.zeros((500,500,3),dtype=0.5)
cv.imshow('Blank',blank)
cv.waitKey(50)