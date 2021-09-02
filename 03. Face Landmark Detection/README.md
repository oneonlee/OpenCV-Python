# 얼굴인식 인공지능 스노우 앱 만들기
![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fb358780e-446a-4527-842c-bda824df9c03%2FUntitled.png?table=block&id=66a8a63e-abf9-495e-9eba-81871f39e03d&spaceId=83c75a39-3aba-4ba4-a792-7aefe4b07895&width=1340&userId=&cache=v2)

## 관련 논문
- [Colorful Image Colorization](https://arxiv.org/pdf/1603.08511.pdf)

## 랜드마크
랜드마크는 얼굴의 눈, 코 좌표를 뜻합니다. 양 눈의 끝 좌표와 코 끝의 좌표를 자동으로 알아내서 안경을 씌워보고 돼지코도 만들어봅시다!
![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fa7392d0d-b123-43a7-8957-7818dec232b7%2FUntitled.png?table=block&id=dba109c3-75ff-4ec4-ac12-26d448ec1041&spaceId=83c75a39-3aba-4ba4-a792-7aefe4b07895&width=820&userId=&cache=v2)

- 본격적으로 랜드마크를 탐지해보죠. 랜드마크 탐지 뿐만아니라 이미지 위에 알기쉽게 결과를 그려볼거에요!

- 랜드마크 모델을 로드하는 방법은 간단합니다.

```python
predictor = dlib.shape_predictor('models/shape_predictor_5_face_landmarks.dat')
```

- 랜드마크를 추론하기 위해서는 원본 이미지와 얼굴 영역 탐지 결과가 필요합니다. 이 랜드마크 모델은 이미지의 얼굴 영역 안에서 눈과 코가 어디에 위치하는지 좌표로 알려줍니다. 우리가 로드한 모델에 `img`와 얼굴위치 좌표 `det`을 넣어주면 `shape` 변수에 랜드마크 좌표가 저장됩니다.

    ```python
    dets = detector(img)

    for det in dets:
        shape = predictor(img, det)
    ```

- `shape` 안의 각 좌표에 대해서 점과 글씨를 넣어줍니다.
    - 랜드마크에 점과 글씨 넣기

        ```python
        for i, point in enumerate(shape.parts()):
        	cv2.circle(img, center=(point.x, point.y), radius=2, color=(0, 0, 255), thickness=-1)
        	cv2.putText(img, text=str(i), org=(point.x, point.y), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.8, color=(255, 255, 255), thickness=2)
        ```

    랜드마크 좌표는 shape.parts() 에 눈, 코 순서로 저장됩니다. 랜드마크 좌표를 그려보기위해 `cv2.circle()`로 점을 그리고 `cv2.putText()`를 사용하여 순서대로 숫자를 표시했습니다.

    ![image](https://user-images.githubusercontent.com/73745836/131890045-a32e3f13-18bc-4162-855b-c8e2e348ae02.png)
    위의 결과를 보시면 

    - 0: 오른쪽 눈꼬리
    - 1: 오른쪽 눈 안쪽
    - 2: 왼쪽 눈꼬리
    - 3: 왼쪽 눈 안쪽
    - 4: 코 끝

    순서로 들어간다는 걸 알 수 있죠!


