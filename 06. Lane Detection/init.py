import cv2
import numpy as np

def roi_setting(init_img, idx, contour):
    
    # test = np.zeros_like(init_img, dtype='uint8')
    # test = cv2.drawContours(test, contour, idx, (255,255,255), -1)
    # cv2.imshow(f'{idx}', test)

    mask = np.zeros_like(init_img, dtype='uint8')
    mask = cv2.drawContours(mask, contour, idx, (1,1,1), -1)
    seprated_slot_img = init_img * (mask)

    cv2.imshow(f'{idx}', seprated_slot_img)
    # cv2.imshow('detected slot image', detected_slot_img)


def parking_slot_detection(init_img): # return parking_slot_dict
    init_img_gray = cv2.cvtColor(init_img, cv2.COLOR_BGR2GRAY)

    # 바이너리 이미지로 변환
    ret, imthres = cv2.threshold(init_img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # cv2.imshow('img', init_img)

    # 모든 컨투어를 트리 계층 으로 수집
    contour, hierarchy = cv2.findContours(imthres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    detected_slot_img = np.zeros_like(init_img, dtype='uint8')
    parking_slot_idx=[]
    # 부모노드가 있는 것들만 (외곽이 아닌 것들만) 컨투어 그리기 
    for idx, cont in enumerate(contour): 
        if hierarchy[0][idx][3] >= 0:
            cv2.drawContours(detected_slot_img, contour, idx, (255,1,1), -1)
            parking_slot_idx.append(idx)

            # 컨투어 첫 좌표에 인덱스 숫자 표시
            cv2.putText(detected_slot_img, str(idx), tuple(cont[0][0]), cv2.FONT_HERSHEY_PLAIN, 3, (255,255,255))

    print(f"총 주차 면 수는 {len(parking_slot_idx)}면 입니다.")
    
    cv2.imshow('detected slot  image', detected_slot_img)


    return parking_slot_idx, contour

###########################################################################



init_img = cv2.imread('parking.png')


parking_slot_idx, contour = parking_slot_detection(init_img)

for idx in parking_slot_idx:
    roi_setting(init_img, idx, contour)

cv2.waitKey(0)
cv2.destroyAllWindows()