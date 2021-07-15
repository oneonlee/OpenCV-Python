import cv2
import numpy as np
import time

def roi_setting(img, idx, contour):
    mask = np.zeros_like(img, dtype='uint8')
    mask = cv2.drawContours(mask, contour, idx, (1,1,1), -1)
    seprated_slot_img = img * (mask)

    cv2.imshow(f'{idx}', seprated_slot_img)

    return seprated_slot_img

def parking_slot_detection(init_img): # return parking_slot_dict
    init_img_gray = cv2.cvtColor(init_img, cv2.COLOR_BGR2GRAY)

    # 바이너리 이미지로 변환
    ret, imthres = cv2.threshold(init_img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # cv2.imshow('img', init_img)

    # 모든 컨투어를 트리 계층 으로 수집
    contour, hierarchy = cv2.findContours(imthres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    detected_slot_img = np.zeros_like(init_img, dtype='uint8')
    # parking_slot_idx=[]
    parking_slot_dict={}
    # 부모노드가 있는 것들만 (외곽이 아닌 것들만) 컨투어 그리기 
    for idx, cont in enumerate(contour): 
        if hierarchy[0][idx][3] >= 0:
            cv2.drawContours(detected_slot_img, contour, idx, (255,1,1), -1)
            # parking_slot_idx.append(idx)
            parking_slot_dict[idx] = None

            # 컨투어 첫 좌표에 인덱스 숫자 표시
            cv2.putText(detected_slot_img, str(idx), tuple(cont[0][0]), cv2.FONT_HERSHEY_PLAIN, 3, (255,255,255))
    
    cv2.imshow('detected slot  image', detected_slot_img)

    return parking_slot_dict, contour

cap = cv2.VideoCapture("test.mov")

init_img_status = False

# 무한루프
while cap.isOpened():
    ret, img = cap.read()     # 카메라로부터 현재 영상을 받아 img에 저장, 잘 받았다면 ret가 참
    
    if init_img_status == False:
        print("Processing \"capture.png\" file ...")
        time.sleep(1)
        cv2.imwrite("init.png", img)  # 파일이름(한글안됨), 이미지 
        print("Done!")
        init_img_status = True
    else:
        # init_img = cv2.imread('parking.png')
        init_img = cv2.imread('init.png')

        parking_slot_dict, contour = parking_slot_detection(init_img)
        for idx in parking_slot_dict:
            # seprated_slot_img = roi_setting(init_img, idx, contour)
            seprated_slot_img = roi_setting(img, idx, contour)
            parking_slot_dict[idx] = seprated_slot_img
        print(f"총 주차 면 수는 {len(parking_slot_dict)}면 입니다.")
        

    # cv2.imshow('result', img)
    if cv2.waitKey(1) == ord('q'):
        break


cap.release()                       # 캡처 객체를 없애줌
cv2.destroyAllWindows()             # 모든 영상 창을 닫아줌
