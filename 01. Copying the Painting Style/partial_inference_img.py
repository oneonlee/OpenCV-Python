import cv2
import numpy as np

net = cv2.dnn.readNetFromTorch('models/instance_norm/candy.t7')

img = cv2.imread('imgs/hw.jpeg')
cropped_img = img[147:369, 481:811]

h, w, c = cropped_img.shape

cropped_img = cv2.resize(cropped_img, dsize=(500, int(h / w * 500)))

MEAN_VALUE = [103.939, 116.779, 123.680]
blob = cv2.dnn.blobFromImage(cropped_img, mean=MEAN_VALUE)

print(blob.shape)

net.setInput(blob)
output = net.forward()

output = output.squeeze().transpose((1, 2, 0))

output += MEAN_VALUE
output = np.clip(output, 0, 255)
output = output.astype('uint8')

output = cv2.resize(output, (w, h))
img[147:369, 481:811] = output



cv2.imshow('img', img)
# cv2.imshow('img', cropped_img)
cv2.imshow('output', output)


def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("X: " + str(x) + ", Y: " + str(y))
    else:
        pass
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('img', onMouse)

cv2.waitKey(0)


