import numpy as np
import cv2 as cv

c = 0
t = 0
is_grayscale = False
path = input()
num = int(input())
img = cv.imread(path)
width = img.shape[0]
height = img.shape[1]
for row in range(width):
    for col in range(height):
        if img[row][col][0] == img[row][col][1] and img[row][col][1] == img[row][col][2]:
            c += 1
        else:
            t += 1
if c > t:
    is_grayscale = True
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    print("The graph is grayscale.")
else:
    is_grayscale = False
    print("The graph is RGB.")

for row in range(width):
    for col in range(height):
        if is_grayscale:
            if img[row][col] + num > 255:
                img[row][col] = 255
            elif img[row][col] + num < 0:
                img[row][col] = 0
            else:
                img[row][col] = img[row][col] + num
        else:
            if img[row][col][2] + num > 255:
                img[row][col][2] = 255
            elif img[row][col][2] + num < 0:
                img[row][col][2] = 0
            else:
                img[row][col][2] += num
cv.imshow('My Image', img)
cv.waitKey(0)