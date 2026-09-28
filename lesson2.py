import cv2
import numpy as np


ruinsImage = cv2.imread("Ruined.jpg",cv2.IMREAD_COLOR)
cv2.imshow("Ruins",ruinsImage)
spaceImage = cv2.imread("Space.jpg",cv2.IMREAD_COLOR)
cv2.imshow("Space",spaceImage)
#Add the images together
additionImage = cv2.addWeighted(ruinsImage,0.50,spaceImage,0.50,1)
#show the image
cv2.imshow("Added Images",additionImage)
cv2.waitKey(0) 
starImage = cv2.imread("star.jpg",cv2.IMREAD_COLOR)
cv2.imshow("Star",starImage)
diamondImage = cv2.imread("diamond.jpg",cv2.IMREAD_COLOR)
cv2.imshow("Diamond",diamondImage)
#Subtract the image
subtractionImage = cv2.subtract(starImage,diamondImage)
cv2.imshow("Subtracted Images",subtractionImage)
cv2.waitKey(0)
#Resize Image
image = cv2.imread("image.jpg",cv2.IMREAD_COLOR)
resizedImage = cv2.resize(image,(800,800))
cv2.imwrite("resized image.jpg",resizedImage)
cv2.imshow("Resized Image",resizedImage)
cv2.waitKey(0)
#erode image
imageAgain = cv2.imread("image.jpg",cv2.IMREAD_COLOR)
kernel = np.ones((27,27),np.uint8)
erodedImage = cv2.erode(imageAgain,kernel)
cv2.imshow("Eroded Image",erodedImage)
cv2.waitKey(0)
#bordering Image
imageAgainAgain = cv2.imread("image.jpg",cv2.IMREAD_COLOR)
#solid border around image
solidBorderImage = cv2.copyMakeBorder(imageAgainAgain,20,20,20,20,cv2.BORDER_CONSTANT,value=(0,0,0))
cv2.imshow("Image with Border",solidBorderImage)
cv2.waitKey(0)
#reflective border around image
reflectiveBorderImage = cv2.copyMakeBorder(imageAgainAgain,20,20,20,20,cv2.BORDER_REFLECT)
cv2.imshow("Image with Reflective Border",reflectiveBorderImage)
cv2.waitKey(0)
cv2.destroyAllWindows()