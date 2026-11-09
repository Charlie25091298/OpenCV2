import cv2
import numpy
import os

variable = "Data Sets"
sub_data = "Charlie"
path = os.path.join(variable,sub_data)
if not os.path.isdir(path):
    os.mkdir(path)

video = cv2.VideoCapture(0)
facecapture = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
for i in range(30):
    boolean,frame = video.read()
    grayframe = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = facecapture.detectMultiScale(grayframe,1.3,4)
    for face in faces :
        x,y,w,h = face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,0),1)
        face = grayframe[y:y+h,x:x+w]
        cv2.imwrite(path,face)
    
    if boolean == False :
        continue
    cv2.imshow("Camera",frame)
    cv2.waitKey(5)

    