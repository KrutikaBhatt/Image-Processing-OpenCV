import cv2

cam =cv2.VideoCapture(0)#Start video capture
i=1

while i<=50:#To store 50 images

    frame,x=cam.read()
    cv2.imwrite('IMG_'+str(i)+'.jpg',x)
    print('IMG-{0}'.format(i))
    i+=1
    if cv2.waitKey(5000)&0xFF==ord('a'):
        break
