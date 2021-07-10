import cv2
import numpy as np

image = cv2.imread('parking.png')
height, width = image.shape[:2]

blank = np.zeros((height, width, 3), np.uint8)

cv2.imshow('img', image)
cv2.imshow('blank', blank)
cv2.waitKey()
