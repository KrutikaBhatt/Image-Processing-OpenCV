mport cv2
import numpy as np
arr=np.zeros((2,2),int)
i=0
img=cv2.imread('Exg.jpg')
def crop_image(event,x,y,flags,param):
    global arr
    global index
    if i<2:
        arr[i]=[x,y]
        i+=1
        if np.all(arr):
            crop_done()

        else:
            pass

def crop_done():
    if arr[0][0]<arr[1][0]:
        if arr[0][1]>arr[1][1]:
            crop=img[arr[1][1]:arr[0][1],arr[0][0]:arr[1][0]]

        else:
            crop=img[arr[0][1]:arr[1][1],arr[0][0]:arr[1][0]]

    else:
        crop=img[arr[0][1]:arr[1][1],arr[1][0]:arr[1][1]]

    cv2.imshow('Cropped',crop)
    
    
cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame',crop_image)
cv2.imshow('Frame',img)
cv2.waitKey(0)
