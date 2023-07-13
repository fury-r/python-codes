import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#image
img=cv.imread('./test/4.1 charmander.jpg')
cv.imshow('Cats',img)
cv.waitKey(10)

blank=np.zeros((500,500,3))
cv.imshow('Blank',blank)
cv.waitKey(500)