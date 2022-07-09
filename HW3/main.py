from cv2 import imread, imshow
import numpy as np
import cv2 as cv

path = input()
img = cv.imread(path, cv.IMREAD_GRAYSCALE)

blurred = cv.GaussianBlur(img, (5, 5), 0)
cv.imshow('Blurred', blurred)
canny = cv.Canny(blurred, 0, 100)
cv.imshow('Filter', canny)
#result = cv.adaptiveThreshold(canny, 255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,2)
ret, result = cv.threshold(canny, 0, 255, cv.THRESH_BINARY_INV)
cv.imshow('Result', result)
cv.waitKey(0) 