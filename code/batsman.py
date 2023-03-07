import cv2
import cvzone
from cvzone.ColorModule import ColorFinder
import numpy as np
from ballDetect import ballDetect




def batsmanDetect(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgBlur= cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgThreshold = cv2.Canny(imgBlur, 112, 0)
    kernel = np.ones((5, 5))
    imgDial = cv2.dilate(imgThreshold, kernel, iterations = 2)
    imgThreshold = cv2.erode(imgDial, kernel, iterations = 2)

    # lower = np.array([threshold1, threshold2, threshold3])
    # upper = np.array([threshold4, threshold5, threshold6 ])

    lower = np.array([112, 0, 181])
    upper = np.array([255, 255, 255])


    mask = cv2.inRange(imgGray, lower, upper)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

















# cap = cv2.VideoCapture(r"lbw.mp4")
# mycolorFinder = ColorFinder(False)
# hsvVals = {'hmin': 0, 'smin': 52, 'vmin': 198, 'hmax': 40, 'smax': 85, 'vmax': 255}
# y_prev = 0


# def empty(a):
#     pass



# def reorder(mypoints):
#     myPoints = mypoints.reshape((4,2))
#     myPointsNew = np.zeros((4, 1, 2), dtype = np.int32)
#     add = myPoints.sum(1)

#     myPointsNew[0] = myPoints[np.argmin(add)]
#     myPointsNew[3] = myPoints[np.argmax(add)]
#     diff = np.diff(myPoints, axis = 1)
#     myPointsNew[1] = myPoints[np.argmin(diff)]
#     myPointsNew[2] = myPoints[np.argmax(diff)]




# cv2.namedWindow("Parameters")
# cv2.resizeWindow("Parameters", 640, 240)
# cv2.createTrackbar("Threshold1", "Parameters", 112, 255, empty)
# cv2.createTrackbar("Threshold2", "Parameters", 0, 255, empty)
# cv2.createTrackbar("Threshold3", "Parameters", 181, 255, empty)
# cv2.createTrackbar("Threshold4", "Parameters", 255, 255, empty)
# cv2.createTrackbar("Threshold5", "Parameters", 255, 255, empty)
# cv2.createTrackbar("Threshold6", "Parameters", 255, 255, empty)
# while True:
#     frame, img = cap.read()
#     imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     imgBlur= cv2.GaussianBlur(imgGray, (5, 5), 1)
#     threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
#     threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
#     threshold3 = cv2.getTrackbarPos("Threshold3", "Parameters")
#     threshold4 = cv2.getTrackbarPos("Threshold4", "Parameters")
#     threshold5 = cv2.getTrackbarPos("Threshold5", "Parameters")
#     threshold6 = cv2.getTrackbarPos("Threshold6", "Parameters")

#     imgThreshold = cv2.Canny(imgBlur, 112, 0)
#     kernel = np.ones((5, 5))
#     imgDial = cv2.dilate(imgThreshold, kernel, iterations = 2)
#     imgThreshold = cv2.erode(imgDial, kernel, iterations = 2)

#     # lower = np.array([threshold1, threshold2, threshold3])
#     # upper = np.array([threshold4, threshold5, threshold6 ])

#     lower = np.array([112, 0, 181])
#     upper = np.array([255, 255, 225])


#     mask = cv2.inRange(imgGray, lower, upper)
#     # Find all contours

#     width = 264
#     height = 2256
                 
#     imgContours = img.copy()
#     # imgWrap = img.copy()
#     contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     for cnt in contours:
#         if cv2.contourArea(cnt) > 5000:
#             y = ballDetect(img, mycolorFinder)
#             if y:
#                 if min(cnt[:,:,1])<y[1]:
#                     cv2.drawContours(imgContours, cnt, -1, (0,255,0), 10)
            


#     #FIND the biggest contour
#     # biggest,  maxArea =  

#     imgStack = cvzone.stackImages([ mask, imgContours], 2, 0.5)
#     cv2.imshow("Stack",imgStack)
#     # cv2.imshow("Perspective", imgWrap)
#     if cv2.waitKey(10) == ord("s"):
#         break

# cap.release()
# cv2.destroyAllWindows()
    
    
    


