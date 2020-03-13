.. role:: raw-html-m2r(raw)
   :format: html


model-timeline
====================================================================================================

model-timeline 명령어 문법 및 연동규격 설명서 입니다.

개요
----------------------------------------------------------------------------------------------------

지정된 데이터 모델의 Timeline을 생성합니다.

설명
----------------------------------------------------------------------------------------------------

 사용자가 지정한 모델이름에 해당하는 데이터 모델을 참조하여, 해당 데이터 모델을 지정한 시간 단위(y, m, d, H, M, S)로 그룹화 하여 제공합니다. 같은 결과를 ``stats``\ 와 같은 연산 명령어로 수행할 수 있지만, ``model-timeline`` 명령어는, 직접 IRIS에 데이터를 요청하기에 빠른 결과를 제공합니다.

Examples
----------------------------------------------------------------------------------------------------


* ``UNIT`` 옵션이 ``1d`` 인경우.

.. code-block:: none

   model-timeline name = syslog start_date = 20181010120000 end_date = 20181015120000 unit = 1d HOST LIKE 'gcs%'

.. list-table::
   :header-rows: 1

   * - date
     - event_count
   * - 20181010000000
     - 441003
   * - 20181011000000
     - 888507
   * - 20181012000000
     - 396628
   * - ...
     - ...



* ``UNIT`` 옵션이 ``1H`` 인경우.

.. code-block:: none

   model-timeline name = syslog start_date = 20181015080000 end_date = 20181015120000 unit = 1H HOST LIKE 'gcs%'

.. list-table::
   :header-rows: 1

   * - date
     - event_count
   * - 20181015080000
     - 32616
   * - 20181015090000
     - 36857
   * - 20181015100000
     - 35459
   * - ...
     - ...


Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   ... | model-timeline MODEL_NAME (MODEL_OWNER)? (OPTIONS)? (ARGUMENTS)?

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - MODEL_NAME
     - 불러올 데이터 모델의 ``모델명``\ 을 지정하는 요소 입니다.\ :raw-html-m2r:`<br />`\ 예 : name = syslog\ :raw-html-m2r:`<br />`\ 특수한 경우 모델 ID 사용이 가능합니다. :raw-html-m2r:`<br />`\ 예 : name = 4c282dba-44c3-4ca1-83cf-e9ff92acde08\ :raw-html-m2r:`<br />`\ 모델명에 스페이스가 포함된 경우 아래와 같이 따옴표 (')로 감싸서 입력해야 합니다.  :raw-html-m2r:`<br />`\ 예 : name = 'B IRIS model A'
     - 필수
   * - MODEL_OWNER
     - 모델명 중복을 방지하기 위해 데이터 모델 소유자를 지정합니다.\ :raw-html-m2r:`<br />`\ 스페이스가 포함된 문자열은 사용불가 합니다.\ :raw-html-m2r:`<br />`\ 예 : model_owner= root
     - 옵션
   * - OPTIONS
     - 검색 옵션입니다.\ :raw-html-m2r:`<br/>`\ ``STARTDATE`` : 검색하고자 하는 데이터의 시작 시간 조건 입니다.\ :raw-html-m2r:`<br />`\ 예 : start_date = 20181015120000\ :raw-html-m2r:`<br />`\ ``ENDDATE`` : 검색하고자 하는 데이터의 끝 시간 조건 입니다.\ :raw-html-m2r:`<br />`\ 예 : end_date = 20181015120000\ :raw-html-m2r:`<br/>`\ ``size`` : 최종적으로 얻고자 하는 크기를 지정하는 것이 아닌, 모든 검색에 앞서 최초 불러온 데이터의 크기를 의미 합니다.\ :raw-html-m2r:`<br/>`\ ``unit`` : 데이터들을 그룹화할 단위를 선택 합니다. 년, 월, 일, 시, 분, 초 (y, m, d, H, M, S)가 지정 가능합니다. 생략 시 데이터 범위에 따라 적절한 기간을 자동으로 지정합니다. ex) unit = 1d
     - 옵션
   * - ARGUMENTS
     - Full-Text-Search 조건을 입력합니다.\ :raw-html-m2r:`<br />`\ 값 지정 시 ``' '`` 를 포함하여야 합니다. (생략 시 필드명으로 인식.)\ :raw-html-m2r:`<br />`\ 예 : model ... MODEL_OWNER = root HOST LIKE 'gcs%'\ :raw-html-m2r:`<br />`\ 예 : model ... MODEL_OWNER= root LEVEL < '6'
     - 옵션


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   modeltimeline_command : modelname options arguments

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

   option : SIZE EQ NUMBER
           | STARTDATE EQ NUMBER
           | ENDDATE EQ NUMBER
           | UNIT EQ NUMBER TERM
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
           | NUMBER
           | FLOAT
           | exception
           | NAME
           | SQ_TERM_SQ
           | q_terms

   TERM : ([^\s=\'\%])+
   BOOL : (?i)true|(?i)false
   MODEL_OWNER : model_owner|MODEL_OWNER
   UNIT : unit|UNIT
   NAME : name|NAME
   STARTDATE : start_date|START_DATE
   ENDDATE : end_date|END_DATE
   NUMBER : \d+
   FLOAT : \d+\.\d+
   SAMPLING : (?i)sampling
   SAMPLING_RATE : (?i)sampling_rate
   SQ_TERM_SQ : \'[a-zA-Z0-9가-힣 _\-\[\]{}()\.:\%]+\'
   SIZE : size|SIZE
