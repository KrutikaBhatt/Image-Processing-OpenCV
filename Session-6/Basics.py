import cv2
import numpy as np

#Read the image
img=cv2.imread('lenna.png')
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#For smoothning the image,use blurs
mean_kernel=np.ones((25,25))/625 #Mean kernel
mean_blur=cv2.filter2D(grey,-1,mean_kernel)

gaussian_blur=cv2.GaussianBlur(grey,(25,25),2) #Gaussian kernel

#Edge detections
canny=cv2.Canny(grey,50,100)

sobelx_kernel=np.array([-1,-2,-1,
                       0,0,0,
                       1,2,1])

sobelx=cv2.filter2D(grey,-1,sobelx_kernel)

sobely_kernel=np.array([-1,0,1,
                       -2,0,2,
                       -1,0,1])

sobely=cv2.filter2D(grey,-1,sobely_kernel)

#Sharpening
sharp_kernel=np.array([-1,-1,-1,
                       -1,9,-1,
                       -1,-1,-1])

sharp=cv2.filter2D(grey,-1,sharp_kernel)

cv2.imshow('Sharp',sharp)
cv2.imshow('Sobelx',sobelx)
cv2.imshow('Sobely',sobely)
cv2.imshow('Canny',canny)
cv2.imshow('Mean',mean_blur)
cv2.imshow('Gaussian',gaussian_blur)
cv2.waitKey(0)