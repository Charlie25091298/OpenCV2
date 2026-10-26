import cv2
import os
from PIL import Image

images = "images"
os.chdir(images)
meanheight = 0
meanwidth = 0
totalimages = len(os.listdir("."))
imagelist = []
for file in os.listdir(".") :
    if file.endswith(".jpg") :
        imageread = Image.open(file)
        width,height = imageread.size
        meanwidth += width
        meanheight += height
meanwidth //= totalimages
meanheight //= totalimages
for file in os.listdir(".") :
    if file.endswith(".jpg") :
        imageread = Image.open(file)
        image = imageread.resize((meanwidth,meanheight),Image.Resampling.LANCZOS)
        image.save(file,"JPEG",quality = 95)

for file in os.listdir("."):
    if file.endswith(".jpg"):
        imagelist.append(file)
        

filename = "Resized Image.avi"
frame = cv2.imread(imagelist[0])
height,width,layers = frame.shape
video = cv2.VideoWriter(filename,0,1,(width,height))
for file in imagelist :
    readimage = cv2.imread(file)
    video.write(readimage)

cv2.destroyAllWindows()
video.release()
print("code is working")

        
        
        
        