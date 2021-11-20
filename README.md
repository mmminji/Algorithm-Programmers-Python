# Algorithm-Python-Study

2021.05.10~

1. [프로그래머스 코딩테스트 연습 with 파이썬](https://programmers.co.kr/learn/challenges)  
2. [SW Expert Academy Course Programming - Intermediate](https://swexpertacademy.com/main/learn/course/subjectList.do?courseId=AVuPDN86AAXw5UW6)


# 학습 및 예측
1. 실행방법
- Problem 1 : `python main_problem1.py` 실행
- Problem 2 : `python main_problem2.py` 실행
- 두 파일은 입출력 데이터의 경로와 데이터 전처리 과정이 상이하다.

2. 각 함수의 역할
- preprocessing() : problem 1만 해당하는 함수이며, 피처추출에 관련된 전처리 과정(변수제거)을 수행한다.
- data_preprocessing() : 주어진 학습 데이터를 8:2로 분리하여 학습용, 검증용 데이터로 나눈다.
- model_selection() : 학습용 데이터를 logistic regression, decision tree, support vector machine, random forest, XGB, LGBM, stacking 모델에 학습시키고 검증용 데이터로 각 모델의 성능을 평가한다.
- save() : 그 중 성능이 가장 좋은 모델을 선택하고 저장한다.
- predict() : 평가 데이터에 선택한 모델을 적용하여 예측값을 구하고, 그 값을 txt파일로 저장한다.



# 웹 서버 실행
1. 실행방법
- `python web_server.py` 실행
- [http://127.0.0.1:5000/html/class.html](http://127.0.0.1:5000/html/class.html) 접근  
(URL이 http://127.0.0.1:5000/ 이 아니라면 변경 필요)
- test.sparse.tsv 데이터와 동일한 형식의 한 line을 입력
(예시 : `0 0 0 0 0 0 115 116 1048 3741 87 0 0 121 0 6194 0 0 0 0 0 0 0 23 0 0 0 0 0 0 0 0 0 23 0 0\t1\t1\ta_date:2021-03-15 06:39:47\tc_date:2021-06-07 14:03:58\t0\t2`)
- predict 버튼 클릭
- category 출력값 확인



# 데이터 탐색
1. Problem 1 : sparse 데이터
- 입력 필드는 7차원의 문자형 데이터
- 출력 레이블은 1~22의 클래스
- 입력 데이터 중 1개는 각기 다른 개수의 숫자가 나열되어 있음(변수 의미 해석 불가)
- 입력 데이터 중 2개는 시간 데이터

2. Problem 2 : dense 데이터
- 입력 필드는 200차원의 실수형 데이터
- 출력 레이블은 1~22의 클래스



# 피쳐 추출
1. Problem 1 : sparse 데이터
- 첫번째 변수는 나열된 숫자의 개수도 다르고 각 숫자의 의미를 해석하지 못해 제거하였다.(변수설명이 있었다면 해당 변수를 one-hot으로 바꾸거나 특성에 맞춰 변환 후에 사용 가능하다.)
- 네번째 변수(a_date)와 다섯번째 변수(c_date)는 날짜와 시간을 모두 분리하여 각각 6개의 변수로 변환하려고 하였다. 하지만 기존에 없던 날짜나 시간의 dummy가 생길시 학습용과 평가용 데이터의 변수를 맞출 수 없기 때문에 제거하였다.
- 나머지 변수는 모두 문자형(범주형) 데이터이기 때문에 dummy 변수로 변환하였다.

2. Problem 2 : dense 데이터
- 모든 변수가 실수형 데이터이므로 따로 변수를 제거하거나 선택하지 않았다.


# 모델 선택
- 학습용 데이터 중 일부를 검증용 데이터로 분리하여 7가지 모델을 비교하였다.
- 각 모델 중 정확도가 가장 높은 모델을 선택하였다.


# 평가 및 결과 분석
1. Problem 1
- logistic reg acc :  0.8007
- decision tree acc :  0.802
- svc acc :  0.79855
- random forest acc :  0.73785
- xgb acc :  0.8022
- lgb acc :  0.22965
- stacking acc :  0.79235
- **best model :  XGBClassifier**

2. Problem 2
- logistic reg acc :  0.96265
- decision tree acc :  0.9193
- svc acc :  0.9731
- random forest acc :  0.7082
- xgb acc :  0.93235
- lgb acc :  0.8249
- stacking acc :  0.9661
- **best model :  SVC**



# 추가사항
1. 학습 및 예측 파일을 실행하려면 다음과 같은 구조에 데이터가 위치해야 한다.
├── files.intern.202111
|       ├── test.dense.tsv
|       ├── test.sparse.tsv
|       ├── train.dense.tsv
|       └── train.sparse.tsv
└── LINEAD_ML_강민지
        ├── model
        ├── result
        ├── src
        ├── README.md
        └── requirements.txt

2. `python=3.7.11`을 사용하였으며, 추가로 사용한 가상환경의 라이브러리는 requirements.txt에 저장되어 있다.
