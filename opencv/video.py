from re import L
import cv2 as cv

capture=cv.VideoCapture('./test/test.mp4')
while True:
    isTrue,frame=capture.read()
    if  not isTrue:
        break
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):break

capture.release()
cv.destroyAllWindows()
cv.waitKey(30)