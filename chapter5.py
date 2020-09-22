import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

width, height=150,222 # dimensions for new image
pts1 = np.float32([[543,194],[696,226],[459,369],[628,414]]) #4 corners of the new image inside the old image
pts2 =np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image", img)
cv2.imshow("Image", imgOutput)

cv2.waitKey(0)