# from ballDetect import ballDetect
from pitch import pitch
from batsman import batsmanDetect
import numpy as np

import cv2
import cvzone
from cvzone.ColorModule import ColorFinder

mycolorFinder = ColorFinder(False)

cap = cv2.VideoCapture(r"LBW-Detection\code\lbw.mp4")
    

def ballDetect(img, mycolorFinder):
    hsvVals = {'hmin': 10, 'smin': 44, 'vmin': 192, 'hmax': 125, 'smax': 114, 'vmax': 255}
    imggray = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    imgColor, mask = mycolorFinder.update(imggray, hsvVals)            
    imgContours, contours =  cvzone.findContours(img, mask, minArea=10)  
    x = 0
    y = 0 
    if contours:
        data = contours[0]
        x = data["center"][0]
        y = data["center"][1]

        # print(x,y)
        # return (x, y)
    return imgContours, x, y


def ballPitchPad(x, x_prev, prev_x_diff, y, y_prev, prev_y_diff, batLeg):
    if abs(x - x_prev) > 3 * abs(prev_x_diff):
        if y < batLeg:
            print(abs(x - x_prev), 3 * abs(prev_x_diff))
            # print(1)
            return "Pad", x - x_prev, y - y_prev
        
    if y-y_prev < 0 and prev_y_diff > 0 :
        # print(2)
        if y < batLeg:
            return "Pad", x - x_prev, y - y_prev
        else:
            return "Pitch", x - x_prev, y - y_prev
    
    # if abs(y-y_prev) > 2 * abs(prev_y_diff):
    #     print(3)
    #     if y < batLeg:
    #         return "Pad", x - x_prev, y - y_prev
        
    return "Motion" ,x-x_prev, y - y_prev

x=0
y=0
batLeg = 0
x_prev = 0
y_prev = 0
prev_x_diff = 0
prev_y_diff = 0

while True:
    # print(x, y)
    x_prev = x
    y_prev = y
    frame, img = cap.read()
    ballImg = img.copy()
    pitchImg = img.copy()
    batsmanImg = img.copy()
    

    ballContour, x, y =  ballDetect(img, mycolorFinder)
    all = ballContour.copy()
    pitchContour = pitch(img)
    batsmanContour = batsmanDetect(img)


    for cnt in pitchContour:
        if cv2.contourArea(cnt) > 50000:
            cv2.drawContours(pitchImg, cnt, -1, (0,255,0), 10)
            cv2.drawContours(all, cnt, -1, (0,255,0), 10)

    for cnt in batsmanContour:
        if cv2.contourArea(cnt) > 5000:
            if min(cnt[:,:,1]) < y:
                # batLeg = max(cnt[:,:,1])
                cv2.drawContours(batsmanImg, cnt, -1, (0,0, 255), 10)
                cv2.drawContours(all, cnt, -1, (0,0,255), 10)

    # output = ballPitchPad(x, x_prev, prev_x_diff, y, y_prev, prev_y_diff, batLeg)
    # prev_x_diff = output[1]
    # prev_y_diff = output[2]
    # print(output)
    


    imgStack = cvzone.stackImages([ballContour, pitchImg, batsmanImg, all], 2, 0.5)
    cv2.imshow("stack",imgStack)
    if cv2.waitKey(1) == ord("k"):
        while True:
            if cv2.waitKey(1) == ord("k"):
                break

    elif cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

