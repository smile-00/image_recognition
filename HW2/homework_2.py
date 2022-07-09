import cv2 as cv
import numpy as np


def update(x):
    global img
    if circle_detect == 1:
        img = circle_img
    rotate_matrix = cv.getRotationMatrix2D(center, x, 1)
    rotated_image = cv.warpAffine(img, rotate_matrix, (width, height))
    if circle_detect == 1:
        #rotated_image = cv.add(rotated_image, bg_img)
        rotated_image = cv.bitwise_or(rotated_image, bg_img)
    cv.imshow('image_win', rotated_image)

#"Please input image path."
path = input("Please input image path.\n")
img = cv.imread(path)
#宣告
height, width = img.shape[:2]
center = (width/2, height/2)
radius = int(min(height/2, width/2))
#輸入是否旋轉圓形
circle_detect = int(input("Please input 1/0 to determine rotate circle or not. 1 for circle.\n"))
circle_img = np.zeros((height, width, 3), np.uint8)
bg_img = np.zeros((height, width, 3), np.uint8)
if circle_detect == 1:
    for i in range (0, height):
        for j in range(0, width):
            temp = ((i - height/2)*(i - height/2) + (j - width/2)*(j - width/2))
            if temp < radius*radius:
                circle_img[i][j][0] = img[i][j][0]
                circle_img[i][j][1] = img[i][j][1]
                circle_img[i][j][2] = img[i][j][2]
            else:
                bg_img[i][j][0] = img[i][j][0]
                bg_img[i][j][1] = img[i][j][1]
                bg_img[i][j][2] = img[i][j][2]

#cv.imshow('circle', circle_img)
#cv.imshow('background', bg_img)
#觸發tracker
cv.namedWindow('image_win')
cv.createTrackbar('value_name','image_win', 0, 360, update)
cv.imshow('image_win', img)
cv.waitKey(0)
#print(center)
