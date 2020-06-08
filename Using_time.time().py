import cv2
import time
cap=cv2.VideoCapture(0)
start=time.time()
while True:
	x,frame=cap.read()
	end=time.time()
	TIME=int(end-start)
	flip=cv2.flip(frame,-1)

	if diff%5==0:
		cv2.imshow('Frame',flip)

	else:
		cv2.imshow('Frame',frame)

	if cv2.waitKey(1)&0xFF=='a':
		break