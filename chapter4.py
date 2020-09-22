import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8) # create image
img[:]= 255, 0, 0 #change color

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) #draw line
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED) #draw rectangle
cv2.circle(img,(400,50),30,(255,255,0),5) # circle
cv2.putText(img, "ALFA",(100,400),cv2.FONT_HERSHEY_COMPLEX,3,(0,150,0),3) #write text
cv2.imshow("Image",img)

cv2.waitKey(0)