import cv2 as cv
import numpy as np


path = input("Please input image path.\n")
img = cv.imread(path)
img = cv.resize(img, (768,512), interpolation=cv.INTER_CUBIC)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, th = cv.threshold(gray, 90, 255, cv.THRESH_BINARY_INV)

kernel = np.ones((3,3), np.uint8)
erosion = cv.erode(th, kernel, iterations = 1)
dilation = cv.dilate(erosion, kernel, iterations = 1)

circle = cv.HoughCircles(dilation, cv.HOUGH_GRADIENT, 1, minDist=25, param1 = 100, param2 = 10, minRadius = 18, maxRadius = 40)
circle = np.uint16(np.around(circle))
for i in circle[0, :]:
    cv.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)

cv.imshow('dilation' ,dilation)
cv.imshow('result' ,img)
print("The detected number of black Go is", len(circle[0, :]))
cv.waitKey(0)