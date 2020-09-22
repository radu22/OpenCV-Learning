import cv2
import numpy as np

def empty(a):
    pass

print("Package Imported")
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0) # 0 is for webcam
cap.set(3, frameWidth) #width
cap.set(4, frameHeight) #height
cap.set(10, 150) #brightness


 # Creating a window with trackbars
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",103,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",137,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",96,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

#Make sure the trackbars are read
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # stop if 'q' is pressed
        break

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

    cv2.imshow("Test",mask)



