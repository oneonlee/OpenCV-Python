# 오래된 흑백 가족사진, 친구와의 사진을 컬러사진으로 복구하는 인공지능 만들기
![image](https://user-images.githubusercontent.com/73745836/131890296-9c8b82fa-c6c1-4b5f-9614-b4f2a61122e0.png)


## 프로젝트 출처
- [http://dlib.net/face_landmark_detection.py.html](http://dlib.net/face_landmark_detection.py.html)

## 모델 준비하기
아래 모델들을 models 폴더에 다운받아 주세요!

- 모델 다운로드
    [models.zip](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0ba535bb-7ef6-4f50-906d-cc46ca5f69e4/models.zip)
    
## Lab 컬러 시스템
이 모델은 이미지를 Lab 컬러로 변경한 후 L 채널을 입력으로 받아 ab 채널을 예측해내는 모델입니다.

![image](https://user-images.githubusercontent.com/73745836/131890959-f16d0dc1-cd7f-4a4f-a099-61d33575705c.png)

Lab 컬러 시스템
L (Luminosity) - 명도, 이미지의 밝기
a - 빨강 / 초록의 보색(a complementary color)축
b - 노랑 / 파랑의 보색(a complementary color)축

BGR과 마찬가지로 Lab 또한 이미지를 표현하는 하나의 체계인데 디자이너들이 여러 종류의 모니터로 같은 사진을 볼 때 차이가 없도록 하기 위해 고안되었다고 해요. 따라서 컬러를 표현하는데 있어서는 괜찮은 컬러 시스템 중에 하나여서 이 모델의 저자가 이 시스템을 채택하여 모델을 작성한 듯 합니다.

우리는 이미지의 명도 값을 추출해내고, 명도 값을 모델에 넣어 나머지 ab 채널의 값을 추론해 낼 거에요. 그리고 추론한 ab 값과 명도 값을 합쳐서 완전한 Lab 이미지를 만들어내고 그걸 다시 BGR 컬러 시스템으로 바꿔서 우리가 볼 수 있게 만들어보죠.

## 그레이스케일 사진에 색 입히기

- 이미지 전처리하기

    모든 딥러닝 모델은 전처리라는 과정이 있습니다. 이번에는 이 모델을 개발한 저자가 어떤 전처리를 했는지 알아볼까요?

    - 이미지 전처리하기

        ```python
        img = cv2.imread('imgs/02.jpg')

        h, w, c = img.shape

        img_input = img.copy()

        img_input = img_input.astype('float32') / 255.
        img_lab = cv2.cvtColor(img_input, cv2.COLOR_BGR2Lab)
        img_l = img_lab[:, :, 0:1]

        blob = cv2.dnn.blobFromImage(img_l, size=(224, 224), mean=[50, 50, 50])
        ```

    - 이미지를 로드하고 img 변수에 저장합니다.
    - 마찬가지로 img의 (높이, 너비, 채널) 을 구해 각각의 변수에 넣습니다.
    - img_input 이라는 변수를 새로 만들어 img 변수 안에 있는 원본 이미지를 복사합니다.
    - img_input 의 타입을 uint8 → float32 로 변경합니다.

        일반적으로 이미지는 uint8 타입을 사용하고 딥러닝 모델은 float32 타입을 사용하기 때문에 변환해주는 과정이 필요합니다.
        딥러닝 모델에서 나온 결과는 float32 → uint8 로 변환하는 과정을 거쳐야지 이미지로 나오겠죠.
        float32 는 32비트 floating point(소수점) 이고 uint8 은 8비트 unsigned integer(부호없는 정수) 라는 것만 알아둡시다.

    - 255로 나누어 0-255 사이의 값을 가지고 있던 픽셀값들을 0-1 사이 값을 가지도록 합니다.
    - 이미지의 컬러 시스템을 BGR 에서 Lab 시스템으로 바꿔줍니다.
    - `img_lab` 에서 L 채널만 사용하기 위해 첫 번째 채널을 추출하여 img_l 에 저장합니다.
    - 지난번과 마찬가지로 `blobFromImage`를 사용하여 `img_l` 에 들어있는 데이터를 너비 224, 높이 224 로 크기를 변형하고 각 픽셀에서 mean 값을 빼줍니다.
  
- 결과 추론하기

    위의 전처리 했던 과정을 보시면 알겠지만 이 모델은 Lab 컬러 시스템에서 L 채널을 입력으로 받아 ab 채널을  추론해내는 모델입니다. 따라서 output 에는 ab 채널의 값이 들어있을 겁니다.

    ```python
    net.setInput(blob)
    output = net.forward()
    ```

    `blob`을 딥러닝 모델에 넣어주고(`setInput`) 결과값을 예상(`forward`)해봅니다. 추론한 결과값은 `output`  변수에 저장됩니다.

- 결과 후처리하기
    - 이미지 후처리하기

        ```python
        output = output.squeeze().transpose((1, 2, 0))

        output_resized = cv2.resize(output, (w, h))

        output_lab = np.concatenate([img_l, output_resized], axis=2)

        output_bgr = cv2.cvtColor(output_lab, cv2.COLOR_Lab2BGR)
        output_bgr = output_bgr * 255
        output_bgr = np.clip(output_bgr, 0, 255)
        output_bgr = output_bgr.astype('uint8')
        ```

    - 차원을 줄여주고 (채널, 높이, 너비) → (높이, 너비, 채널) 순으로 차원 순서를 변경합니다.
    - 이미지를 (224, 224) → 원본 사이즈로 확대합니다.
    - 모델에서 나온 결과값이 ab 채널이므로 앞에 L 채널을 붙여서 이미지를 전체적으로 완성시킵니다.
    - Lab 을 우리가 볼 수 있는 BGR 채널로 다시 변경시킵니다.
    - 모델에 넣기 전에 255 로 나누었으므로 다시 255를 곱합니다.
    - 이상한 값을 없애기위해 0-255 사이에 있는 값이 아니라면 없애버립니다.
    - float32 데이터를 uint8 의 이미지 형태로 변환합니다.

- 결과 출력하기

    ```python
    cv2.imshow('img', img_input)
    cv2.imshow('result', output_bgr)
    cv2.waitKey(0)
    ```

    ![image](https://user-images.githubusercontent.com/73745836/131891071-5a58c175-cf63-4ade-9baa-ee48b7681c9c.png)
    ![image](https://user-images.githubusercontent.com/73745836/131891092-fd22a08b-0975-4459-b8c0-2920167356f2.png)


-완성 코드

    ```python
    import cv2
    import numpy as np

    proto = 'models/colorization_deploy_v2.prototxt'
    weights = 'models/colorization_release_v2.caffemodel'

    net = cv2.dnn.readNetFromCaffe(proto, weights)

    pts_in_hull = np.load('models/pts_in_hull.npy')
    pts_in_hull = pts_in_hull.transpose().reshape(2, 313, 1, 1).astype(np.float32)
    net.getLayer(net.getLayerId('class8_ab')).blobs = [pts_in_hull]

    net.getLayer(net.getLayerId('conv8_313_rh')).blobs = [np.full((1, 313), 2.606, np.float32)]

    img = cv2.imread('imgs/02.jpg')

    h, w, c = img.shape

    img_input = img.copy()

    img_input = img_input.astype('float32') / 255.
    img_lab = cv2.cvtColor(img_input, cv2.COLOR_BGR2Lab)
    img_l = img_lab[:, :, 0:1]

    blob = cv2.dnn.blobFromImage(img_l, size=(224, 224), mean=[50, 50, 50])

    net.setInput(blob)
    output = net.forward()

    output = output.squeeze().transpose((1, 2, 0))

    output_resized = cv2.resize(output, (w, h))

    output_lab = np.concatenate([img_l, output_resized], axis=2)

    output_bgr = cv2.cvtColor(output_lab, cv2.COLOR_Lab2BGR)
    output_bgr = output_bgr * 255
    output_bgr = np.clip(output_bgr, 0, 255)
    output_bgr = output_bgr.astype('uint8')

    cv2.imshow('img', img_input)
    cv2.imshow('result', output_bgr)
    cv2.waitKey(0)
    ```
