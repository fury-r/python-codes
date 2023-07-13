import os
import cv2 as cv
import time,pandas
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

people=['scarlett johansson','robert']
main_path="./test/"
haar_cascade=cv.CascadeClassifier('./xml/haarcascade_frontalface_default.xml')
features=[]
labels=[]

for person in people:
    path=main_path+person
    label=people.index(person)
    for img in os.listdir(path):
        img_path=os.path.join(path,img)
        img_array=cv.imread(img_path)
        gray=cv.cvtColor(img_array,cv.COLOR_RGB2GRAY)
        faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)

        for x,y,w,h in faces_rect:
            faces_roi=gray[y:y+h,x:x+w]
            features.append(faces_roi)
            labels.append(label)
print('training model --------')
#tainer 
features=np.array(features,dtype='object')
labels=np.array(labels)

#neural network
face_recognizer=cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features,labels)

face_recognizer.save('./xml/face_trained.yml')

np.save('features.npy',features)
np.save('labels.npy',labels)
print('training done --------')
