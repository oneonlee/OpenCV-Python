import numpy as np
import cv2

img = cv2.imread('parking.png')
img2 = img.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edge = cv2.Canny(imgray, 100, 200)
contours, hierarchy = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
cv2.drawContours(img, [cnt], 0, (0, 255, 0), 3)

epsilon = 0.1 * cv2.arcLength(cnt, True)

approx = cv2.approxPolyDP(cnt, epsilon, True)

cv2.drawContours(img2, [approx], 0, (0, 255, 0), 3)

cv2.imshow('Contour', img)
cv2.imshow('Approx', img2)

cv2.waitKey(0)


