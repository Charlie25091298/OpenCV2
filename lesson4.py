import cv2

image = cv2.imread("image.jpg",cv2.IMREAD_COLOR)
#line
startpoint = (100,100)
endpoint = (150,100)
color = (0,0,0)
thickness = 3
lineImage = cv2.line(image,startpoint,endpoint,color,thickness)
cv2.imshow("line on image",lineImage)
cv2.waitKey(0)
#rectangle
startpoint = (200,200)
endpoint = (300,350)
color = (0,255,0)
thickness = -1
imagereread = cv2.imread("image.jpg",cv2.IMREAD_COLOR)
rectImage = cv2.rectangle(imagereread,startpoint,endpoint,color,thickness)
cv2.imshow("rectangle on image",rectImage)
cv2.waitKey(0)
#circle
imagecircle = cv2.imread("image.jpg",cv2.IMREAD_COLOR)
centerpoint = (330,330)
radius = 50
color = (0,0,255)
thickness = -1
circleImage = cv2.circle(imagecircle,centerpoint,radius,color,thickness)
cv2.imshow("circle on image",circleImage)
cv2.waitKey(0)
#text
imagewithouttext = cv2.imread("image.jpg",cv2.IMREAD_COLOR)
text = "Hello, World!"
font = cv2.FONT_HERSHEY_COMPLEX
color = (255,0,0)
point = (0,250)
thickness = 1
fontscale = 2
imagewithtext = cv2.putText(imagewithouttext,text,point,font,fontscale,color=color,thickness=3)
cv2.imshow("text on image",imagewithtext)
cv2.waitKey(0)