# 해상도 향상 모델
- 추가 패키지 설치하기

    옛날 사진이라 해상도가 낮은 사진들이 있을거에요. 해상도를 높이는 모델을 한 번 사용해서 사진의 해상도를 3배로 높여보죠!

    터미널에서 아래 코드를 입력하여 opencv-contrib-python을 설치해줍니다.

    ```bash
    pip install opencv-contrib-python

    윈도우의 경우 pip install --user opencv-contrib-python을 입력해주세요
    ```

- 모델 다운로드

    models 폴더에 저장해주세요.

    [EDSR_x3.pb](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7120b529-6ec2-4fa8-ab26-adc766f67524/EDSR_x3.pb)

- 예제 이미지 다운로드

    저해상도의 이미지를 다운로드해서 준비해요.

    [06.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c8d1b5ce-9b56-4b16-955b-b636e9670093/06.jpg)
    
## 해상도 향상 모델 사용하기

- 모델 로드하기

    ```python
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel('models/EDSR_x3.pb')
    sr.setModel('edsr', 3)
    ```

    우리는 EDSR라는 이름의 모델을 로드할건데요. 이 모델은 이미지의 해상도를 3배로 향상시켜주는 모델입니다. 만약 원본 이미지의 크기가 100x100 사이즈였다면 결과 이미지의 크기는 300x300이 될거에요!

- 이미지 로드하고 추론하기

    ```python
    img = cv2.imread('imgs/06.jpg')

    result = sr.upsample(img)
    ```

    해상도가 낮은 이미지를 로드해주고 sr.upsample() 함수를 사용하여 추론해줍니다. 이 함수는 전처리와 후처리 과정을 함수에서 해줘서 간편해요.

- 결과 이미지 비교하기

    ```python
    resized_img = cv2.resize(img, dsize=None, fx=3, fy=3)

    cv2.imshow('img', img)
    cv2.imshow('resized_img', resized_img)
    cv2.imshow('result', result)
    cv2.waitKey(0)
    ```

    일단 원본 이미지를 cv2.resize()를 사용하여 가로 3배, 세로 3배의 크기로 늘려줍니다. n배로 이미지 크기를 변형하고 싶을 때는 dsize 에 None 을 넣고 fx(너비 배수), fy(높이 배수)를 사용하여 이미지 크기를 변형할 수 있어요.

    우리가 이 과정을 하는 이유는 기본 알고리즘을 사용하여 이미지의 해상도를 3배 늘렸을 때(resized_img)와 화질향상 딥러닝 모델을 사용하여 이미지의 해상도를 3배 늘렸을 때(result) 어떤 차이가 있는지 눈으로 확인하기 위함입니다!

    그리고 각각의 이미지를 출력해보죠!

    왼쪽이 기본 알고리즘으로 해상도를 늘렸을 때, 오른쪽이 딥러닝 모델을 사용하여 해상도를 늘렸을 때 결과 이미지입니다. 차이가 느껴지시나요?
    ![image](https://user-images.githubusercontent.com/73745836/131891965-19dc593f-b41d-4e5a-a5b8-5cea0ddb4de7.png)

- 완성 코드

    ```python
    import cv2

    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel('models/EDSR_x3.pb')
    sr.setModel('edsr', 3)

    img = cv2.imread('imgs/06.jpg')

    result = sr.upsample(img)

    resized_img = cv2.resize(img, dsize=None, fx=3, fy=3)

    cv2.imshow('img', img)
    cv2.imshow('resized_img', resized_img)
    cv2.imshow('result', result)
    cv2.waitKey(0)
    ```
