import cv2 as cv
import sys

(major_ver, minor_ver, subminor_ver) = (cv.__version__).split('.')

if __name__ == '__main__' :



    tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
    tracker_type = tracker_types[2]

    if int(minor_ver) < 3:
        tracker = cv.Tracker_create(tracker_type)
    else:
        if tracker_type == 'BOOSTING':
            tracker = cv.TrackerBoosting_create()
        if tracker_type == 'MIL':
            tracker = cv.TrackerMIL_create()
        if tracker_type == 'KCF':
            tracker = cv.TrackerKCF_create()
        if tracker_type == 'TLD':
            tracker = cv.TrackerTLD_create()
        if tracker_type == 'MEDIANFLOW':
            tracker = cv.TrackerMedianFlow_create()
        if tracker_type == 'GOTURN':
            tracker = cv.TrackerGOTURN_create()
        if tracker_type == 'MOSSE':
            tracker = cv.TrackerMOSSE_create()
        if tracker_type == "CSRT":
            tracker = cv.TrackerCSRT_create()

    video=cv.VideoCapture('./test/4K Road traffic video for object detection and tracking - free download now!.mp4')
    vehicle_cascade=cv.CascadeClassifier('./xml/cars.xml')
    boundary_box=(287,23,86,320)
    while True:

        check,frame=video.read()
        gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        vehicle_detect=vehicle_cascade.detectMultiScale(gray,1.1,4)
        for x,y,w,h in vehicle_detect:

            check=tracker.init(frame,(x,y,w,h))
        while True:
            check,frame=video.read()
            if not check:
                break
            timer=cv.getTickCount()
            check,boundary_box=tracker.update(frame)
            fps=cv.getTickFrequency()/(cv.getTickCount()-timer)

            if check:
                print(boundary_box,'box')
                p1=(int(boundary_box[0]),int(boundary_box[1]))
                p2=(int(boundary_box[0]+boundary_box[2]),(int(boundary_box[1]+boundary_box[3])))
                cv.rectangle(frame,p1,p2,(255,0,0),2,1)
            else:
                cv.putText(frame,'tracking failure detected',(100,80),cv.FONT_HERSHEY_SIMPLEX,0.75,(0,0,255),2)
                
            cv.putText(frame,'tracker',(100,20),cv.FONT_HERSHEY_SIMPLEX,0.75,(50,170,50),2)
            cv.putText(frame,'fps'+str(int(fps)),(100,50),cv.FONT_HERSHEY_SIMPLEX,0.75,(50,170,50),2)
            cv.imshow('Tracking',frame)
            key=cv.waitKey(1)
        if key==ord('q'):
            break
video.release()
cv.destroyAllWindows()
  