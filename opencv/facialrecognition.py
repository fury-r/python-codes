import cv2 as cv
import time,pandas
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('./test/people.jpg')
gray=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
cv.imshow('gray',gray)

haar_cascade=cv.CascadeClassifier('./xml/haarcascade_frontalface_default.xml')

faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)

for x,y,w,h in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow('Detected faces',img)
print(len(faces_rect))
cv.waitKey(5000)