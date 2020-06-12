import cv2
import numpy
arr=[]
img=cv2.imread('Exg.jpg')
def crop_image(event,x,y,flags,param):
    global arr
    if event==cv2.EVENT_LBUTTONDOWN:
        pts=[(x,y)]
        arr.append((x,y))
        print(arr)

    if len(arr)==2:
        crop=img[arr[0][1]:arr[1][1],arr[0][0]:arr[1][0]]
        cv2.imshow('Crop',crop)
        

cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame',crop_image)
cv2.imshow('Frame',img)
cv2.waitKey(0)