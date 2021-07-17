<img width="1386" alt="스크린샷 2021-07-15 오후 6 22 40" src="https://user-images.githubusercontent.com/73745836/125781413-d81b7b68-6470-437e-ba14-0e75deace483.png">
# 스마트 해상물류 OpenCV 프로젝트

## 7월 11일

<img width="1077" alt="스크린샷 2021-07-11 오후 2 25 21" src="https://user-images.githubusercontent.com/73745836/125183723-d6de7c00-e253-11eb-892e-58426bfceb6b.png">

1. 이미지를 바이너리 이미지로 변환
2. 모든 컨투어를 트리 계층 으로 수집
3. 수집한 컨투어 중, 부모 노드가 있는 것들만 (즉, 외곽이 아닌 것들만) 컨투어 그리기 
  - 두께를 -1로 해주어 윤곽선 안 쪽을 흰색으로 모두 채움

## 7월 15일

<img width="1169" alt="스크린샷 2021-07-15 오후 5 06 46" src="https://user-images.githubusercontent.com/73745836/125752557-34db0751-6fd3-49fc-bfa2-4ac17ee93143.png">

mask로 각각의 자리만을 나타냄.

---

<img width="1386" alt="스크린샷 2021-07-15 오후 6 22 40" src="https://user-images.githubusercontent.com/73745836/125781450-39500278-b5f7-4f18-8c7b-d2f93d55ac2f.png">

분할된 각각의 자리에서 차량 주차 현황을 확인할 수 있음

## 7월 18일 

<img width="1440" alt="스크린샷 2021-07-17 오후 2 04 32" src="https://user-images.githubusercontent.com/73745836/126044848-e062636c-486a-410f-bffa-0e38d87be975.png">

새로운 각도의 동영상을 기존의 코드로 돌려보았을 때, 빛반사로 인해 노이즈가 생기는 현상을 확인할 수 있음

---

<img width="1391" alt="스크린샷 2021-07-18 오전 2 17 04" src="https://user-images.githubusercontent.com/73745836/126044964-89daed00-c9ba-41e1-9a31-241abd727118.png">

* 기존의 ```grayscale → binary```의 전처리 과정을
* ```Converting Grayscale → Blurring → Canny Edge Detection → Dilation Morphological Operation```로 수정하여 노이즈를 제거하고 원하는 결과를 얻음
