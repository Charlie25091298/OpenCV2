import cv2
import numpy
import os

video = cv2.VideoCapture("video.mp4")
for i in range(40) :
    boolean,background = video.read()
    if boolean == False:
        break

while video.isOpened():
    boolean,frame = video.read()
    if boolean == False:
        break
    HSVframe = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_red = numpy.array([100,40,40])
    upper_red = numpy.array([100,255,255])
    mask1 = cv2.inRange(HSVframe,lower_red,upper_red)

    lower_red = numpy.array([150,40,40])
    upper_red = numpy.array([180,255,255])
    mask2 = cv2.inRange(HSVframe,lower_red,upper_red)
    mask1 = mask1 + mask2
    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,numpy.ones((3,3),numpy.uint8),iterations=6)
    mask1 = cv2.dilate(mask1,numpy.ones((3,3),numpy.uint8),iterations=1)
    mask2 = cv2.bitwise_not(mask1)

    result1 = cv2.bitwise_and(background,background,mask= mask1)
    result2 = cv2.bitwise_and(frame,frame,mask=mask2)
    final_output = cv2.addWeighted(result1,1,result2,1,0)
    cv2.imshow("video",final_output)
    key = cv2.waitKey(10)
    if key == 27 :
        break
