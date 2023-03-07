import cv2
import cvzone
from cvzone.ColorModule import ColorFinder


def ballDetect(img, mycolorFinder):
    hsvVals = {'hmin': 10, 'smin': 44, 'vmin': 192, 'hmax': 125, 'smax': 114, 'vmax': 255}
    imggray = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    imgColor, mask = mycolorFinder.update(imggray, hsvVals)            
    imgContours, contours =  cvzone.findContours(img, mask, minArea=10)
    # cv2.imshow("ball", imgContours)
    # cv2.waitKey()
    # print(len(contours))   
    # return imgContours
    if contours:
        data = contours[0]
        x = data["center"][0]
        y = data["center"][1]

        print(x,y)
        return (x, y)






















# cap = cv2.VideoCapture(r"lbw.mp4")
# mycolorFinder = ColorFinder(False)
# hsvVals = {'hmin': 10, 'smin': 44, 'vmin': 192, 'hmax': 125, 'smax': 114, 'vmax': 255}
# y_prev = 0
# while True:
#     frame, img = cap.read()
#     imggray = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     imgColor, mask = mycolorFinder.update(imggray, hsvVals)            
    
#     ret, thresh = cv2.threshold(imggray, 127, 255, 0)
#     imgContours, contours =  cvzone.findContours(img, mask, minArea=10)
#     imgStack = cvzone.stackImages([img, imgColor, mask, imgContours], 2, 0.5)
#     # print(len(contours))   
#     if contours:
#         data = contours[0]
#         x = data["center"][0]
#         y = data["center"][1]

#         print(x,y - y_prev)
#         y_prev = y
#         # print(f"area = {data['area']}, centre = {data['center']}")

#     # contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#     # cv2.drawContours(img, contours,  -1, (0,255,0), 3)
#     cv2.imshow("Video", imggray)
#     cv2.imshow("hsv", imgStack)
#     cv2.waitKey()
#     # if key == ord("q"):
#     #     break

# # cap.release()
# # cv2.destroyAllWindows()