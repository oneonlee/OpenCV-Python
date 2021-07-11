import cv2
import numpy as np

# import sys
# sys.stdout = open('out2.txt','w')

init_img = cv2.imread('test.png')
height, width = init_img.shape[:2]

blank_img = np.zeros((height, width, 3), np.uint8)

init_img_gray = cv2.cvtColor(init_img, cv2.COLOR_BGR2GRAY)

# 바이너리 이미지로 변환
ret, imthres = cv2.threshold(init_img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('init_img', init_img)

# 컨투어 계층 트리 (cntr_hierachy.py)
# 모든 컨투어를 트리 계층 으로 수집
contour, hierarchy = cv2.findContours(imthres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 컨투어 갯수와 계층 트리 출력 
print(len(contour), hierarchy)

# 부모노드가 있는 것들만 (외곽이 아닌 것들만) 컨투어 그리기 
for idx, cont in enumerate(contour): 
    if hierarchy[0][idx][3] >= 0:
         mask = cv2.drawContours(blank_img, contour, idx, (255, 255, 255), -1)
    # 컨투어 첫 좌표에 인덱스 숫자 표시 
        # cv2.putText(blank_img, str(idx), tuple(cont[0][0]), cv2.FONT_HERSHEY_PLAIN, 3, (255,255,255))

# 화면 출력
# cv2.imshow('init_img', init_img)
cv2.imshow('blank', blank_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
