import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib.pyplot as plt


def show(img, figsize=(10, 10), title="Image"):
    figure=plt.figure(figsize=figsize)
    
    plt.imshow(img)
    plt.show()

def get_size(filename="dd.png"):
    stat = os.stat(filename)
    size=stat.st_size
    return size

def RLE_encoding(channel):
    # ret,channel = cv.threshold(channel, 127, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
    encoded = []
    count = 0
    prev = None
    fchannel = channel.flatten()
    for pixel in fchannel:
        if prev==None:
            prev = pixel
            count += 1
        else:
            if prev!=pixel:
                encoded.append((count, prev))
                prev=pixel
                count = 1
            else:
                count += 1
    encoded.append((count, prev))
    
    return np.array(encoded)

img1 = cv.imread("img1.bmp")
img2 = cv.imread("img2.bmp")
img3 = cv.imread("img3.bmp")
b1, g1, r1 = img1[:, :, 0], img1[:, :, 1], img1[:, :, 2]
b2, g2, r2 = img2[:, :, 0], img2[:, :, 1], img2[:, :, 2]
b3, g3, r3 = img3[:, :, 0], img3[:, :, 1], img3[:, :, 2]

shape1 = img1.shape
shape2 = img2.shape
shape3 = img3.shape

bb1 = RLE_encoding(b1)
gg1 = RLE_encoding(g1)
rr1 = RLE_encoding(r1)
bb2 = RLE_encoding(b2)
gg2 = RLE_encoding(g2)
rr2 = RLE_encoding(r2)
bb3 = RLE_encoding(b3)
gg3 = RLE_encoding(g3)
rr3 = RLE_encoding(r3)

#save encode file
np.savez("encoded_img1.npz", [bb1, gg1, rr1], dtype=object)
np.savez("encoded_img2.npz", [bb2, gg2, rr2], dtype=object)
np.savez("encoded_img3.npz", [bb3, gg3, rr3], dtype=object)

#ratio
ratio1 = get_size("img1.bmp")/get_size("encoded_img1.npz")
ratio2 = get_size("img2.bmp")/get_size("encoded_img2.npz")
ratio3 = get_size("img3.bmp")/get_size("encoded_img3.npz")

#output
print("size of img1 =", get_size("img1.bmp"))
print("img1 compression size =", get_size("encoded_img1.npz"))
print("compression ratio =", ratio1)
print("size of img2 =", get_size("img2.bmp"))
print("img2 compression size =", get_size("encoded_img2.npz"))
print("compression ratio =", ratio2)
print("size of img3 =", get_size("img3.bmp"))
print("img3 compression size =", get_size("encoded_img3.npz"))
print("compression ratio =", ratio3)
print("average compression ratio =", (ratio1 + ratio2 + ratio3)/3)
