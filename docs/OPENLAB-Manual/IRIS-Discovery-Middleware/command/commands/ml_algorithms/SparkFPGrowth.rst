
Spark FP-Growth
====================================================================================================

FP-Growth 학습 알고리즘 설명 및 파라미터 설명서 입니다.

개요
----------------------------------------------------------------------------------------------------

FP-Growth 알고리즘을 사용해 모델을 만들고 데이터를 학습하는 명령어 입니다.

설명
----------------------------------------------------------------------------------------------------

FP-Growth 모델을 만들고 input data frame을 모델에 적용시킵니다. FP-Growth 모델 학습에 필요한 파라미터들을 지정할 수 있으며 지정하지 않을 시 Default 값으로 설정됩니다.

Examples
----------------------------------------------------------------------------------------------------


* Fit으로  FP-Growth를 적용해 아이템을 추천해주는 모델을 생성하는 명령어 예제입니다.

.. code-block:: none

   ... | fit_predict fpgrowth FEATURES items minSupport=0.1 minConfidence=0.5 INTO modelC


* 
  fit 명령어를 이용해 모델 생성 & 변경된 fit 리턴값 출력

* 
  frequent item 과 pattern 정보 출력

.. list-table::
   :header-rows: 1

   * - user
     - buy
     - items
     - prediction
   * - 0
     - apple banana grape  strawberry
     - apple,banana,grape,strawberry
     - [...]
   * - 1
     - peach orange  mango
     - peach,orange,mango
     - [...]
   * - 2
     - apple,orange, pineapple
     - apple,orange,pineapple
     - [...]


Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   ... | fit FPGrowth FEATURES fields INTO_model

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - FEATURES
     - 학습에 사용될 특징 column을 입력 받습니다.
     - 필수
   * - fields
     - 특징 column들의 이름입니다.
     - 필수
   * - params
     - 알고리즘 setting 파라미터들입니다.
     - 옵션
   * - INTO_model
     - ``INTO model_name``\ 으로 이루어져 있습니다. 경로 (\ **/Biris/angora/ml**\ )에 모델 메타 데이터와 함께 저장합니다.
     - 필수
   * - minSupport
     - frequent item에 대한 threshold값 입니다.
     - 옵션
   * - minConfidence
     - pattern 에 대한 threshold값 입니다.
     - 옵션
   * - numPartitions
     - partition 갯수 입니다.
     - 옵션


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   SparkFPGrowth_command : FEATURES fields params INTO_model

   fields : field
           | fields COMMA field

   field : WORD

   params : param
           | params param

   param : WORD EQUALS WORD
           | WORD EQUALS DOUBLE

   INTO_model : INTO WORD

   WORD : \w+
   COMMA : \,
   FEATURES : FEATURES | features
   INTO : INTO
   EQUALS : \=
   DOUBLE : [-+]?[0-9]+(\.([0-9]+)?([eE][-+]?[0-9]+)?|[eE][-+]?[0-9]+)


   params : minSupport=0.3, minConfidence=0.8, numPartitions=None
