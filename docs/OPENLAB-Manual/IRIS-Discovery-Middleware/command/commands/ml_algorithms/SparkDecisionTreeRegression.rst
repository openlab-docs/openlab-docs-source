.. role:: raw-html-m2r(raw)
   :format: html


Spark DecisionTree Regression
====================================================================================================

개요
----------------------------------------------------------------------------------------------------

DecisionTree는 Classification / Regression에 모두 사용 할 수 있으며, 특정 값이 누락되어 있어도 사용 할 수 있습니다.

설명
----------------------------------------------------------------------------------------------------

Decision Tree 모델을 만들고 input data frame을 모델에 적용시킵니다. Decision Tree 모델 학습에 필요한 파라미터들을 지정할 수 있으며 지정하지 않을 시 Default 값으로 설정됩니다.

Examples
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


fit으로  DecisionTreeRegression 적용해 분류 하는 모델을 생성하는 명령어 예제입니다.

.. code-block:: none

   * | fit DecisionTreeRegression FEATURES crim, age, tax LABEL medv maxdepth=3 minInfoGain=0.0 seed=None INTO modelC

feature별 gini계수(feature importance) , 평가지표(rmse, r2,mae) 출력

.. list-table::
   :header-rows: 1

   * - features
     - generalizeGini
     - space
     - rmse
     - r2
     - mae
   * - crim
     - 0.2784
     - |
     - 6.7384
     - 0.4621
     - 4.5765
   * - age
     - 0.0688
     - |
     - None
     - None
     - None
   * - tax
     - 0.6528
     - |
     - None
     - None
     - None


predict로 modelC에 샘플 데이터를 다시 넣어 예측하는 명령어 예제입니다.

.. code-block:: none

   * | predict modelC crim, age, tax

.. list-table::
   :header-rows: 1

   * - crim(범죄율)
     - age(연식)
     - tax(세금)
     - medv(집값)
     - prediction
   * - 0.671909988
     - 90.30000305
     - 307
     - 16.60000038
     - 22.336029403
   * - 1.002449989
     - 87.30000305
     - 307
     - 21
     - 22.336029403
   * - 8.055789948
     - 95.40000153
     - 666
     - 13.80000019
     - 14.740000152
   * - ...
     - ...
     - ...
     - ...
     - ...


fit_predict로 DecisionTreeRegression을 적용해 분류모델을 생성하고 후 예측하는 명령어 예제입니다.

.. code-block:: none

   * | fit_predict DecisionTreeRegression FEATURES crim, age, tax LABEL medv maxdepth=3 minInfoGain=0.0 seed=None INTO modelC

Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   SparkDecisionTreeRegression_command : FEATURES fields LABEL l_field params INTO_model

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
   * - maxDepth
     - tree의 깊이를 설정합니다.\ :raw-html-m2r:`<br />`\ 예 : maxDepth=10
     - 5
   * - maxBins
     - bin의 최댓값을 설정합니다.
     - 31
   * - minInstancesPerNode
     - split 이후에 반드시 가져야하는 child의 instance 수를 설정합니다.
     - 1
   * - minInfoGain
     - tree의 split을 위한 얻을 수 있는 최소 정보입니다. (정확히는 모르겠습니다.)
     - 0.0
   * - maxMemoryInMB
     - 최대 메모리를 설정합니다.
     - 256
   * - cacheNodeIds
     - 각 트리의 instance 마다 cache node id를 사용할지 안할지 여부 결정합니다.
     - False
   * - impurity
     - 계산 결과에서 얻을 수 잇는 정보의 표준을 결정합니다. (gini, entorpy, variance)
     - variance
   * - checkpointInterval
     - cache 하는 checkpoint의 반복 주기를 설정합니다.
     - 10
   * - seed
     - 학습에 필요한 seed값 입니다.
     - None


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   SparkDecisionTreeRegression_command : FEATURES fields LABEL l_field params INTO_model
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

   WORD = r'\w+'
   COMMA = r'\,'
   FEATURES = r'FEATURES | features'
   LABEL = r'LABEL | label'
   INTO = r'INTO'
   EQUALS = r'\='
   TIMES = r'\*'
   MINUS = r'-'
   LBRACKET = r'\['
   RBRACKET = r'\]'
   DOUBLE = [-+]?[0-9]+(\.([0-9]+)?([eE][-+]?[0-9]+)?|[eE][-+]?[0-9]+)
