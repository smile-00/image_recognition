import cv2 as cv
import numpy as np

path = input()
img = cv.imread(path)
img = cv.resize(img, (600,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('img', img)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

lower = np.array([0, 43, 46])
upper = np.array([10, 255, 255])
mask = cv.inRange(hsv, lower, upper)

height,width = mask.shape
black = np.array([0,0,0])
blue = np.array([255,0,0])
yellow = np.array([0,255,255])

img_b = img.copy()
img_y = img.copy()
for row in range(height):
    for col in range(width):
        if (black!=mask[row][col]).all():
            img_b[row][col] = blue
            img_y[row][col] = yellow

cv.imshow('result1', img_b)
cv.imshow('result2', img_y)
cv.waitKey(0)                     