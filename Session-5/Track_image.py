import cv2
import numpy as np

define=np.ndarray((0,0),np.uint8)
array=np.zeros((2,2),int) #Creating array of 2*2 size

index=0
#Capturing live video from webcam
cam=cv2.VideoCapture(0)

def double_click(event,x,y,flags,param):#This funtion gets the points to crop in array
    global array,index
    global define
    if event==cv2.EVENT_LBUTTONDOWN:
        if (index <2):
            array[index]=[x,y]
            index+=1

            if np.all(array):
                define=Crop_Image(cam.read()[1],array)

            

def Crop_Image(frame,array):
    global define
   
    if array[0][0]>array[1][0]:
        if array[0][1]>array[1][1]:
            crop=frame[array[1][1]:array[0][1],array[1][0]:array[0][0]]
        else:
            crop=frame[array[0][1]:array[1][1],array[1][0]:array[0][0]]

    else:
        if array[0][1]>array[1][1]:
            crop=frame[array[1][1]:array[0][1],array[0][0]:array[1][0]]
        else:
            crop=frame[array[0][1]:array[1][1],array[0][0]:array[1][0]]

    return crop

   
def Compare_Template(video_frame):
    global define
    grey_frame=cv2.cvtColor(video_frame,cv2.COLOR_BGR2GRAY)
    grey_image=cv2.cvtColor(define,cv2.COLOR_BGR2GRAY)
    
    res=cv2.matchTemplate(grey_frame,grey_image,cv2.TM_CCOEFF_NORMED)
    loc=np.where(res>0.6)
    print(loc)
    return loc



cv2.namedWindow('WebCam')
cv2.setMouseCallback('WebCam',double_click)
while True:
    x,frame=cam.read()

    if define.size>3:
        height=define.shape[0]
        width=define.shape[1]
        match_point=Compare_Template(frame)
        for x,y in zip(*match_point[::-1]):
            cv2.rectangle(frame,(x,y),(x+width,y+height),(255,0,0),1)
            cv2.putText(frame,'Object',(x,y),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),1)
            
        cv2.imshow('Object',define)

    cv2.imshow('WebCam',frame)

    if cv2.waitKey(1)&0xFF==ord('a'):
        break



    
