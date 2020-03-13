
Spark DecisionTree Classification
====================================================================================================

DecisionTree Classfication 학습 알고리즘 설명 및 파라미터 설명서 입니다.

개요
----------------------------------------------------------------------------------------------------

DecisionTree는 Classification / Regression에 모두 사용 할 수 있으며, 특정 값이 누락되어 있어도 사용 할 수 있습니다.

설명
----------------------------------------------------------------------------------------------------

Decision Tree 모델을 만들고 input data frame을 모델에 적용시킵니다. Decision Tree 모델 학습에 필요한 파라미터들을 지정할 수 있으며 지정하지 않을 시 Default 값으로 설정됩니다.

Examples
----------------------------------------------------------------------------------------------------


* Fit으로  DecisionTreeClassification 적용해 분류 하는 모델을 생성하는 명령어 예제입니다.

.. code-block:: none

   ... | fit DecisionTreeClassification FEATURES a,b,c,d LABEL s maxdepth=3 minInfoGain=0.0 seed=None INTO modelD


* 
  fit 명령어를 이용해 DT 모델 생성 & 변경된 fit 리턴값 출력

* 
  feature별 gini계수(feature importance) , 평가지표(acc, pre, f1, recall) 출력

.. list-table::
   :header-rows: 1

   * - features
     - generalizeGini
     - space
     - accuracy
     - precision
     - f1
     - recall
   * - a
     - 1.0
     - |
     - 1.0
     - 1.0
     - 1.0
     - 1.0
   * - b
     - 0.0
     - |
     - None
     - None
     - None
     - None
   * - c
     - 0.0
     - |
     - None
     - None
     - None
     - None
   * - d
     - 0.0
     - |
     - None
     - None
     - None
     - None


Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   ... | fit DecisionTreeClassification FEATURES fields LABEL l_fields maxdepth=3 minInfoGain=0.0 seed=None INTO_model

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
     - INTO model name으로 이루어져 있습니다. 경로 (\ **/Biris/angora/ml**\ )에 모델 메타 데이터와 함께 저장합니다.
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
   * - minInfoGain
     - tree의 split을 위한 얻을 수 있는 최소 정보입니다.
     - 옵션
   * - maxMemoryInMB
     - 최대 메모리를 설정합니다.
     - 옵션
   * - cacheNodeIds
     - 각 트리의 instance 마다 cache node id를 사용할지 안할지 여부 결정합니다.
     - 옵션
   * - impurity
     - 계산 결과에서 얻을 수 잇는 정보의 표준을 결정합니다. (Gini, Entorpy)
     - 옵션
   * - checkpointInterval
     - cache 하는 checkpoint의 반복 주기를 설정합니다.
     - 옵션
   * - seed
     - 학습에 필요한 seed값 입니다.
     - 옵션


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   SparkDecisionTreeClassification_command : FEATURES fields LABEL l_field params INTO_model

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
   COMMA : ,
   FEATURES : FEATURES | features
   LABEL : LABEL | label
   INTO : INTO
   EQUALS : \=
   TIMES : \*
   MINUS : \-
   LBRACKET = \[
   RBRACKET = \]
   DOUBLE = [-+]?[0-9]+(\.([0-9]+)?([eE][-+]?[0-9]+)?|[eE][-+]?[0-9]+)


   params : maxDepth=5, maxBins=32, minInstancesPerNode=1, minInfoGain=0.0, maxMemoryInMB=256, cacheNodeIds=False, seed=None, impurity='Gini', checkpointInterval=10,
