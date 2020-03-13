.. role:: raw-html-m2r(raw)
   :format: html


fit_predict
====================================================================================================

Fit_predict 명령어 문법 및 연동규격 설명입니다.

개요
----------------------------------------------------------------------------------------------------

이 명령어는 해당 데이터를 선택한 알고리즘으로 기계학습 모델에 TEST set을 넣은 값을 출력합니다.

설명
----------------------------------------------------------------------------------------------------

데이터를 학습하고 싶은 알고리즘(ex:classfication,regeression,clustering,ranking,...)을 선택하여 해당 알고리즘에 맞게 기계학습한 모델을 만들고 저장 여부를 선택합니다. 이 때, 해당 알고리즘 각각의 하이퍼파라미터를 조정하여 사용자가 원하는 모델의 결과 값을 확인할 수 있습니다.

Algorithms
````````````````````````````````````````````````````````````````````````````````````````````````````

각 알고리즘의 사용법은 관련 명령어 문서를 확인해주세요.

.. toctree::
    :glob:

    ml_algorithms/*.rst

Examples
----------------------------------------------------------------------------------------------------


* 검색대상이되는 데이터가 다음과 같이 존재합니다.

.. list-table::
   :header-rows: 1

   * - UPDATE_TIME
     - SYS_OUT
     - OUT_TYPE
     - LAT
     - LON
   * - 2018-03-08  1:00
     - a
     - 37.5
     - 127.5
     - 107
   * - 2018-03-08  1:00
     - b
     - 37
     - 126.5
     - 145
   * - 2018-03-08  1:00
     - c
     - 38.5
     - 126
     - 797
   * - 2018-03-08 1:00
     - a
     - 38
     - 128
     - 456
   * - 2018-03-08 1:00
     - d
     - 36.5
     - 127
     - 41
   * - 2018-03-08 1:00
     - c
     - 37
     - 126
     - 179



* 
  Fit_predict으로 logicsticregression을 적용해 TEST set을 출력하는 명령어 예제입니다.

  .. code-block:: python

     ... | fit_predcit logisr FEATURES LAT,LON LABEL SYS_OUT maxIter=100 regParem=0.01 (INTO modelA)

  명령어 이후 예측 값 출력

.. list-table::
   :header-rows: 1

   * - SYS_OUT
     - LAT
     - LON
     - (PROBABILTY)
     - PREDICTION
   * - a
     - 127.5
     - 107
     - 0.77231
     - a
   * - b
     - 126.5
     - 145
     - 0.67525
     - b
   * - c
     - 126
     - 797
     - 0.22345
     - c
   * - a
     - 128
     - 456
     - 0.22456
     - b
   * - a
     - 126
     - 179
     - 0.23098
     - b
   * - c
     - 127
     - 41
     - 0.45671
     - b


Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: python

   fit_predictCommand : alg option

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - alg
     - *학습 알고리즘입니다.\ :raw-html-m2r:`<br />`\ 예 : LogisticRegression
     - 필수
   * - option
     - 해당 알고리즘의 내부 파라미터 및 모델 저장 이름입니다.\ :raw-html-m2r:`<br />`\ 예 : FEATURES fieldA, fieldB, LABEL target maxIter=100 regParam=0.1 fitIntercept=True INTO modelA
     - 필수


*학습 알고리즘

.. list-table::
   :header-rows: 1

   * - 알고리즘
     - 지정파라미터
     - 필수요소
   * - LogisticRegression
     - Label, Features, regParam, maxIter, name
     - Label, Features, name
   * - SVM
     - Label, Features, regType, maxIter, name
     - Label, Features, name
   * - Decisontree
     - (Label), Features, maxDepth, name
     - (Label), Features, name
   * - RandomForest
     - (Label), Features, numTree, name
     - (Label), Features, name
   * - LinearRegression
     - Label, Features, regParam, name
     - Label, Features, name
   * - Kmeans
     - Features, numk,name
     - Features,numk,name
   * - FPGrowh
     - Features, minSupport, minConfidance, name
     - Features, name


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: python

   fit_command : alg options
   alg : WORD
   options : any
           | options any
   any : WORD
       | NUMBER
       | DOUBLE
       | EQUALS
       | COMMA
       | SPACE
       | DOT
       | TIMES
       | MINUS
       | LBRACKET
       | RBRACKET

   WORD = r'\w+'
   COMMA = r','
   TIMES = r'\*'
   MINUS = r'-'
   EQUALS = r'\='
   SPACE = r'\ '
   DOT = r'\.'
   LBRACKET = r'\['
   RBRACKET = r'\]'
   NUMBER = \d+
   DOUBLE = [-+]?[0-9]+(\.([0-9]+)?([eE][-+]?[0-9]+)?|[eE][-+]?[0-9]+)
