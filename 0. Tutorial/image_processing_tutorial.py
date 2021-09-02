import cv2

img = cv2.imread('01.jpg')
print(cv2.__version__)
print(img)
print(img.shape)

# cv2.rectangle(img, pt1=(259, 89), pt2=(380, 348), color=(255,0,0), thickness=2)
cv2.circle(img, center=(320, 220), radius=(50), color=(0, 0, 255), thickness=3)

cropped_img = img[89:348, 259:380]
img_resized = cv2.resize(img, (512, 256))
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imshow('result', img_rgb)
cv2.waitKey(0)

cv2.imshow('resize', img_resized)
cv2.imshow('crop', cropped_img)
cv2.imshow('wow', img)
cv2.waitKey(0)
