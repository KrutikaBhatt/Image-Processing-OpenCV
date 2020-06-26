
#!/usr/bin/env python3
import cv2
import random

def color_img(img,x1,y1,x2,y2):# get randomly colored squares 
    a=random.randint(0,255)
    b=random.randint(0,255)
    c=random.randint(0,255)
    img=cv2.rectangle(img,(x1,y1) , (x2,y2), (a,b,c),-1)


img=cv2.imread('image.jpeg')
print(img.shape)
heigth=(img.shape[0]/7)#To get squares of dimention (img width)/7 *(img height)/7
weidth=(img.shape[1]/7)
counter=0
x1=0
y1=0
x2=weidth
y2=heigth

while y1<=img.shape[0]:
    
    if(counter%2==0):
        while(x2<=img.shape[1]):
            color_img(img,x1,y1,x2,y2)
            x1=x1+weidth
            x2=x2+weidth
            cv2.imshow('Frame',img)
            cv.waitKey(1)
            

    
    else:
        while(x1>=0):
            color_img(img,x1,y1,x2,y2)
            x1=x1-weidth
            x2=x2-weidth
            cv2.imshow('Frame',img)
            cv2.waitKey(1)
            
    color_img(img,x1,y1,x2,y2)  
    y1=y1+heigth
    y2=y2+heigth
    counter=counter+1

    
