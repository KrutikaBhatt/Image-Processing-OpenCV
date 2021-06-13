import numpy as np
import cv2

#Get the face and eye casscade classifiers
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface.xml')
eye_casscade = cv2.CascadeClassifier('haarcascade_eye.xml')

#Start the webcam
cam = cv2.VideoCapture(0)
ret,img = cam.read()
reading = True
while(ret):
    ret,img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #Remove Impurity
    gray = cv2.bilateralFilter(gray,5,1,1)

    #Detect the Face
    faces = face_cascade.detectMultiScale(gray,1.3,5,minSize=(200,200))
    if len(faces)>0:
        for (x,y,w,h) in faces:
            # Making a Rectangle around face
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h,x:x+w]
            roi_img = img[y:y+h,x:x+w]

            # Using Eye Casscade to identify the eyes
            eyes = eye_casscade.detectMultiScale(roi_gray,1.3,5,minSize=(50,50))
            if(len(eyes)>=2):
                if(reading):
                    cv2.putText(img,"Eye detected. Press e to exit \nand r to start",(20,70),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
                else:
                    cv2.putText(img,"Eye open!",(70,70),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)

            else:
                if(reading):
                    cv2.putText(img,"No eyes detected",(70,70),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
                else:
                    print("Blink Detected ...")
                    cv2.putText(img,"Blink detected ..",(70,70),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
                    cv2.waitKey(3000)
                    reading = True
    else:
        cv2.putText(img,"No faces detected",(100,100),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
    cv2.imshow('Frame',img)
    a = cv2.waitKey(1)
    if(a == ord('e')):
        break
    elif(a == ord('r') and reading):
        reading = False

cam.release()
cv2.destroyAllWindows()

