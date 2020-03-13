.. role:: raw-html-m2r(raw)
   :format: html


model-stats
====================================================================================================

model-stats 명령어 문법 및 연동규격 설명서 입니다.

개요
----------------------------------------------------------------------------------------------------

지정된 필드에 대한 distinct count 값을 제공합니다.

설명
----------------------------------------------------------------------------------------------------

 사용자가 지정한 모델이름에 해당하는 데이터 모델을 참조하여, 해당 데이터 모델에 포함된 필드별 distinct count 값을 제공합니다.

Examples
----------------------------------------------------------------------------------------------------


* ``field`` 옵션이 포함지 않은 경우.

.. code-block:: none

   model-stats name = syslog start_date = 20181010120000 end_date = 20181015120000

명령어 이후 테이블

.. list-table::
   :header-rows: 1

   * - distinct_count
     - type
     - name
   * - 22
     - TEXT
     - HOST
   * - 26532
     - TEXT
     - RAW
   * - 7
     - TEXT
     - LEVEL
   * - ...
     - ...
     - ...



* ``field`` 옵션이 포함된 경우.

.. code-block:: none

   model-stats name = syslog start_date = 20181010120000 end_date = 20181015120000 field = HOST

명령어 이후 테이블

.. list-table::
   :header-rows: 1

   * - distinct_count
     - type
     - name
   * - 22
     - TEXT
     - HOST


Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   ... | model-stats MODEL_NAME (MODEL_OWNER)? (OPTIONS)? (ARGUMENTS)?

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - MODEL_NAME
     - 불러올 데이터 모델의 ``모델명``\ 을 지정하는 요소 입니다.\ :raw-html-m2r:`<br/>`\ 예 : name = syslog\ :raw-html-m2r:`<br/>`\ 특수한 경우 모델 ID 사용이 가능합니다. :raw-html-m2r:`<br/>`\ 예 : name = 4c282dba-44c3-4ca1-83cf-e9ff92acde08\ :raw-html-m2r:`<br/>`\ 모델명에 스페이스가 포함된 경우 아래와 같이 따옴표 (')로 감싸서 입력해야 합니다.  :raw-html-m2r:`<br/>`\ 예 : name = 'B IRIS model A'
     - 필수
   * - MODEL_OWNER
     - 모델명 중복을 방지하기 위해 데이터 모델 소유자를 지정합니다.\ :raw-html-m2r:`<br/>`\ 스페이스가 포함된 문자열은 사용불가 합니다.\ :raw-html-m2r:`<br/>`\ 예 : model_owner= root
     - 옵션
   * - OPTIONS
     - 검색 옵션입니다.\ :raw-html-m2r:`<br/>`\ ``STARTDATE`` : 검색하고자 하는 데이터의 시작 시간 조건 입니다.\ :raw-html-m2r:`<br/>`\ 예 : start_date = 20181015120000\ :raw-html-m2r:`<br/>`\ ``ENDDATE`` : 검색하고자 하는 데이터의 끝 시간 조건 입니다.\ :raw-html-m2r:`<br/>`\ 예 : end_date = 20181015120000\ :raw-html-m2r:`<br/>`\ ``FIELD`` : 얻고자 하는 값 대상 필드를 지정합니다. 생략 시, 모든 필드의 결과값이 제공됩니다.
     - 옵션
   * - ARGUMENTS
     - ex) field = hostFull-Text-Search 조건을 입력합니다.\ :raw-html-m2r:`<br/>`\ 값 지정 시 ``' '`` 를 포함하여야 합니다. (생략 시 필드명으로 인식.)\ :raw-html-m2r:`<br/>`\ 예 : model ... MODEL_OWNER = root HOST LIKE 'gcs%'\ :raw-html-m2r:`<br/>`\ 예 : model ... MODEL_OWNER= root LEVEL < '6'
     - 옵션


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   modelstats_command : modelname options arguments

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

   TERM : ([^\s=\'\%])+
   BOOL : (?i)true|(?i)false
   MODEL_OWNER : model_owner|MODEL_OWNER
   FIELD : field|FIELD
   NAME : name|NAME
   STARTDATE : start_date|START_DATE
   ENDDATE : end_date|END_DATE
   NUMBER : \d+
   FLOAT : \d+\.\d+
   SAMPLING : (?i)sampling
   SAMPLING_RATE : (?i)sampling_rate
   SQ_TERM_SQ : \'[a-zA-Z0-9가-힣 _\-\[\]{}()\.:\%]+\'
