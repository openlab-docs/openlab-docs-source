.. role:: raw-html-m2r(raw)
   :format: html


generalizedLinearRegression
====================================================================================================

개요
----------------------------------------------------------------------------------------------------

Linaer Regression에서 각각의 column에 대한 중요도를 뽑아내지 못 하여 해당 알고리즘을 추가 했습니다.

설명
----------------------------------------------------------------------------------------------------

비 정규 분포를 따르는 응답에 적용하기 위해 일반화 선형 모델(generalized linear regression)을 사용합니다.
family 분포도는 사용자가 스스로 결정해야합니다.

Examples
----------------------------------------------------------------------------------------------------

집값에 대한 샘플데이터 입니다.

.. list-table::
   :header-rows: 1

   * - indus
     - rm
     - dis
     - tax
     - lstat
     - medv
   * - 2.309999943
     - 6.574999809
     - 4.090000153
     - 296
     - 4.980000019
     - 24
   * - 7.070000172
     - 6.421000004
     - 4.967100143
     - 242
     - 9.140000343
     - 21.60000038
   * - 7.070000172
     - 7.184999943
     - 4.967100143
     - 242
     - 4.03000021
     - 34.70000076
   * - 2.180000067
     - 6.998000145
     - 6.062200069
     - 222
     - 2.940000057
     - 33.40000153
   * - ...
     - ...
     - ...
     - ...
     - ...
     - ...


.. list-table::
   :header-rows: 1

   * - 속성
     - 설명
   * - CRIM
     - 마을별 범죄율
   * - ZN
     - 주거지의 비율
   * - INDUS
     - 공업 지의 비율
   * - CHAS
     - 강변 위치 여부
   * - NOX
     - 대기 중 질소 산화물 농도
   * - RM
     - 가구당 방의 개수
   * - AGE
     - 1940년 전에 지어진 집의 비율
   * - DIS
     - 일터와의 평균 거리
   * - RAD
     - 고속도로 접근성
   * - TAX
     - 재산세율
   * - PTRATIO
     - 마을 별 학생-교사 비율
   * - B
     - 흑인 주거 비율
   * - LSTAT
     - 저소득층 주거 비율
   * - MEDV
     - 집값 중간값


fit으로 generalized linear regression 적용해 분류 하는 모델을 생성하는 명령어 예제입니다.

.. code-block:: none

   * | fit GeneralizedLinearRegression FEATURES rm,tax,indus,lstat,dis LABEL medv maxIter=100 regParam=0.1 fitIntercept=True solver=irls INTO modelB

.. list-table::
   :header-rows: 1

   * - features
     - estimate
     - coefficientStandardErrors
     - tValues
     - pValues
     - space
     - dispersion
     - rmse
     - r2
     - mae
   * - intercept
     - 8.3766
     - 3.431
     - 2.4415
     - 0.015
     - |
     - 28.2425
     - 5.2828
     - 0.6694
     - 3.7289
   * - rm
     - 4.7425
     - 0.432
     - 10.9786
     - 0
     - |
     - None
     - None
     - None
     - None
   * - tax
     - -0.0078
     - 0.002
     - -3.8132
     - 0.0002
     - |
     - None
     - None
     - None
     - None
   * - indus
     - -0.1239
     - 0.0612
     - -2.0267
     - 0.0432
     - |
     - None
     - None
     - None
     - None
   * - lstat
     - -0.6136
     - 0.0499
     - -12.29
     - 0
     - |
     - None
     - None
     - None
     - None
   * - dis
     - -0.8767
     - 0.161
     - -5.4454
     - 0
     - |
     - None
     - None
     - None
     - None


predict로 modelB에 샘플 데이터를 다시 넣어 예측하는 명령어 예제입니다.

.. code-block:: none

   * | predict modelB rm,tax,indus,lstat,dis

fit_predict로 generalized linear regression 적용해 분류 하는 모델을 생성하고 예측하는 명령어 예제입니다.

.. code-block:: none

   * | fit_predict GeneralizedLinearRegression FEATURES rm,tax,indus,lstat,dis LABEL medv maxIter=100 regParam=0.1 fitIntercept=True solver=irls INTO modelB

.. list-table::
   :header-rows: 1

   * - indus
     - rm
     - dis
     - tax
     - lstat
     - medv
     - prediction
   * - 2.309999943
     - 6.574999809
     - 4.090000153
     - 296
     - 4.980000019
     - 24
     - 30.327170453
   * - 7.070000172
     - 6.421000004
     - 4.967100143
     - 242
     - 9.140000343
     - 21.60000038
     - 26.105575673
   * - 7.070000172
     - 7.184999943
     - 4.967100143
     - 242
     - 4.03000021
     - 34.70000076
     - 32.864401681
   * - 2.180000067
     - 6.998000145
     - 6.062200069
     - 222
     - 2.940000057
     - 33.40000153
     - 34.881037647
   * - ...
     - ...
     - ...
     - ...
     - ...
     - ...
     - ...


Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   SparkGeneralizedLinearRegression_command : FEATURES fields LABEL l_field params INTO_model

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - FEATURES fields
     - 학습에 사용될 특징 column을 입력 받습니다.
     - 필수
   * - LABEL l_fiedls
     - 학습에 사용될 라벨 column을 입력 받습니다.
     - 필수
   * - params
     - *알고리즘 옵션을 지정해줍니다.
     - 필수
   * - INTO_model
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
   * - fitintercept
     - 훈련 데이터에 대한 증간된 표현을 사용할지 안 할지 정해주는 Boolean (편향을 학습에 사용할지 안 할지)
     - True
   * - tol
     - 최적화 함수에 대한 반복 수렴 오차 값.
     - 1e-06
   * - solver
     - 최적화 알고리즘을 정합니다.
     - irls
   * - family
     - 모델에 사용되는 오류 분포 (gaussian, binomial, poisson, gamma and tweedie)
     - gaussian
   * - link
     - 선형적인 예측과 분포 함수의 평균사이의 관계를 제공해주는 함수 (identity, log, inverse, logic, probit, cloglog, sort)
     - identity


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   SparkGeneralizedLinearRegression_command : FEATURES fields LABEL l_field params INTO_model
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

Problems
----------------------------------------------------------------------------------------------------


* 
  구현 문제인지, 다른 문제인지 확인 불가

  .. code-block:: none

     File"/Users/jungjunhwang/Desktop/work/code/fit_work/SparkGenerlizedLinearRegression.py", line 245, in modeling eval_dict['pValues'] = summary.pValues

     File "/Users/jungjunhwang/spark-2.2.0-bin hadoop2.7/python/pyspark/ml/regression.py", line 1719, in pValues
         return self._call_java("pValues")

     IllegalArgumentException: u'requirement failed: degreesOfFreedom must be positive, but got -4.0'

  로컬 테스트시 column의 갯수 혹은 column들의 관계에 따라 pValue 값을 계산하지 못함.

  Data-Discovery-Service 서버 테스트 시 정상작동 그러나, 값이 정확한지 확인 불가.

  .. code-block:: none

     <angora Test Command>
     ... | fit SparkGeneralizedLinearRegression features * LABEL medv maxIter=100 INTO modelD

* 
  값이 정확한지 확인 불가.

  .. code-block:: none

     <angora Test Command>
     ... | fit SparkGeneralizedLinearRegression FEATURES rm,tax,indus,lstat,crim,age,b,rad LABEL medv maxIter=100 regParam=0.1 fitIntercept=True INTO modelD

Data-Discovery-Service_TEST

.. list-table::
   :header-rows: 1

   * - Coeffiecient
     - estimate
     - standError
     - tValues
     - pValues
   * - intercept
     - -3.3659
     - 0.4538
     - 11.2661
     - 0.0
   * - rm
     - 5.1128
     - 0.0041
     - -3.5127
     - 0.0005
   * - tax
     - -0.0144
     - 0.0604
     - 0.7848
     - 0.433
   * - indus
     - 0.0474
     - 0.057
     - -9.8506
     - 0.0
   * - lstat
     - -0.5619
     - 0.0368
     - -1.9531
     - 0.0514
   * - crim
     - -0.0719
     - 0.0123
     - 1.3831
     - 0.1673
   * - age
     - 0.017
     - 0.003
     - 3.1231
     - 0.0019
   * - b
     - 0.0094
     - 0.0717
     - 2.8293
     - 0.0049
   * - rad
     - 0.2028
     - 3.6905
     - -0.9121
     - 0.3622

