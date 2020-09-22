import cv2

faceCascade=cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
img = cv2.imread('Resources/trump.jpg')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # color conversion

faces = faceCascade.detectMultiScale(imgGray,1.1,4) #detect faces

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #draw rectangle on face

cv2.imshow("Result",img)
cv2.waitKey(0)