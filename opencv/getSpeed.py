import os
import cv2 as cv
import time,pandas
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

vehicle_cascade=cv.CascadeClassifier('./xml/cars.xml')
interval=200
video=cv.VideoCapture('./test/4K Road traffic video for object detection and tracking - free download now!.mp4',)
static_back=None
current_motion=['','']
motionlist=[]
car_recog=cv.face.LBPHFaceRecognizer_create
while True:

    check,frame=video.read()

    motion=0

    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    vehicle_detect=vehicle_cascade.detectMultiScale(gray,1.1,4)
    for x,y,w,h in vehicle_detect:
        vehicles_1=gray[y:y+h,x:x+w]
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
    #gray=cv.GaussianBlur(gray,(21,21),0)

    # if static_back is None:
    #     static_back=gray 
    # diff=cv.absdiff(static_back,gray)
    # thresh_frame=cv.threshold(diff,30,255,cv.THRESH_BINARY)[1]
    # thresh_frame=cv.dilate(thresh_frame,None,iterations=2)
    # contours,_=cv.findContours(thresh_frame.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    # for i in contours:
    #     if cv.contourArea(i)<10000:
    #         motion=1
    #     if current_motion[0]=='' and motion==1:
    #         current_motion[0]=datetime.now().strftime('%m%d%Y,%H:%M:%S')
    #         motionlist.append(current_motion)

    #     (x,y,w,h)=cv.boundingRect(i)
    #     cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    # if motion==0 and  current_motion[0]!='':
    #     current_motion[1]=datetime.now().strftime("%m%d%Y:%H:%M:%S")
    #     current_motion=['','']
    cv.imshow('frame',frame)
    key=cv.waitKey(1)
    if key==ord('q'):
        print(motionlist)
        break
video.release()
cv.destroyAllWindows()