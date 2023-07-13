from turtle import width
import cv2 as cv
import numpy as np

def rescaleFrame(frame,size):
    width=int(frame.shape[1]*size)
    height=int(frame.shape[0]*size)
    dimension=(width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

def ChangesRes(width,height):
    capture.set(3,width)
    capture.set(4,height)

capture=cv.VideoCapture('./test/test.mp4')
while True:
    isTrue,frame=capture.read()
    if not isTrue:
        break
    frame_resized=rescaleFrame(frame,0.5)
    cv.imshow('Video',frame)
    cv.imshow('VideoResized',frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()

cv.destroyAllWindows()
cv.waitKey(60)