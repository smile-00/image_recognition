import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


path = input()
img = cv.imread(path, cv.IMREAD_GRAYSCALE)

rows,cols=img.shape
rows_half,cols_half=int(rows/2),int(cols/2)
mask=np.zeros((rows,cols,2),dtype=np.uint8)
mask[rows_half-30:rows_half+30,cols_half-30:cols_half+30] = 1

#傅立葉
dft = cv.dft(np.float32(img), flags=cv.DFT_COMPLEX_OUTPUT)
dftShift = np.fft.fftshift(dft)
dft_result = 20 * np.log(cv.magnitude(dftShift[:, :, 0], dftShift[:, :, 1]))

#逆傅立葉
fShift = dftShift*mask
ishift = np.fft.ifftshift(fShift)
recover_result = cv.idft(ishift)
recover_result = cv.magnitude(recover_result[:,:,0], recover_result[:,:,1])

cv.imshow("Image", img)
plt.subplot(121)
plt.imshow(dft_result, cmap="gray")
plt.axis('off')
plt.subplot(122)
plt.imshow(recover_result, cmap="gray")
plt.axis('off')
plt.show()

cv.waitKey()