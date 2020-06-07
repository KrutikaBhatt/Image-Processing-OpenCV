import cv2
cam=cv2.VideoCapture(0)
i=input("No. of Frames before flipping :")
j=0
while True:
    x,frame=cam.read()
    fip=cv2.flip(frame,-1)
    j+=1
    if(j%i==0):
        cv2.imshow('Frame',fip)
    else:
        cv2.imshow('Frame',frame)

    if cv2.waitKey(2000) &0xFF==ord('a'):
        break
    
    
