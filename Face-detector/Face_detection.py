import cv2

cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
# Start the webcam
cam=cv2.VideoCapture(0)

while True:
    x,frame=cam.read()

    #It is very important to convert the frame to grey-scale image
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=cascade.detectMultiScale(gray,1.1,2)
    #Input the gray image
    # 1.1 is the scaleFactor-specifying how much the image size is reduced at each image     scale.
    # 2 is the minNeighbors:Parameter specifying how many neighbors each candidate rectangle should have to retain it.
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)

    cv2.imshow('Frame',frame)
    if cv2.waitKey(1)&0xFF==ord('a'):
        break

cam.release()
