#Detecting colors
import cv2
import numpy as np

def empty(a):
    pass

path = "Resources/lambo.jpg"

 # Creating a window with trackbars
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",26,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",66,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",45,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

#Make sure the trackbars are read
while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max","TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min","TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max","TrackBars")
    v_min = cv2.getTrackbarPos("Val Min","TrackBars")
    v_max = cv2.getTrackbarPos("Val Max","TrackBars")
    lower = np.array([h_min,s_min,v_min])  #min values
    upper = np.array([h_max,s_max,v_max]) #max values
    mask = cv2.inRange(imgHSV,lower,upper) #create the mask

    imgResult = cv2.bitwise_and(img,img,mask=mask) # combine the img with the mask

    cv2.imshow("Original",img)
    cv2.imshow("HSV",imgHSV)
    cv2.imshow("Mask",mask)
    cv2.imshow("ImageResult",imgResult)

    cv2.waitKey(1)
