"""
Logic followed  :
1. In function recognize - Import a dataset with values - color,color name ,hexadecimal code, and R G B values
   Transverse through each row of the dataset and get the name of the color who has closet resemblence to the (R,G,B) value recieved when clicked
   REturn the color name 

2. Function mouse_clicked is performed when user clicked anywhere in the image frame - It sets the R,G,B values and x,y position clicked 
   b,g,r = img[y,x]

   Do look at this part of code -https://github.com/KrutikaBhatt/Image-Processing-OpenCV/blob/master/Session-4/Question1.py
   It shows why b,g,r = img[y,x] and not img[x.y] (Since it shows error when clicked to left side of image)

3. In main code,call the above functions and put text showing the color name and (R,G,B) values

"""

import numpy as np
import pandas as pd
import cv2


img = cv2.imread("Color.png")
# Show the image 
#while(1):
#  cv2.imshow('Frame',img)
#  if cv2.waitKey(1)&0xFF==ord('a'):
#    break

df = pd.read_csv('https://raw.githubusercontent.com/amankharwal/Website-data/master/colors.csv')
df.head(10)

index=["color", "color_name", "hex", "R", "G", "B"]
df = pd.read_csv('https://raw.githubusercontent.com/amankharwal/Website-data/master/colors.csv', names=index, header=None)

clicked = False
r = g = b = xpos = ypos = 0

# Color recognization function

def recognize(R,G,B):
  minimum = 10000
  for i in range(len(df)):
    d = abs(R- int(df.loc[i,"R"])) + abs(G- int(df.loc[i,"G"]))+ abs(B- int(df.loc[i,"B"]))
    if(d<=minimum):
      minimum = d
      cname = df.loc[i,"color_name"]

  return cname

# Mouse click
def mouse_clicked(event,x,y,flags,param):
  if event == cv2.EVENT_LBUTTONDOWN:
    global b,g,r,xpos,ypos, clicked
    clicked = True
    xpos = x
    ypos = y
    b,g,r = img[y,x]
    b = int(b)
    g = int(g)
    r = int(r)

cv2.namedWindow("Color_Recognization")
cv2.setMouseCallback('Color_Recognization',mouse_clicked)

while(1):
  cv2.imshow("Color_Recognization",img)
  if(clicked):
    cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)
    text = recognize(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
    cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
    if(r+g+b>=600):
      cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
      clicked=False

  if cv2.waitKey(20) & 0xFF ==27:  # Press ESC to stop
    break
cv2.destroyAllWindows()