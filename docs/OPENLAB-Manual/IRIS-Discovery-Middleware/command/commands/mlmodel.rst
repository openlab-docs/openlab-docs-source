.. role:: raw-html-m2r(raw)
   :format: html


mlmodel
====================================================================================================

개요
----------------------------------------------------------------------------------------------------

Data-Discovery-Service ML 관련 명령어 이며, ML 명령어 중 ``fit`` 명령어를 통해 생성되는 모델 및 메타데이터를 관리하는 명령어 입니다. 

설명
----------------------------------------------------------------------------------------------------

사용자가 ``fit`` 명령어를 통해 학습시킨 ML 모델의 목록, 형태 를 확인하고 관리하는 명령어 입니다.

Examples
----------------------------------------------------------------------------------------------------

``list`` options 를 사용한 예제입니다.

.. code-block:: none

   * | mlmodel list

명령어 이후 테이블

.. list-table::
   :header-rows: 1

   * - index
     - alg
     - model_name
     - saved_date
     - comment
   * - 0
     - LinearRegression
     - LR_modelA
     - 20180619010000
     - test
   * - 1
     - LinearRegression
     - LR_modelB
     - 20180627010000
     - latest
   * - 2
     - LogisticRegression
     - Lg_modelA
     - 20180701010000
     - xx 테스트용
   * - 3
     - K-means
     - K_means_model2
     - 20180710010000
     - None
   * - 4
     - LDA
     - LDAmodel_syslog
     - 20180719010000
     - None
   * - ...
     - …
     - …
     - ...
     - ...


``list`` options 이후 필터링하여 원하는 결과를 얻는 예제입니다.

.. code-block:: none

   * | mlmodel list | where saved_date > 201807000000

.. code-block:: none

   * | mlmodel list | where algo = LinearRegression

.. code-block:: none

   * | mlmodel list | where evaluation > 90.0

.. code-block:: none

   * | mlmodel list | where index == 7

``delete`` options 를 사용한 예제입니다.

.. code-block:: none

   mlmodel delete LR_modelA

명령어 이후 테이블

.. list-table::
   :header-rows: 1

   * - index
     - alg
     - model_name
     - saved_date
     - comment
   * - 1
     - LinearRegression
     - LR_modelB
     - 20180627010000
     - latest
   * - 2
     - LogisticRegression
     - Lg_modelA
     - 20180701010000
     - xx 테스트용
   * - 3
     - K-means
     - K_means_model2
     - 20180710010000
     - None
   * - 4
     - LDA
     - LDAmodel_syslog
     - 20180719010000
     - None
   * - ...
     - …
     - …
     - ...
     - ...


``rename`` options 를 사용한 예제입니다.

.. code-block:: none

   mlmodel rename LR_modelB LR_bestmodel

명령어 이후 테이블

.. list-table::
   :header-rows: 1

   * - index
     - alg
     - model_name
     - saved_date
     - comment
   * - 0
     - LinearRegression
     - LR_modelA
     - 20180619010000
     - test
   * - 1
     - LinearRegression
     - LR_bestmodel
     - 20180627010000
     - latest
   * - 2
     - LogisticRegression
     - Lg_modelA
     - 20180701010000
     - xx 테스트용
   * - 3
     - K-means
     - K_means_model2
     - 20180710010000
     - None
   * - 4
     - LDA
     - LDAmodel_syslog
     - 20180719010000
     - None
   * - ...
     - …
     - …
     - ...
     - ...


``summary`` options 를 사용한 예제입니다.

.. code-block:: none

   mlmodel summary K_means_model2

명령어 이후 테이블

.. list-table::
   :header-rows: 1

   * - alg
     - model_name
     - saved_date
     - path
     - params
     - evaluation(%)
     - feature_fields
     - labeled_field
     - comment
   * - K-means
     - K_means_model2
     - 20180710010000
     - /K-means/20180710010000_K_means_model2.x
     - {"k" : 5, "b":0.01 …
     - { "accuracy" : 88.45, "b" : 83.23 ...}
     - fieldA
     - None
     - None


Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   mlmodel_command : ACTION model_name new_model_name

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - ACTION
     - *\ ``mlmodel`` 명령어의 기능을 지정 합니다. (defualt: list)\ :raw-html-m2r:`<br />`\ 예 : list
     - 옵션
   * - model_name
     - ``delete``\ , ``summary``\ , ``rename`` 에 사용되는 파라메터로 사전에 등록된 모델의 이름을 지정합니다.
     - 옵션
   * - new_model_name
     - ``rename`` 기능에 사용되는 파라메터로 새로 지정할 모델 명을 입력합니다.
     - 옵션


*\ ``mlmodel`` 명령어의 기능

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 예제
   * - list
     - 생성된 모든 모델의 메타정보의 일부를 출력합니다.
     - list
   * - summary
     - 모델의 요약 정보를 출력합니다.
     - summary modelLR_01
   * - delete
     - 모델을 삭제합니다.
     - delete modelLR_02
   * - rename
     - 모델의 이름을 변경합니다.
     - rename modelLR_01 modelLR_03


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   mlmodel_command : ACTION model_name new_model_name
   ACTION : LIST
          | SUMMARY
          | DELETE
          | RENAME
          |
   model_name : WORD
              |
   new_model_name : AS WORD
                  |           

   LIST = LIST | list
   SUMMARY = summary | SUMMARY
   DELETE = DELETE | delete
   RENAME = RENAME | rename
   AS = AS | as

API Request & Response
----------------------------------------------------------------------------------------------------


* 
  POST


  * 
    URL

    .. code-block:: none

       POST /angora/query/jobs?

  * 
    body

    .. code-block:: none

       { ...
           "q" : "MLMODEL options model_name new_model_name"
       ...}

  * 
    Example(Request)

    .. code-block:: none

       { ...
           "q" : "mlmodel list"
       ...}



* 
  GET


  * 
    URL

    .. code-block:: none

       GET /angora/query/jobs/[sid]?



  * 
    Reponse

    .. code-block:: none

       {
         "status": {
           "current": 1, 
           "total": 1
         }, 
         "fields": [
           {
             "grouped": false, 
             "type": "LONG", 
             "name": "index"
           },
           {
             "grouped": flase, 
             "type": "TEXT", 
             "name": "alg"
           }, 
           {
             "grouped": false, 
             "type": "TEXT", 
             "name": "model_name"
           },
           {
             "grouped": false, 
             "type": "TEXT", 
             "name": "saved_date"
           },
           {
             "grouped": false, 
             "type": "TEXT", 
             "name": "comment"
           }
         ], 
         "isEnd": true, 
         "results": [
           [
             0,
             "LinearRegression",
             "LR_modelA",
             "20180619010000",
             "test"
           ], 
           [
             1,
             "LogisticRegression",
             "Lg_modelA",
             "20180701010000",
             "테스트용"
           ], 
           [
             2,
             "K-means",
             "K_means_model2",
             "20180710010000",
             None
           ], 

         ]
       }

  * 
    Response (잘못된 options을 지정한 상황)

    .. code-block:: none

       {
         "message": "[llist] is Not in Options. [ list, delete, summary, rename ] are available.", 
         "type": "<class 'angora.exceptions.AngoraException'>"
       }

Problem
----------------------------------------------------------------------------------------------------


* 상세 검색 지원? or where 명령어로 사용?
* delete, rename 명령어 시 , 권한 문제.
* model 명 대신 index 활용 -> 편의 위하여
