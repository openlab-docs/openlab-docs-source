.. role:: raw-html-m2r(raw)
   :format: html


model
====================================================================================================

개요
----------------------------------------------------------------------------------------------------

모델에 해당하는 데이터 소스의 데이터를 로드합니다.

설명
----------------------------------------------------------------------------------------------------

사용자가 지정한 모델이름에 해당하는 데이터 모델을 참조하여, 데이터의 타입을 확인 및 해당하는 데이터 소스(IRIS, HDFS 등) 에서 데이터를 불러옵니다. 데이터를 로드하는 명령어 이므로, 특정 명령어를  제외한 모든 명령어에 내부적으로 선행되어 사용 됩니다.

Examples
----------------------------------------------------------------------------------------------------

모든 모델의 이름 목록을 보여줍니다.

.. code-block:: none

   * | model list

.. list-table::
   :header-rows: 1

   * - name
   * - wiki_ko
   * - syslog
   * - slope
   * - POLLUTION
   * - ...


``syslog`` 모델의 데이터 중 host 컬럼의 값이 ``gcs3``\ 인 레코드를 보여줍니다.

검색 창에는 ``host='gcs3'``\ 만 입력하였지만 ``model``\ 명령어가 내부적으로 선행됩니다.

.. code-block:: none

   # 검색창
   host='gcs3'
   # 내부 쿼리
   model name = 'syslog' model_owner = eva start_date = 20191028172800 end_date = 20191028172956 host='gcs3'

.. list-table::
   :header-rows: 1

   * - DATETIME
     - HOST
     - ...
     - LEVEL
   * - 20191028172805
     - gcs3
     - ...
     - info
   * - 20191028172805
     - gcs3
     - ...
     - info
   * - 20191028172805
     - gcs3
     - ...
     - info
   * - ...
     - ...
     - ...
     - ...


``syslog`` 모델의 데이터 중 host 컬럼의 값이 ``gcs``\ 로 시작하는 레코드를 보여줍니다.

검색 창에는 ``host like 'gcs%'``\ 만 입력하였지만 ``model``\ 명령어가 내부적으로 선행됩니다.

.. code-block:: none

   # 검색창
   host like 'gcs%'
   # 내부 쿼리
   model name = 'syslog' model_owner = eva start_date = 20191028175700 end_date = 20191028175838 host like 'gcs%'

.. list-table::
   :header-rows: 1

   * - DATETIME
     - HOST
     - ...
     - LEVEL
   * - 20191029090700
     - gcs1
     - ...
     - warning
   * - 20191029090701
     - gcs4
     - ...
     - info
   * - 20191029090701
     - gcs4
     - ...
     - info
   * - ...
     - ...
     - ...
     - ...


Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   ... | model ACTIONS (MODEL_OWNER) (OPTIONS) (ARGUMENTS)

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - ACTIONS
     - ``LIST`` 또는 ``modelname``\ 을 지정할 수 있습니다.\ :raw-html-m2r:`<br />`\ `LIST`: 현재 보유한 데이터 모델 리스트를 불러 오며,  `LIST`옵션 사용 시 이후의 파라메터들은 적용되지 않습니다.<br />예 : list\ :raw-html-m2r:`<br />`\ ``modelname`` : 불러올 데이터 모델의 *\ ``모델명``\ 을 지정하는 요소 입니다.\ :raw-html-m2r:`<br />`\ 예 : name = syslog :raw-html-m2r:`<br />`\ 특수한 경우 모델 ID 사용이 가능합니다. :raw-html-m2r:`<br />`\ 예 : name = 4c282dba-44c3-4ca1-83cf-e9ff92acde08\ :raw-html-m2r:`<br />`\ 모델명에 스페이스가 포함된 경우 아래와 같이 따옴표 (')로 감싸서 입력해야 합니다.  :raw-html-m2r:`<br />`\ 예 : name = 'B IRIS model A'
     - 필수
   * - MODEL_OWNER
     - 모델명 중복을 방지하기 위해 데이터 모델 소유자를 지정합니다.\ :raw-html-m2r:`<br />`\ 스페이스가 포함된 문자열은 사용불가 합니다.\ :raw-html-m2r:`<br />`\ 예 : model_owner= root
     - 옵션
   * - OPTIONS
     - 검색 옵션입니다.\ :raw-html-m2r:`<br />`\ ``STARTDATE`` : 검색하고자 하는 데이터의 시작 시간 조건 입니다.\ :raw-html-m2r:`<br />`\ 예 : start_date = 20181015120000\ :raw-html-m2r:`<br />`\ ``ENDDATE`` : 검색하고자 하는 데이터의 끝 시간 조건 입니다.\ :raw-html-m2r:`<br />`\ 예 : end_date = 20181015120000
     - 옵션
   * - ARGUMENTS
     - Full-Text-Search 조건을 입력합니다.\ :raw-html-m2r:`<br />`\ 값 지정 시 ``' '`` 를 포함하여야 합니다. (생략 시 필드명으로 인식.)\ :raw-html-m2r:`<br />`\ 예 : model ... MODEL_OWNER = root HOST LIKE 'gcs%'\ :raw-html-m2r:`<br />`\ 예 : model ... MODEL_OWNER= root LEVEL < '6'
     - 옵션


*\ ``모델명`` : 특정 데이터 소스(IRIS, HDFS 등)의 객체(Table, File 등)을 사용하기 위해 사용자가 모델을 생성하게 되는데 그 모델의 이름

Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   model_command : actions options arguments

   actions : LIST
           | modelname

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
             | LIST TERM
             | TERM NAME
             | TERM LIST

   options : option
           | options option

   option : SIZE EQ NUMBER
          | STARTDATE EQ NUMBER
          | ENDDATE EQ NUMBER
          | MODEL_OWNER EQ TERM
          | MODEL_OWNER EQ NUMBER
          | MODEL_OWNER EQ NUMBER TERM
          | MODEL_OWNER EQ exception
          | SPATIAL_COORDINATES EQ POLYGON
          | SPATIAL_COLUMN EQ q_terms
          | SPATIAL_RELATION EQ q_terms
          | MAP_LEVEL EQ NUMBER
          | MAP_LEVEL_COLUMN EQ q_terms
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

   SIZE = (?i)size
   SQ_TERM_SQ = \'[a-zA-Z0-9가-힣 _\-\[\]{}()\.:]+\'
   FLOAT = \d+\.\d+
   NUMBER = \d+
   SAMPLING_RATE = (?i)sampling_rate
   SAMPLING = (?i)sampling
   POLYGON = 'POLYGON\(\((?:[0-9 ,.-]*)\)\)'
   STARTDATE = (?i)start_date
   ENDDATE = (?i)end_date
   LIST = (?i)list
   NAME = (?i)name
   MODEL_OWNER = (?i)model_owner
   SPATIAL_COORDINATES = (?i)spatial_coordinates
   SPATIAL_COLUMN = (?i)spatial_column
   SPATIAL_RELATION = (?i)spatial_relation
   MAP_LEVEL_COLUMN = (?i)map_level_column
   MAP_LEVEL = (?i)map_level
   BOOL = (?i)true|(?i)false
   TERM = ([^\s=\'])+
