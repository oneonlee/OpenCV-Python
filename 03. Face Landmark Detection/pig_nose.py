import cv2
import numpy as np
import dlib

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('models/shape_predictor_5_face_landmarks.dat')

# cap = cv2.VideoCapture('videos/02.mp4')
cap = cv2.VideoCapture(0)

sticker_img = cv2.imread('imgs/pig.png', cv2.IMREAD_UNCHANGED)

while True:
    ret, img = cap.read()

    if ret == False:
        break

    dets = detector(img)
    print("number of faces detected:", len(dets))

    for det in dets:
        shape = predictor(img, det)

        glabella_x1 = shape.parts()[3].x
        glabella_x2 = shape.parts()[1].x

        h, w, c = sticker_img.shape

        glabella_w = glabella_x2 - glabella_x1

        nose_w = glabella_w+15
        nose_h = int(h / w * nose_w)

        center_x = shape.parts()[4].x
        center_y = shape.parts()[4].y-20

        nose_x1 = int(center_x - nose_w/2)
        nose_x2 = int(center_x + nose_w/2)
        nose_y1 = int(center_y - nose_h/2)
        nose_y2 = int(center_y + nose_h/2)

        overlay_img = sticker_img.copy()
        overlay_img = cv2.resize(overlay_img, dsize=(nose_w, nose_h))

        overlay_alpha = overlay_img[:, :, 3:4] / 255.0
        background_alpha = 1.0 - overlay_alpha

        img[nose_y1:nose_y2, nose_x1:nose_x2] = overlay_alpha * overlay_img[:, :, :3] + background_alpha * img[nose_y1:nose_y2, nose_x1:nose_x2]


    cv2.imshow('result', img)
    if cv2.waitKey(1) == ord('q'):
        break