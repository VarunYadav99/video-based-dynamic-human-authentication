import cv2
import os

cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480) 

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
n=int(input('\nEnter no of users:'))
i=0
while(i<n):
    
    print("\n [INFO] Initializing face capture. Look at the camera and wait ...")
    count = 0

    while(True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            #cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
            count += 1

            # Save the captured image into the datasets folder
            cv2.imwrite("training-data/User." + str(i) + '.' + str(count) + ".jpg", img)
            cv2.imshow('image', img)

        k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 60: # Take 30 face sample and stop video
            break
    i=i+1
    if i<n:
        print("next user:")
    cv2.waitKey(5000)
cam.release()
cv2.destroyAllWindows()