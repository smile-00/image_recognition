import cv2 as cv
import numpy as np

path = input()
count = 0
img = cv.imread(path)
img = cv.resize(img, (600,768), interpolation=cv.INTER_CUBIC)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#ret, th = cv.threshold(gray, 127, 255, cv.THRESH_BINARY_INV)
can = cv.Canny(gray, 128, 256)
kernel = np.ones((5,5), np.uint8)
dilation = cv.dilate(can, kernel, iterations = 1)

contours, hierarchy = cv.findContours(dilation, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    (x, y), radius = cv.minEnclosingCircle(cnt)
    center, radius = (int(x), int(y)), int(radius)  # for the minimum enclosing circle
    if(radius <= 20 and radius > 5):
        count += 1
        img = cv.circle(img, center, radius, (0, 255, 0), 2)  # red
print("船的數量為:", count)
cv.imshow('Result', img)
cv.waitKey(0)