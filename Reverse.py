import cv2
import numpy
import random
img=cv2.imread('Exg.jpg')
def color_img(img,x1,y1,x2,y2):
    a=random.randint(0,255)
    b=random.randint(0,255)
    c=random.randint(0,255)
    img=cv2.rectangle(img,(x1,y1),(x2,y2),(a,b,c),-1)

print(img.shape)
w=(img.shape[1])/7
h=(img.shape[0])/7
x1=img.shape[1]-w
y1=0
x2=img.shape[1]
y2=h
counter=1
while y1<=img.shape[0]:
    if counter%2!=0:
        while x1>=0:
            color_img(img,x1,y1,x2,y2)
            x1=x1-w
            x2=x2-w
            cv2.imshow('Frame',img)
            cv2.waitKey(500)
        color_img(img,x1,y1,x2,y2)

    else:
        while(x2<=img.shape[1]):
            color_img(img,x1,y1,x2,y2)
            x1=x1+w
            x2+=w
            cv2.imshow('Frame',img)
            cv2.waitKey(500)

    y1=y1+h
    y2=y2+h
    counter+=1
