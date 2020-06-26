import cv2

cam=cv2.VideoCapture(0)#start video capture

j=0
while True:

    x,frame=cam.read()
    fip=cv2.flip(frame,1)
    j+=1

    if(j%2==0):
        cv2.imshow('Frame',fip)
    else:
        cv2.imshow('Frame',frame)

    if cv2.waitKey(2000) &0xFF==ord('a'):
        break
