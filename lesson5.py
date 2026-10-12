import cv2
import os
from PIL import Image

images = "images"
os.chdir(images)
meanheight = 0
meanwidth = 0
totalimages = len(os.listdir("."))
for file in os.listdir(".") :
    if file.endswith(".jpg") :
        