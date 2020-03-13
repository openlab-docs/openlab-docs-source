.. role:: raw-html-m2r(raw)
   :format: html


fit
====================================================================================================

개요
----------------------------------------------------------------------------------------------------

이 명령어는 해당 데이터를 선택한 알고리즘으로 기계학습 모델을 만들어줍니다.

설명
----------------------------------------------------------------------------------------------------

데이터를 학습하고 싶은 알고리즘(ex:classfication,regeression,clustering,ranking,...)을 선택하여 해당 알고리즘에 맞게 기계학습한 모델을 만들어줍니다. 이 때, 해당 알고리즘 각각의 하이퍼파라미터를 조정하여 사용자가 원하는 모델을 만들어줍니다.

Algorithms
````````````````````````````````````````````````````````````````````````````````````````````````````

각 알고리즘의 사용법은 관련 명령어 문서를 확인해주세요.

1. `RandomForest Classification <ml_algorithms/RandomForestClassification.html>`_
2. `RandomForest Regression <ml_algorithms/RandomForestRegression.html>`_
3. `Spark DecisionTree Classification <ml_algorithms/SparkDecisionTreeClassification.html>`_
4. `Spark DecisionTree Regression <ml_algorithms/SparkDecisionTreeRegression.html>`_
5. `Spark FP-Growth <ml_algorithms/SparkFPGrowth.html>`_
6. `Spark Kmeans <ml_algorithms/SparkKmeans.html>`_
7. `generalizedLinearRegression <ml_algorithms/generalizedlinearregression.html>`_
8. `linearRegression <ml_algorithms/linearregression.html>`_
9. `logisticRegression <ml_algorithms/logisticregression.html>`_

Examples
----------------------------------------------------------------------------------------------------

LogisticRegression을 학습하는 예제 입니다.

검색대상이되는 데이터가 다음과 같이 존재합니다.

.. list-table::
   :header-rows: 1

   * - a
     - b
     - s
     - d
     - Species
     - minmax_a
     - minmax_b
     - minmax_c
     - minmax_d
     - Label
   * - 5.1
     - 3.5
     - 4
     - 0.2
     - Iris-setosa
     - 0.222222
     - 0.625
     - 0.508475
     - 0.041667
     - 0
   * - 4.9
     - 3
     - 1.4
     - 0.2
     - Iris-setosa
     - 0.166667
     - 0.416667
     - 0.067797
     - 0.041667
     - 0
   * - 4.7
     - 3.2
     - 1.3
     - 0.2
     - Iris-setosa
     - 0.111111
     - 0.5
     - 0.050847
     - 0.041667
     - 0
   * - 4.6
     - 3.1
     - 1.5
     - 0.2
     - Iris-setosa
     - 0.083333
     - 0.458333
     - 0.084746
     - 0.041667
     - 0
   * - 5
     - 3.6
     - 1.4
     - 0.2
     - Iris-setosa
     - 0.194444
     - 0.666667
     - 0.067797
     - 0.041667
     - 0
   * - 7
     - 3.2
     - 4.7
     - 1.4
     - Iris-versicolor
     - 0.75
     - 0.5
     - 0.627119
     - 0.541667
     - 2
   * - 6.4
     - 3.2
     - 4.5
     - 1.5
     - Iris-versicolor
     - 0.583333
     - 0.5
     - 0.59322
     - 0.583333
     - 2
   * - 6.8
     - 3.2
     - 5.9
     - 2.3
     - Iris-virginica
     - 0.694444
     - 0.5
     - 0.830508
     - 0.916667
     - 1
   * - 6.7
     - 3.3
     - 5.7
     - 2.5
     - Iris-virginica
     - 0.666667
     - 0.541667
     - 0.79661
     - 1
     - 1


Fit으로 logicsticregression을 적용해 분류 하는 모델을 생성하는 명령어 예제입니다.

.. code-block:: none

   ... | fit LogisticRegression FEATURES minmax_a,minmax_b,minmax_c,minmax_d LABEL label maxIter=100 regParam=0.1 fitIntercept=True INTO modelA

명령어 이후 모델 저장

.. list-table::
   :header-rows: 1

   * - index
     - category
     - algorithm
     - Model_name
     - saved_date
     - features
     - label
     - parameters
     - Evaluation
     - crossvalidation
     - grid_info
     - used_data_count
     - spent_seconds
     - user
   * - 1
     - Classfication
     - LogisticRegresssion
     - ModelA
     - 20190909102754
     - LAT, LON
     - SYS_OUT
     - (maxIter:100,regParam:0.01,...)
     - (Accuracy:99,pricison:99,recall:10,...)
     - {}
     - {}
     - 100
     - 5 sec
     - None


Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   fitCommand : alg option

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

.. code-block:: none

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

추가 개발 사항(Issue)
----------------------------------------------------------------------------------------------------


* Merge_dataframe 실행 시 df가 섞이는 현상이 발생함 sort 후 섞는 기능 추가.
* model metadata Evaluation에 summary 사용 불가, 여러 성능 지표 계산 기능 추가.
* 겹치는 함수 및 Tensorflow 확장성을 위해 내부 함수들을 fit단계로 올려할 것.

추가 개발 방향
----------------------------------------------------------------------------------------------------


* Running_curve : 데이터량에 따라 학습이 얼마나 잘 진행되고 있는지 알려줄 수 있는 데이터를 return값에 포함 시켜줍니다. Data-Discovery-Service내에서 따로 시각화해서 확인 할수 있게 설계합니다. 기본적인 기능 구현을 우선시하여 뒤로 밀린 개발사항입니다.
* Sampling : 학습 알고리즘 내부에서 알아서 training/test 데이터를 나눠주는지 확인하지 못 하였습니다. 만약 스스로 나누지 않는다면 구현해야할 사항입니다. 역시 우선순위는 뒤로 밀렸습니다.
* CrossValidation : 교차검증기능 역시 알고리즘 내부에서 자동으로 이루어지는지 확인해 봐야 합니다. 스스로 이루어지지 않을 시에는 옵션으로 구현해야합니다. 역시 우선순위는 뒤로 밀렸습니다.
* Overfit,Underfit : 두 가지 경우에 어떻게 해줄지 생각을 하고 설계 및 개발을 해줘야한다.
