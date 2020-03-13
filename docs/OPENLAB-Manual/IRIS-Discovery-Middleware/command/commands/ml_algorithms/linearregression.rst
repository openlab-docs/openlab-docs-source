.. role:: raw-html-m2r(raw)
   :format: html


linearRegression
====================================================================================================

개요
----------------------------------------------------------------------------------------------------

지도학습을 하는 선형회귀 알고리즘입니다.

설명
----------------------------------------------------------------------------------------------------

지도학습을 하는 선형회귀 알고리즘입니다.

Example
----------------------------------------------------------------------------------------------------

집값에 대한 샘플데이터 입니다.

.. list-table::
   :header-rows: 1

   * - crim(범죄율)
     - age(연식)
     - tax(세금)
     - medv(집값)
   * - 0.671909988
     - 90.30000305
     - 307
     - 16.60000038
   * - 1.002449989
     - 87.30000305
     - 307
     - 21
   * - 8.055789948
     - 95.40000153
     - 666
     - 13.80000019
   * - ...
     - ...
     - ...
     - ...


fit으로 LinearRegression을 적용해 feature와 label의  선형 상관관계를 모델링하는 명령어 예제입니다.

crim, age, tax을 feature로, medv을 label로 학습하고 modelA로 저장합니다. (옵션은 100번 반복, feature 표준화입니다.)

.. code-block:: none

   * | fit linearregression FEATURES crim, age, tax LABEL medv maxIter=100 standardization=True INTO modelA

.. list-table::
   :header-rows: 1

   * - features
     - estimate
     - coefficientStandardErrors
     - space
     - meanAbsoluteError
     - rootMeanSquaredError
     - r2
   * - intercept
     - 33.470874208
     - 0.050606818157
     - |
     - 5.6438527876
     - 7.8910514027
     - 0.26239019966
   * - crim
     - -0.17025122296
     - 0.014574116347
     - |
     - None
     - None
     - None
   * - age
     - -0.057344502576
     - 0.0028028265109
     - |
     - None
     - None
     - None
   * - tax
     - -0.015653811458
     - 1.1493026629
     - |
     - None
     - None
     - None


predict로 modelA에 샘플 데이터를 다시 넣어 예측하는 명령어 예제입니다.

.. code-block:: none

   * | predict modelA crim, age, tax

.. list-table::
   :header-rows: 1

   * - crim
     - age
     - tax
     - medv
     - prediction
   * - 0.671909988
     - 90.30000305
     - 307
     - 16.60000038
     - 23.372551835
   * - 1.002449989
     - 87.30000305
     - 307
     - 21
     - 23.488310504
   * - 8.055789948
     - 95.40000153
     - 666
     - 13.80000019
     - 21.022852399
   * - ...
     - ...
     - ...
     - ...
     - ...


fit_predict로 LinearRegression을 적용해 feature와 label의 선형 상관관계를 모델링 후 예측하는 명령어 예제입니다.

.. code-block:: none

   * | fit_predict linearregression features lstat,tax LABEL medv maxIter=100 standardization=True INTO modelA

Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   SparkLinearRegression_command : FEATURES fields LABEL l_field params INTO model

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - FEATURES fields
     - 학습에 사용될 특징 column을 입력 받습니다.
     - 필수
   * - LABEL l_field
     - 학습에 사용될 라벨 column을 입력 받습니다.
     - 필수
   * - params
     - *알고리즘 옵션을 지정해줍니다.
     - 필수
   * - INTO model
     - 모델을 저장해주는 예약어 입니다. :raw-html-m2r:`<br />`\ 경로 (\ **/B-IRIS/USERS/dani/ML/**\ )에 모델, 모델 메타 데이터가 저장됩니다.\ :raw-html-m2r:`<br />`\ 예 : into modelA
     - 옵션


*알고리즘 옵션

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 기본값
   * - maxIter
     - 학습 반복 수
     - 100
   * - regParam
     - 정규화 계수 값
     - 0.0
   * - elasticNetParam
     - 정규화 함수 타입으로 ``0.0~1.0``\ 의 범위\ :raw-html-m2r:`<br />`\ 1.0에 가까울수록 'L1' 타입, 0.0에 가까울수록 'L2' 타입
     - 0.0
   * - fitintercept
     - 훈련 데이터에 대한 증간된 표현을 사용할지 안 할지 정해주는 Boolean (편향을 학습에 사용할지 안 할지)
     - True
   * - tol
     - 최적화 함수에 대한 반복 수렴 오차 값.
     - 1e-06
   * - standardization
     - 모델 fitting 전에 training 특징들을 표준화 해줄지 안 해줄지 정합니다.
     - False
   * - solver
     - 최적화 알고리즘을 정합니다. (Normal, l-bfgs, auto)
     - auto


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   SparkLinearRegression_command : FEATURES fields LABEL l_field params INTO_model
   fields : field
          | fields COMMA field
   field : WORD
         | TIMES
         | MINUS WORD
   l_field : WORD
   params : param
          | params param
          |
   param : WORD EQUALS WORD
         | WORD EQUALS DOUBLE
         | WORD EQUALS LBRACKET words RBRACKET
         | WORD EQUALS LBRACKET doubles RBRACKET
   words : WORD
         | words COMMA WORD
   doubles : DOUBLE
           | doubles COMMA DOUBLE
   INTO_model : INTO WORD
              |

   WORD = \w+
   COMMA = \,
   FEATURES = FEATURES | features
   LABEL = LABEL | label
   INTO = INTO
   EQUALS = \=
   TIMES = \*
   MINUS = -
   LBRACKET = \[
   RBRACKET = \]
   DOUBLE = [-+]?[0-9]+(\.([0-9]+)?([eE][-+]?[0-9]+)?|[eE][-+]?[0-9]+)
