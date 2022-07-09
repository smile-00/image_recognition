import cv2
import numpy as np

path = input()
img = cv2.imread(path)
cv2.imshow('img', img)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower = np.array([0, 50, 200])
upper = np.array([34, 255, 255])
mask = cv2.inRange(hsv, lower, upper)

output = cv2.bitwise_and(img, img, mask = mask)
cv2.imshow('second', mask)
cv2.imshow('result', output)
cv2.waitKey()                     