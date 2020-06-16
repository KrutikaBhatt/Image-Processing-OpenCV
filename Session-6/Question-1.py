import cv2
import numpy as np

# To detect edges in the image as per the required output 
#Step1: Use Thresholding to view image properly as it has Two images
#Step2: Dilate the image and erase all noise and written stuff
#Step3: Smoothen the image using Gaussian Blur 
# Use canny for final Edge detection

image=cv2.imread('Screen.png') 
img_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

guassian=cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,25,2)

kernel_blur=np.ones((5,5))
CLOSE=cv2.morphologyEx(guassian,cv2.MORPH_CLOSE,kernel_blur)

gauss_blur=cv2.GaussianBlur(CLOSE,(25,25),2)
canny=cv2.Canny(gauss_blur,80,255)


cv2.imshow('Gauss',canny)
cv2.waitKey(0)