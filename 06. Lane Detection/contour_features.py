import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('test.png')

img1 = img.copy()
img2 = img.copy()
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
res, thr = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# print(contours)

for i in contours:
    cnt = i
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img1, (x, y), (x+w, y+h), (0, 0, 255), 3)

    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)

    box = np.int0(box)
    print(box)
    cv2.drawContours(img2, [box], 0, (0, 255, 0), 3)

cv2.imshow('rotated', img2)
cv2.waitKey()

# images = [img1, img2]
# titles = ['straight', 'rotated']
# plt.figure(figsize = (8,8))
# for i in range(2):
#     plt.subplot(1, 2, i+1)
#     # plt.title()
#     # plt.imshow()
#     # plt.axis('off')
#     cv2.imshow(titles[i], images[i])
#     cv2.waitKey()