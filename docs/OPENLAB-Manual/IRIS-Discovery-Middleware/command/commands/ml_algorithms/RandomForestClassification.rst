.. role:: raw-html-m2r(raw)
   :format: html


RandomForest Classification
====================================================================================================

개요
----------------------------------------------------------------------------------------------------

RandomForest는 Classification / Regression에 모두 사용 할 수 있으며, 특정 값이 누락되어 있어도 사용 할 수 있습니다.

설명
----------------------------------------------------------------------------------------------------

여러개의 Decision Tree를 만들고 *앙상블 기법으로 결과를 결정합니다. 때문에, 오버피팅을 방지할 수 있습니다.

*앙상블 기법 : 여러개의 모델을 학습시켜 그 모델들의 예측결과들을 이용해 하나의 모델보다 더 나은 값을 예측하는 방법

Examples
----------------------------------------------------------------------------------------------------

꽃받침, 꽃잎의 종류에 따른 종의 종류에 대한 샘플데이터 입니다.

.. list-table::
   :header-rows: 1

   * - *sepal_length
     - sepal_width
     - *petal_length
     - petal_width
     - *species
   * - 5.1
     - 3.5
     - 4
     - 0.2
     - Iris-setosa
   * - 4.9
     - 3
     - 1.4
     - 0.2
     - Iris-setosa
   * - 5.2
     - 2.7
     - 3.9
     - 1.4
     - Iris-versicolor
   * - 5
     - 2
     - 3.5
     - 1
     - Iris-versicolor
   * - 6.4
     - 3.2
     - 5.3
     - 2.3
     - Iris-virginica
   * - 6.5
     - 3
     - 5.5
     - 1.8
     - Iris-virginica
   * - ...
     - ...
     - ...
     - ...
     - ...


*sepal_length: 꽃받침 조각 길이

*petal_length : 꽃잎 길이

*species : 종

fit으로 RandomForestClassification 적용해 분류 하는 모델을 생성하는 명령어 예제입니다.

(앞의 indexer쿼리문은 라벨정보가 되는 ``species``\ 를 ``0, 1, 2``\ 로 바꿔주는 전처리를 수행합니다.)

.. code-block:: none

   * | indexer species to s | fit RandomForestClassification FEATURES sepal_length,sepal_width,petal_length,petal_width LABEL s maxDepth=10 INTO modelD

.. list-table::
   :header-rows: 1

   * - features
     - generalizeGini
     - space
     - numTrees
     - numClasses
     - space2
     - accuracy
     - precision
     - f1
     - recall
   * - a
     - 0.0532
     - |
     - 20
     - 3
     - |
     - 0.9933
     - 0.9935
     - 0.9933
     - 0.9933
   * - b
     - 0.0149
     - |
     - None
     - None
     - |
     - None
     - None
     - None
     - None
   * - c
     - 0.4425
     - |
     - None
     - None
     - |
     - None
     - None
     - None
     - None
   * - d
     - 0.4894
     - |
     - None
     - None
     - |
     - None
     - None
     - None
     - None


predict로 modelD에 샘플 데이터를 다시 넣어 예측하는 명령어 예제입니다.

.. code-block:: none

   * | predict modelD sepal_length,sepal_width,petal_length,petal_width

.. list-table::
   :header-rows: 1

   * - sepal_length
     - sepal_width
     - petal_length
     - petal_width
     - species
     - target
     - prediction
   * - 5.1
     - 3.5
     - 4
     - 0.2
     - Iris-setosa
     - 0
     - 0
   * - 4.9
     - 3
     - 1.4
     - 0.2
     - Iris-setosa
     - 0
     - 0
   * - 5.2
     - 2.7
     - 3.9
     - 1.4
     - Iris-versicolor
     - 1
     - 1
   * - 5
     - 2
     - 3.5
     - 1
     - Iris-versicolor
     - 1
     - 1
   * - 6.4
     - 3.2
     - 5.3
     - 2.3
     - Iris-virginica
     - 2
     - 2
   * - 6.5
     - 3
     - 5.5
     - 1.8
     - Iris-virginica
     - 2
     - 2
   * - ...
     - ...
     - ...
     - ...
     - ...
     - ...
     - ...


fit_predict로 RandomForestClassification을 적용해 분류 모델링 후 예측하는 명령어 예제입니다.

.. code-block:: none

   * | indexer species to s | fit_predict RandomForestClassification FEATURES sepal_length,sepal_width,petal_length,petal_width LABEL s maxDepth=10 INTO modelD

Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   algorithm_command : FEATURES f_fields LABEL l_field params INTO model

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - FEATURES f_fields
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
   * - maxDepth
     - tree의 깊이를 설정합니다.\ :raw-html-m2r:`<br />`\ 예 : maxDepth=10
     - 5
   * - maxBins
     - bin의 최댓값을 설정합니다.
     - 32
   * - minInstancesPerNode
     - split 이후에 반드시 가져야하는 child의 instance 수를 설정합니다.
     - 1
   * - numTrees
     - 만들 tree의 수를 설정합니다.
     - 20
   * - minInfoGain
     - tree의 split을 위한 얻을 수 있는 최소 정보입니다.
     - 0.0
   * - maxMemoryInMB
     - 최대 메모리를 설정합니다.
     - 256
   * - cacheNodeIds
     - 각 트리의 instance 마다 cache node id를 사용할지 안할지 여부 결정합니다.
     - False
   * - subsamplingRate
     - 각각의 decisiontree에서 learning에 사용할 training data의 비율을 설정합니다.
     - 1.0
   * - impurity
     - 계산 결과에서 얻을 수 잇는 정보의 표준을 결정합니다. (gini, entorpy)
     - gini
   * - checkpointInterval
     - cache 하는 checkpoint의 반복 주기를 설정합니다.
     - 10
   * - featureSubsetStrategy
     - 특징의 수를 고려하여 각각의 tree를 얼마나 펼칠지 결정합니다. :raw-html-m2r:`<br />`\ (auto, all, onethird, sqrt, log2, (0.0-1.0], [1-n])
     - auto


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   SparkRandomForestClassification_command : FEATURES fields LABEL l_field params INTO_model

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
