import cv2

img=cv2.imread('image.jpg')
print(img.shape)#Print the resolution of Image
img=cv2.line(img,(0,0),(img.shape[0],img.shape[1]),(255,0,0),5)
cv2.imwrite('Strike.jpg')#Saving the striked image
#Displaying image
cv2.imshow('Frame',img)
cv2.waitKey(0)