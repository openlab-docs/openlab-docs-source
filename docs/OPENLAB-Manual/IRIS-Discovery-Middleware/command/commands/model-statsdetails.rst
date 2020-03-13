.. role:: raw-html-m2r(raw)
   :format: html


model-statsdetails
====================================================================================================

개요
----------------------------------------------------------------------------------------------------

지정된 필드에 존재하는 값들의 상위 빈도 10개 값을 제공합니다.

설명
----------------------------------------------------------------------------------------------------

사용자가 지정한 모델이름에 해당하는 데이터 모델을 참조하여, 해당 데이터 모델에 포함된 필드 중 지정된 필드의 값들 중 빈도가 가장 높은 상위 10개의 값을 제공합니다. 

UI의 검색탭에서 검색 후, 특정 컬럼을 선택할 때 사용됩니다.

Examples
----------------------------------------------------------------------------------------------------

.. code-block:: none

   model-statsdetails name = 'syslog' model_owner = eva start_date = 20191028152800 end_date = 20191028152934 field = HOST

.. list-table::
   :header-rows: 1

   * - count
     - value
   * - 1926
     - tsdn-svr1
   * - 160
     - gcs7
   * - 144
     - gcs3
   * - ...
     - ...


Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   ... | model-statsdetails MODEL_NAME (MODEL_OWNER)? (OPTIONS)? FIELD

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - MODEL_NAME
     - 불러올 데이터 모델의 *\ ``모델명``\ 을 지정하는 요소 입니다.\ :raw-html-m2r:`<br />`\ 예 : name = syslog\ :raw-html-m2r:`<br />`\ 특수한 경우 모델 ID 사용이 가능합니다. :raw-html-m2r:`<br />`\ 예 : name = 4c282dba-44c3-4ca1-83cf-e9ff92acde08\ :raw-html-m2r:`<br />`\ 모델명에 스페이스가 포함된 경우 아래와 같이 따옴표 (')로 감싸서 입력해야 합니다.  :raw-html-m2r:`<br />`\ 예 : name = 'B IRIS model A'
     - 필수
   * - MODEL_OWNER
     - 모델명 중복을 방지하기 위해 데이터 모델 소유자를 지정합니다.\ :raw-html-m2r:`<br />`\ 스페이스가 포함된 문자열은 사용불가 합니다.\ :raw-html-m2r:`<br />`\ 예 : model_owner= root
     - 옵션
   * - OPTIONS
     - 검색 옵션입니다.\ :raw-html-m2r:`<br />`\ ``STARTDATE`` : 검색하고자 하는 데이터의 시작 시간 조건 입니다.\ :raw-html-m2r:`<br />`\ 예 : start_date = 20181015120000\ :raw-html-m2r:`<br />`\ ``ENDDATE`` : 검색하고자 하는 데이터의 끝 시간 조건 입니다.\ :raw-html-m2r:`<br />`\ 예 : end_date = 20181015120000
     - 옵션
   * - FIELD
     - 얻고자 하는 값 대상 필드를 지정합니다.\ :raw-html-m2r:`<br />`\ 스페이스가 포함된 문자열 사용불가.\ :raw-html-m2r:`<br />`\ 예 : field = host
     - 필수
   * - ARGUMENTS
     - Full-Text-Search 조건을 입력합니다.\ :raw-html-m2r:`<br />`\ 값 지정 시 ``' '`` 를 포함하여야 합니다. (생략 시 필드명으로 인식.)\ :raw-html-m2r:`<br />`\ 예 : model ... MODEL_OWNER = root HOST LIKE 'gcs%'\ :raw-html-m2r:`<br />`\ 예 : model ... MODEL_OWNER= root LEVEL < '6'
     - 옵션


*\ ``모델명`` : 특정 데이터 소스(IRIS, HDFS 등)의 객체(Table, File 등)을 사용하기 위해 사용자가 모델을 생성하게 되는데 그 모델의 이름

Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   modelname : NAME EQ SQ_TERM_SQ
             | NAME EQ TERM
             | NAME EQ NUMBER
             | NAME EQ NUMBER TERM
             | NAME EQ exception
             | NAME EQ q_terms

   q_terms : SQ q_term SQ

   q_term : TERM
          | NUMBER
          | q_term q_term

   exception : NAME TERM
             | TERM NAME

   options : option
           | options option

   option : STARTDATE EQ NUMBER
          | ENDDATE EQ NUMBER
          | FIELD EQ TERM
          | MODEL_OWNER EQ TERM
          | MODEL_OWNER EQ NUMBER
          | MODEL_OWNER EQ NUMBER TERM
          | MODEL_OWNER EQ exception
          | SAMPLING EQ BOOL
          | SAMPLING_RATE EQ FLOAT
          | SAMPLING_RATE EQ NUMBER

   arguments : arguments argument

   argument : terms
            | terms EQ terms

   terms : TERM
         | SQ_TERM_SQ
         | NUMBER
         | FLOAT
         | exception
         | NAME
         | q_terms
