import cv2
import numpy as np

net = cv2.dnn.readNetFromTorch('models/eccv16/starry_night.t7')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    if ret == False:
        break

    MEAN_VALUE = [103.939, 116.779, 123.680]
    blob = cv2.dnn.blobFromImage(img, mean=MEAN_VALUE)

    net.setInput(blob)
    output = net.forward()

    output = output.squeeze().transpose((1, 2, 0))

    output += MEAN_VALUE
    output = np.clip(output, 0, 255)
    output = output.astype('uint8')

    cv2.imshow('img', img)
    cv2.imshow('result', output)

    if cv2.waitKey(1) == ord('q'):
        break