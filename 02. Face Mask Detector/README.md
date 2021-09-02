# [COVID-19] 마스크를 썼는지 안썼는지 알아내는 인공지능 만들기

![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fb7d5a589-739f-4d2f-88ab-95513067d3a0%2FUntitled.png?table=block&id=41a53e02-12e3-424e-bbd5-2be34facd3f0&spaceId=83c75a39-3aba-4ba4-a792-7aefe4b07895&width=2120&userId=&cache=v2)

## 관련 아티클

- [COVID-19: Face Mask Detector with OpenCV, Keras/TensorFlow, and Deep Learning](https://www.pyimagesearch.com/2020/05/04/covid-19-face-mask-detector-with-opencv-keras-tensorflow-and-deep-learning/)

## 딥러닝 모델 다운로드

아래의 파일들을 models 폴더에 다운받아주세요.

- 얼굴 영역 탐지 모델 & 마스크 판단 모델 다운로드
  - [models.zip](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/03cac2ba-9c9d-4ce7-b77f-4c2ffb79fdea/models.zip)

## 패키지 불러오기

main.py 에 아래 코드를 작성합니다.

- 패키지 로드하기

  ```python
  from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
  from tensorflow.keras.models import load_model
  import numpy as np
  import cv2
  ```
## 모델 로드하기

얼굴 영역 탐지 모델과 마스크 판단 모델을 각각 로드해봐요.

- 모델 로드하기

  ```python
  facenet = cv2.dnn.readNet('models/deploy.prototxt', 'models/res10_300x300_ssd_iter_140000.caffemodel')
  model = load_model('models/mask_detector.model')
  ```

  facenet 이 얼굴 영역 탐지 모델이고 model 이 마스크 판단 모델이에요.
