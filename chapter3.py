import cv2
import numpy as np

img = cv2.imread("Resources/test_img.jpg")
print(img.shape)

imgResize = cv2.resize(img,(300,200)) #image resize
print(imgResize.shape)

imgCropped = img[0:200,300:600] #image crop

cv2.imshow("Image", img)
# cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)