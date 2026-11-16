import cv2
import os
import numpy


path = "Data Sets"
faces = []
labels = []
names = {}
id = 0
for (subdirectories,directories,files) in os.walk(path):
    for directory in directories :
        names[id] = directory
        id += 1
        directorypath = os.path.join(path,directory)
        for file in os.listdir(directorypath) :
            filepath = os.path.join(directorypath,file)
            faces.append(cv2.imread(filepath,0))
            labels.append(id)
width,height = 130,100
(faces,labels) = [numpy.array(lis) for lis in [faces,labels]]
#training the model
model = cv2.face.LBPHFaceRecognizer_create()
model.train(faces,labels)
print("Hello, World!")



