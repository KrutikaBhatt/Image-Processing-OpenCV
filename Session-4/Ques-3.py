import cv2
import numpy as np
img=cv2.imread('Wrap.JPG')
arr=[]
def warp_image(event,x,y,flags,param):
    global arr
    if event==cv2.EVENT_LBUTTONDOWN:
        arr.append((x,y))
        print(arr)

    if len(arr)==4:
        pts1=np.array([(arr[0][0],arr[0][1]),(arr[1][0],arr[1][1]),(arr[2][0],arr[2][1]),(arr[3][0],arr[3][1])],np.float32)
        pts2=np.array([(0,0),(500,0),(0,600),(500,600)],np.float32)
        perspective=cv2.getPerspectiveTransform(pts1,pts2)
        trans=cv2.warpPerspective(img,perspective,(500,600))
        cv2.imshow('Wrap',trans)

cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame',warp_image)
cv2.imshow('Frame',img)
cv2.waitKey(0)
