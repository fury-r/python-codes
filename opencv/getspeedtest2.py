import cv2 as cv
import sys

(major_ver, minor_ver, subminor_ver) = (cv.__version__).split('.')

if __name__ == '__main__' :
    trackerTypes = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
    def createTrackerByName(trackerType):
            if trackerType == trackerTypes[0]:
                tracker = cv.legacy.TrackerBoosting_create()
            elif trackerType == trackerTypes[1]:
                tracker = cv.legacy.TrackerMIL_create()
            elif trackerType == trackerTypes[2]:
                tracker = cv.legacy.TrackerKCF_create()
            elif trackerType == trackerTypes[3]:
                tracker = cv.legacy.TrackerTLD_create()
            elif trackerType == trackerTypes[4]:
                tracker = cv.legacy.TrackerMedianFlow_create()
            elif trackerType == trackerTypes[5]:
                tracker = cv.legacy.TrackerGOTURN_create()
            elif trackerType == trackerTypes[6]:
                tracker = cv.TrackerMOSSE_create()
            elif trackerType == trackerTypes[7]:
                tracker = cv.legacy.TrackerCSRT_create()
            else:
                tracker = None
                print('Incorrect tracker name')
                print('Available trackers are:')
                for t in trackerTypes:
                    print(t)

            return tracker





    tracker = cv.legacy.MultiTracker_create()

    video=cv.VideoCapture('./test/4K Road traffic video for object detection and tracking - free download now!.mp4')
    vehicle_cascade=cv.CascadeClassifier('./xml/cars4.xml')
    boundary_box=(287,23,86,320)
    trackertype='CSRT'
    while True:

        check,frame=video.read()
        gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        vehicle_detect=vehicle_cascade.detectMultiScale(gray,1.1,4)
        
        for x,y,w,h in vehicle_detect:
            check=tracker.add(createTrackerByName(trackertype), frame,(x,y,w,h))
        while True:
            check,frame=video.read()
            if not check:
                break
            timer=cv.getTickCount()
            check,boundary_box=tracker.update(frame)
            fps=cv.getTickFrequency()/(cv.getTickCount()-timer)

            if check:
                for i,newbox in enumerate(boundary_box):
                    print(type(newbox[0][1]))
                    p1=(int(newbox[0]),int(newbox[1]))
                    p2=(int(newbox[0]+newbox[2]),(int(newbox[1]+newbox[3])))
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
  