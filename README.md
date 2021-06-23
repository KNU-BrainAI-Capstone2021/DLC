# 2021 DLC

## Member
|name |   |
|-----|---|
|김현민| Hyunmin-K |
|이광열| choco1692 |
|손건웅| acushla39 |
|제갈건| geon-j    |

# Objection
 딥러닝을 활용한 가상 피팅 시스템

## 1학기 프로젝트
 물체 인식 기술을 이해하고 특정 데이터셋을 활용해 물체 인식  
 ![KakaoTalk_20210408_193219579](https://user-images.githubusercontent.com/79971598/114018699-7e8c8c80-98a8-11eb-9535-584f076117ce.png)


 
## Concept
 CNN을 기반으로 한 Object detection을 활용하여, 의상을 인식하고 이를 추출하는 것   
  ![image](https://user-images.githubusercontent.com/79971598/123065142-de2b1a80-d449-11eb-83ef-11b1cbd5c8e2.png)   
  
  ![image](https://user-images.githubusercontent.com/79971598/123061438-9c4ca500-d446-11eb-91f8-7df6cc8cff38.png)   
   
  
### Model
 Yolo V3   
  ![image](https://user-images.githubusercontent.com/79971598/123057002-6f968e80-d442-11eb-864e-fac530933433.png)   
 
 1-stage detector   
  ![image](https://user-images.githubusercontent.com/79971598/123057634-019e9700-d443-11eb-944b-65752efd4ec5.png)   
   
   
### Backbone
 darknet-53   
  ![image](https://user-images.githubusercontent.com/79971598/123063090-129dd700-d448-11eb-9c91-de436d56c40d.png)     
 
 downsample으로 block이 구분   


### Data preprocessing
 LetterBoxing   
![image](https://user-images.githubusercontent.com/79971598/123058688-09127000-d444-11eb-8c3e-a595c0a4e7be.png)

 resize   
  320 × 320 : 작고 정확도는 떨어지지 만 속도 빠름   
  609 × 609 : 정확도는 더 높지만 속도 느림   
  416 × 416 : 중간   
     
     
### Parameter
 ![image](https://user-images.githubusercontent.com/79971598/123058433-c94b8880-d443-11eb-8a39-dff9615d633d.png)   
 ![image](https://user-images.githubusercontent.com/79971598/123064247-11b97500-d449-11eb-982f-7458da992cc2.png)   
   
### Dataset
  Deepfashion2   
 ![image](https://user-images.githubusercontent.com/79971598/123065458-1f232f00-d44a-11eb-8c24-ce16635db009.png)
   
   
### 2학기 프로젝트
 사람 체형을 인식하여 의상의 사이즈를 조절 후 실제로 입은 것처럼 표현  
 ![KakaoTalk_20210408_202015656](https://user-images.githubusercontent.com/79971598/114018205-f312fb80-98a7-11eb-9de4-509e83e77556.png)

## 참조 Link
 https://curiousily.com/posts/object-detection-on-custom-dataset-with-yolo-v5-using-pytorch-and-python/  
 https://youtu.be/mQXOnOdhSOk  
 https://www.youtube.com/watch?v=hL-gJXgscOc  
 https://syncedreview.com/2020/04/07/deep-fashion3d-dataset-benchmark-for-virtual-clothing-try-on-and-more/  
