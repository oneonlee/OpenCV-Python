import cv2
import numpy as np

net = cv2.dnn.readNetFromTorch('models/eccv16/starry_night.t7')

img = cv2.imread('imgs/02.jpeg')

# 전처리
h, w, c = img.shape
img = cv2.resize(img, dsize=(500, int(h / w * 500)))
img =img[162:513, 185:428]

MEAN_VALUE = [103.939, 116.779, 123.680]
blob = cv2.dnn.blobFromImage(img, mean=MEAN_VALUE)

net.setInput(blob)
output=net.forward()

# 후처리
output = output.squeeze().transpose((1, 2, 0))
output += MEAN_VALUE
output = np.clip(output, 0, 255)
output = output.astype('uint8')

cv2.imshow('result', output)
cv2.imshow('image', img)
cv2.waitKey(0)