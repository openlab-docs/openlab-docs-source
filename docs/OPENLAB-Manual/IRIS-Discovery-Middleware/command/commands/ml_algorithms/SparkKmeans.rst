
Spark Kmeans
====================================================================================================

Kmeans학습 알고리즘 설명 및 파라미터 설명서 입니다.

개요
----------------------------------------------------------------------------------------------------

Kmeans알고리즘을 사용해 모델을 만들고 데이터를 학습하는 명령어 입니다.

설명
----------------------------------------------------------------------------------------------------

Kmeans 모델을 만들고 input data frame을 모델에 적용시킵니다. Kmeans 모델 학습에 필요한 파라미터들을 지정할 수 있으며 지정하지 않을 시 Default 값으로 설정됩니다.

Examples
----------------------------------------------------------------------------------------------------

Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   ... | fit KMeans FEATURES fields INTO_model

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
   * - k
     - 중심점의 갯수 입니다.
     - 옵션
   * - initMode
     - initialize mode입니다.
     - 옵션
   * - tol
     - convergence tolerance 값 입니다.
     - 옵션


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   SparkKmeans_command : FEATURES fields params INTO_model

   fields : field
           | fields COMMA field

   field : WORD
           | TIMES
           | MINUS WORD

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
   INTO : INTO
   EQUALS : \=
   TIMES : \*
   MINUS : \-
   LBRACKET : \[
   RBRACKET : \]
   DOUBLE : [-+]?[0-9]+(\.([0-9]+)?([eE][-+]?[0-9]+)?|[eE][-+]?[0-9]+)


   params : k = 2, initMode = "k-means||", initSteps = 2, tol = 1e-4, maxIter = 20, seed = None
