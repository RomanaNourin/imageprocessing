import cv2
import numpy as np
img = cv2.imread('lena.jpg')


def convert_to_negative(img1):
    negative = np.zeros(img.shape, img.dtype)
    height, width = img1.shape[0:2]
    #img1 = img1[:, :, 2]
    for i in range(height):
        for j in range(width):
            negative[i, j] = 255 - img1[i, j]
    cv2.imwrite('negative.jpg', negative)


cv2.imshow('lena.jpg', img)
convert_to_negative(img)
cv2.imshow('Negative Image', cv2.imread('negative.jpg'))
cv2.waitKey(0)
