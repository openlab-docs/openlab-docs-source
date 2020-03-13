
RandomForest Regression
====================================================================================================

RandomForest Regression 학습 알고리즘 설명 및 파라미터 설명서 입니다.

개요
----------------------------------------------------------------------------------------------------

RandomForest는 Classification / Regression에 모두 사용 할 수 있으며, 특정 값이 누락되어 있어도 사용 할 수 있습니다.

설명
----------------------------------------------------------------------------------------------------

여러개의 Decision Tree를 만들고 앙상블 기법으로 결과를 결정합니다. 때문에, 오버피팅을 방지할 수 있습니다.

Examples
----------------------------------------------------------------------------------------------------


* Fit으로 RandomForestRegression 적용해 분류 하는 모델을 생성하는 명령어 예제입니다.

.. code-block:: none

   ... | fit RandomForestRegression FEATURES * LABEL medv maxDepth=10 INTO modelD

.. list-table::
   :header-rows: 1

   * - features
     - generalizeGini
     - space
     - numTrees
     - rmse
     - r2
     - mae
   * - crim
     - 0.1687
     - |
     - 20
     - 2.4099
     - 0.8691
     - 1.8495
   * - zn
     - 0.0004
     - |
     - None
     - None
     - None
     - None
   * - indus
     - 0.0
     - |
     - None
     - None
     - None
     - None
   * - chas
     - 0.0
     - |
     - None
     - None
     - None
     - None
   * - nox
     - 0.0432
     - |
     - None
     - None
     - None
     - None
   * - rm
     - 0.1709
     - |
     - None
     - None
     - None
     - None
   * - age
     - 0.2407
     - |
     - None
     - None
     - None
     - None
   * - dis
     - 0.06
     - |
     - None
     - None
     - None
     - None
   * - rad
     - 0.0139
     - |
     - None
     - None
     - None
     - None
   * - tax
     - 0.0323
     - |
     - None
     - None
     - None
     - None
   * - ptratio
     - 0.001
     - |
     - None
     - None
     - None
     - None
   * - b
     - 0.1345
     - |
     - None
     - None
     - None
     - None
   * - lstat
     - 0.1345
     - |
     - None
     - None
     - None
     - None


Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   ... | fit RandomForestRegression FEATURES fields LABEL l_fields maxdepth=3 minInfoGain=0.0 seed=None INTO_model

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
   * - maxDepth
     - tree의 깊이를 설정합니다.
     - 옵션
   * - maxBins
     - bin의 최댓값을 설정합니다.
     - 옵션
   * - minInstancesPerNode
     - split 이후에 반드시 가져야하는 child의 instance 수를 설정합니다.
     - 옵션
   * - numTrees
     - 만들 tree의 수를 설정합니다.
     - 옵션
   * - minInfoGain
     - tree의 split을 위한 얻을 수 있는 최소 정보입니다. (정확히는 모르겠습니다.)
     - 옵션
   * - maxMemoryInMB
     - 최대 메모리를 설정합니다.
     - 옵션
   * - cacheNodeIds
     - 각 트리의 instance 마다 cache node id를 사용할지 안할지 여부 결정합니다.
     - 옵션
   * - subsamplingRate
     - 각각의 decisiontree에서 learning에 사용할 training data의 비율을 설정합니다.
     - 옵션
   * - impurity
     - 계산 결과에서 얻을 수 잇는 정보의 표준을 결정합니다. (Gini, Entorpy)
     - 옵션
   * - checkpointInterval
     - cache 하는 checkpoint의 반복 주기를 설정합니다.
     - 옵션
   * - featureSubsetStrategy
     - 특징의 수를 고려하여 각각의 tree를 얼마나 펼칠지 결정합니다. (auto, all, onethird, sqrt, log2, (0.0-1.0], [1-n])
     - 옵션
   * - seed
     - 학습에 필요한 seed값 입니다.
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


   params : maxDepth=5, maxBins=32, minInstancesPerNode=1, numTrees=20, minInfoGain=0.0, maxMemoryInMB=256, cacheNodeIds=False, seed=None, subsamplingRate=1.0, impurity='Gini', checkpointInterval=10, featureSubsetStrategy='auto'
