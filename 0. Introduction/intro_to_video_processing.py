import cv2

cap = cv2.VideoCapture('week1/03.mp4')

while True:
    ret, img = cap.read()

    if ret == False:
        break

    img = img[183:465, 721:950]
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray_crop_result', img_gray)

    if cv2.waitKey(2) == ord('q'):
        break