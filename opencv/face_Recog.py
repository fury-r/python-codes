import cv2 as cv
import time,pandas
import numpy as np
import os


people=['scarlett johansson','robert']
main_path="./test/"
haar_cascade=cv.CascadeClassifier('./xml/haarcascade_frontalface_default.xml')
features=np.load('features.npy',allow_pickle=True)
labels=np.load('labels.npy')

face_recognizer=cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('./xml/face_trained.yml')
img=cv.imread(main_path+people[1]+'/'+'rdj2.jpg')

gray=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
faces_rect=haar_cascade.detectMultiScale(gray,1.1,4)

for x,y,w,h in faces_rect:
        faces_roi=gray[y:y+h,x:x+w]
        label,confidence=face_recognizer.predict(faces_roi)
        print(f'label={people[label]}\nConfidence rating={confidence}')
        cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow('img',img)
cv.waitKey(5000)