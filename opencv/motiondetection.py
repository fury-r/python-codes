import cv2 as cv
import time,pandas
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt


#static back
static_back=None
#start time and end time
currentMotion=['','']
#stores frames
motionlist=[]

video=cv.VideoCapture(0,cv.CAP_DSHOW)

while True:
    check,frame=video.read()
    #motion=0 (no motion)
    motion=0

    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
    gray=cv.GaussianBlur(gray,(21,21),0)
    
    if  static_back is None:
        static_back=gray
        

    diff_frame=cv.absdiff(static_back,gray)

    thresh_frame=cv.threshold(diff_frame,30,255,cv.THRESH_BINARY)[1]
    thresh_frame=cv.dilate(thresh_frame,None,iterations=2)

    contour,_=cv.findContours(thresh_frame.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    for count in contour:
        if cv.contourArea(count)<10000:
            motion=1

        if currentMotion[0]=='' and motion==1:
            currentMotion[0]=datetime.now().strftime('%m%d%Y,%H:%M:%S')
        (x,y,w,h)=cv.boundingRect(count)
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

        #if no motion
    if motion==0 and  currentMotion[0]!='':
        currentMotion[1]=datetime.now().strftime('%m%d%Y,%H:%M:%S')
        motionlist.append(currentMotion)
        currentMotion=['','']
    cv.imshow('gray',gray)
    cv.imshow('diff',diff_frame)
    cv.imshow('thresh_frame',thresh_frame)
    cv.imshow('frame',frame)
    key=cv.waitKey(1)
    if key==ord('q'):
        if motion==1 and currentMotion[0]!='':
            currentMotion[1]=datetime.now().strftime('%m%d%Y,%H:%M:%S')
            motionlist.append(currentMotion)
        
        break

for move in motionlist:
    print(move)
video.release()
cv.destroyAllWindows()