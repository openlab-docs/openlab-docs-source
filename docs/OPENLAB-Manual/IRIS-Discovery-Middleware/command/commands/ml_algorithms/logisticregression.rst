.. role:: raw-html-m2r(raw)
   :format: html


logisticRegression(LBFGS)
====================================================================================================

Logistic Regression 학습 알고리즘 파라미터 설명서 입니다.

개요
----------------------------------------------------------------------------------------------------

Logistic Regression 이진 분류에 많이 사용되는 학습 알고리즘입니다. 최적화 알고리즘은 LBFGS를 사용합니다.

**현재 Binary 분류는 구현이 안되있는 상태입니다.**
**LogisticRegression 멀티 클래스만 지원하는 상태입니다.**

설명
----------------------------------------------------------------------------------------------------

이진분류에 주로 사용되지만 다중 분류에도 사용할수 있는 학습 알고리즘입니다. 최적화 알고리즘으로 SGD, LBFGS를 사용할 수 있지만 현재 저희가 제공하는 최적화 알고리즘 LBFGS를 사용합니다.

Examples
----------------------------------------------------------------------------------------------------

Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   ... | fit LogisticRegression FEATURES fields LABEL l_fields INTO_model

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - FEATURES
     - 학습에 사용될 특징 column을 입력 받습니다.
     - 필수
   * - LABEL
     - 학습에 사용될 라벨 column을 입력 받습니다.
     - 필수
   * - fields
     - 특징 column들의 이름입니다.
     - 필수
   * - l_fields
     - 라벨 column들의 이름입니다.
     - 필수
   * - params
     - 알고리즘 setting 파라미터들입니다.
     - 옵션
   * - INTO_model
     - ``INTO model_name``\ 으로 이루어져 있습니다. 경로 (\ **/Biris/angora/ml**\ )에 모델 메타 데이터와 함께 저장합니다.
     - 필수
   * - maxIter
     - 학습 반복 수 (default : 100)
     - 옵션
   * - regParam
     - 정규화 계수 값 (default : 0.0)
     - 옵션
   * - elasticNetParam
     - 정규화 함수 타입 (default : L2)\ :raw-html-m2r:`<br/>`\ ``0.0~1.0`` : 1.0에 가까울수록 'L1' 타입, 0.0에 가까울수록 'L2' 타입
     - 옵션
   * - fitintercept
     - 훈련 데이터에 대한 증간된 표현을 사용할지 안 할지 정해주는 Boolean (편향을 학습에 사용할지 안 할지 default : True)
     - 옵션
   * - tol
     - L-BFGS에 대한 반복 수렴 오차 값 (default : 1e-06)
     - 옵션
   * - threshold
     - 이진 분류되는 임계 값 (default : 0.5)
     - 옵션


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   SparkRandomForestRegression_command : FEATURES fields LABEL l_field params INTO_model

   fields : field
           | fields COMMA field

   field : WORD
           | TIMES
           | MINUS WORD

   l_field : WORD

   params : param
           | params param

   param : WORD EQUALS WORD
           | WORD EQUALS DOUBLE
           | WORD EQUALS LBRACKET words RBRACKET
           | WORD EQUALS LBRACKET doubles RBRACKET

   words : WORD
           | words COMMA WORD

   doubles : DOUBLE
           | doubles COMMA DOUBLE

   INTO_model : INTO WORD

   WORD : \w+
   COMMA : \,
   FEATURES : FEATURES | features
   LABEL : LABEL | label
   INTO : INTO
   EQUALS : \=
   TIMES : \*
   MINUS : \-
   LBRACKET : \[
   RBRACKET : \]
   DOUBLE : [-+]?[0-9]+(\.([0-9]+)?([eE][-+]?[0-9]+)?|[eE][-+]?[0-9]+)


   params : maxIter=100, regParam=0.0, elasticNetParam=0.0, tol=1e-06, fitIntercept=True, threshold=0.5
