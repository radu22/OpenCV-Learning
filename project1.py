import cv2
import numpy as np

## WebCam setup
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0) # 0 is for webcam
cap.set(3, frameWidth) #width
cap.set(4, frameHeight) #height
cap.set(10, 150) #brightness

#Color shades that the algorithm can identify
    # blue
    # red
myColors = [[103,96,0,137,255,255],   #hue_min, sat_min, val_min, hue_max, sat_max, val_max
            [0,178,136,3,200,255]]

# Drawing colors
myColorValues = [[153,0,0],  # BGR
                 [0,0,204]]

myPoints = [] # [x,y,colorId]

def findColor(img,myColors, myColorValues):
    '''
    Looks for the given colors shades
    :param img: current image
    :param myColors: color shades that the algorithm can see
    :param myColorValues: similar color shades used for drawing on the image
    :return: the point with its specific color
    '''
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count = 0
    newPoints=[]
    for color in myColors:
        lower = np.array(color[0:3])  #min values
        upper = np.array(color[3:6]) #max values
        mask = cv2.inRange(imgHSV,lower,upper) #create the mask
        x,y = getConturs(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED) # draw a circle for the current location
        if x!=0 and y!=0:  # if the colored object has been spotted
            newPoints.append([x,y,count]) # add the point for drawing
        count += 1  # counter used for keeping track with the color in the list
        #cv2.imshow(str(color[0]),mask)
    return newPoints


def getConturs(img):
    '''
    Finds the contours of the object
    :param img: current image
    :return: returns the middle x position, and the y position
    '''
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # find contours
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)  # calculate the area under the contours
        if area > 500:
            # cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 5)
            peri = cv2.arcLength(cnt, True)  # find the perimeter
            approx = cv2.approxPolyDP(cnt, 0.01 * peri, True)  # find each corner
            x, y, w, h = cv2.boundingRect(approx)  # create the bounding box
    return x+w//2,y


def drawOnCanvas(myPoints,myColorValues):
    '''
    Draws on the screen where the colored object has been
    :param myPoints: list of all the points where the object has been
    :param myColorValues: the color used for drawing
    '''
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 20, myColorValues[point[2]], cv2.FILLED)


while True:  #frame by frame video output
    success, img = cap.read()
    imgResult = img.copy() # the image with the drawings
    newPoints = findColor(img, myColors, myColorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)
    cv2.imshow("Video",img)
    cv2.imshow("result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'): #stop if 'q' is pressed
        break