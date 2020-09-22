import cv2
print("Package Imported")

cap = cv2.VideoCapture(0) # 0 is for webcam
cap.set(3, 1960) #width
cap.set(4, 1280) #height
cap.set(10, 100) #brightness

while True:  #frame by frame video output
    success, img = cap.read() 
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'): #stop if 'q' is pressed
        break