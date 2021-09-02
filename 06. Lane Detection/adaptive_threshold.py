import cv2
import numpy as np

cap = cv2.VideoCapture(0) # 동영상 불러오기

while(cap.isOpened()):
    ret, image = cap.read()

    src = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # blur = cv2.GaussianBlur(src,(5,5),0)
    cv2.imshow('src', src)

    ret, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imshow('dst', dst)

    dst2 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, 7)
    cv2.imshow('dst2', dst2)

    dst3 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 7)
    cv2.imshow('dst3', dst3)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
