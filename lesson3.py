import cv2
import numpy as np
#greyscale image using for loop and mean function
image = cv2.imread("image.jpg",cv2.IMREAD_COLOR)
rows,cols = image.shape[0:2]
for i in range(rows):
    for j in range(cols):
        image[i,j] = np.mean(image[i,j]) 
cv2.imshow("Image",image)
cv2.waitKey(0)
#greyscale image using cvtColor
image2 = cv2.imread("image.jpg",cv2.IMREAD_COLOR)
greyscaleImage = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
cv2.imshow("greyscale image",greyscaleImage)
cv2.waitKey(0)
#BGR2HSV
image3 = cv2.imread("image.jpg",cv2.IMREAD_COLOR)
HSVimage = cv2.cvtColor(image3,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV image",HSVimage)
cv2.waitKey(0)
#image rotation
image4 = cv2.imread("image.jpg",cv2.IMREAD_COLOR)
rows,cols = image.shape[0:2]
m = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
warpedImage = cv2.warpAffine(image4,m,(cols,rows))
cv2.imshow("Rotated image",warpedImage)
cv2.waitKey(0)
