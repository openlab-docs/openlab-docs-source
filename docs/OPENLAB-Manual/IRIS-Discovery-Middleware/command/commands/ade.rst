.. role:: raw-html-m2r(raw)
   :format: html


ade
====================================================================================================

개요
----------------------------------------------------------------------------------------------------

Anomaly Detection Engine(ADE) 이상 탐지를 하는 명령어 입니다.

설명
----------------------------------------------------------------------------------------------------

현재는 SPC와 IQR 모델만 지원합니다.

Examples
----------------------------------------------------------------------------------------------------

최근 10분의 ``HOST`` 별 해당 record의 갯수가 과거 4주와 비교하여 얼만큼 이상한 값을 갖고 있는지 탐지하는 명령어 입니다.

.. code-block:: none

     ... | ade SPC
       KEYS HOST SIZE 500
       VALUES count(HOST)
       TEST DATETIME START '20170705121000' END '20170705132000'
       REFERENCE DATETIME START '20170604000000' END '20170705121000'
       BY 10M
       PERMISSIVE TRUE
       TIMEMATCH TRUE
       NULLVALUE NULL
       DAYS SAMEDAY

Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   ... | ade MODEL
     (KEYS FIELD_NAME (AS ALIAS)? (SIZE NUMBER)? (, KEYS FIELD_NAME (AS ALIAS)? (SIZE NUMBER)?)*)?
     VALUES FUNCTION (, FUNCTION)*
     (TEST FIELD_NAME START DATE END DATE)?
     (REFERENCE FIELD_NAME START DATE END DATE)?
     BY [1H|5M|10M|1M]
     PERMISSIVE [TRUE|FALSE]
     TIMEMATCH [TRUE|FALSE]
     NULLVALUE [NULL|ANY]
     DAYS [SAMEDAY|WEEKDAY|WEEKEND]
     (FILTER CONDITION)?

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - MODEL
     - ``MODEL`` 은 iqr 과 spc가 올 수 있습니다.
     - 필수
   * - KEYS FIELD_NAME
     - 키로 지정 할 필드 이름을 의미합니다.
     - 필수
   * - AS ALIAS
     - ``AS``\ 는 예약어이며, ``ALIAS``\ 는 output에서 별칭 될 이름을 의미합니다.\ :raw-html-m2r:`<br />`\ 예 : AS field_alias
     - 옵션
   * - SIZE NUMBER
     - ``SIZE``\ 는 예약어이며, ``NUMBER``\ 는 숫자를 의미합니다.\ :raw-html-m2r:`<br />`\ 예 : SIZE 10
     - 옵션
   * - VALUES FUNCTION
     - ``VALUES``\ 는 예약어이며, ``FUNCTION``\ 은 ``func(...)`` 와 같은 형태의 값을 의미합니다. :raw-html-m2r:`<br />`\ 예 : avg(fieldA)
     - 옵션
   * - TEST FIELD_NAME START DATE END DATE
     - 비교 데이터의 범위 기간을 지정합니다. :raw-html-m2r:`<br />`\ ``TEST``\ , ``START``\ 와 ``END``\ 는 예약어이며, ``FIELD_NAME`` 는 시간 필드 이름을 의미합니다.
     - 옵션
   * - REFERENCE FIELD_NAME START DATE END DATE
     - 참조 데이터의 범위 기간을 지정합니다.\ :raw-html-m2r:`<br />`\ ``TEST``\ , ``START``\ 와 ``END``\ 는 예약어이며, ``FIELD_NAME`` 는 시간 필드 이름을 의미합니다.
     - 옵션
   * - BY [1H|5M|10M|1M]
     - 비교 데이터가 group-by될 시간 단위를 지정합니다. :raw-html-m2r:`<br />`\ ``BY``\ ,\ ``1H``\ , ``5M``\ , ``10M`` 와 ``1M``\ 는 예약어입니다.
     - 필수
   * - PERMISSIVE [TRUE|FALSE]
     - 참조 데이터에 없는 key값을 테스트 데이터의 새로운 key가 들어 왔을 때, 허용 하느냐 안하느냐를 뜻합니다. :raw-html-m2r:`<br />`\ 모두 예약어입니다.
     - 필수
   * - TIMEMATCH [TRUE|FALSE]
     - 참조 데이터와 비교 데이터의 비교 시간을 일치시킬 것인지 아닌지를 의미합니다. :raw-html-m2r:`<br />`\ 모두 예약어입니다.
     - 필수
   * - NULLVALUE [NULL|ANY]
     - 결측치를 나타낼 값을 의미합니다. 모두 예약어입니다
     - 필수
   * - DAYS [SAMEDAY|WEEKDAY|WEEKEND]
     - 처리해야 할 날짜의 분류를 의미합니다. 모두 예약어입니다.
     - 필수
   * - FILTER CONDITION
     - ``FILTER``\ 는 예약어이며 ``CONDITION``\ 에는 where 절에 올 수 있는 조건들을 의미합니다.
     - 옵션


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   clauses : model keys values test reference by permissive timematch nullvalue days filter
           | model keys values test reference by permissive timematch nullvalue days
           | model keys values test by permissive timematch nullvalue days filter
           | model keys values test by permissive timematch nullvalue days
           | model keys values reference by permissive timematch nullvalue days
           | model keys values reference by permissive timematch nullvalue days filter
           | model keys values by permissive timematch nullvalue days
           | model values by permissive timematch nullvalue days filter
           | model values test reference by permissive timematch nullvalue days filter
           | model values test reference by permissive timematch nullvalue days
           | model values test by permissive timematch nullvalue days filter
           | model values test by permissive timematch nullvalue days
           | model values reference by permissive timematch nullvalue days
           | model values reference by permissive timematch nullvalue days filter
           | model values by permissive timematch nullvalue days

   model : string_or_token

   keys : KEYS key_list

   key_list : key
            | key_list COMMA key

   key : string_or_token AS string_or_token SIZE string_or_token KEYVALUES string_or_tokens
       | string_or_token AS string_or_token SIZE string_or_token
       | string_or_token AS string_or_token
       | string_or_token
       | string_or_token SIZE string_or_token KEYVALUES string_or_tokens
       | string_or_token SIZE string_or_token


   string_or_tokens : string_or_token
                    | string_or_tokens string_or_token

   string_or_token : TOKEN
                   | STRING

   values : VALUES value_list

   value_list : string_or_token LPAREN string_or_token RPAREN
              | value_list COMMA string_or_token LPAREN string_or_token RPAREN

   test : TEST string_or_token START string_or_token END string_or_token
        | TEST string_or_token string_or_token
        | TEST string_or_token

   reference : REFERENCE string_or_token START string_or_token END string_or_token
             | REFERENCE string_or_token END string_or_token
             | REFERENCE string_or_token START string_or_token
             | REFERENCE string_or_token

   by : BY string_or_token

   permissive : PERMISSIVE string_or_token

   timematch : TIMEMATCH string_or_token

   nullvalue : NULLVALUE string_or_token

   days : DAYS SAMEDAY
        | DAYS WEEKDAY
        | DAYS WEEKEND

   filter : FILTER raw_tokens

   raw_tokens : raw_tokens TOKEN
              | raw_tokens STRING
              | TOKEN
              | STRING

   STRING = (?:"(?:[^"\\n\\r\\\\]|(?:"")|(?:\\\\x[0-9a-fA-F]+)|(?:\\\\.))*")|(?:\'(?:[^\'\\n\\r\\\\]|(?:\'\')|(?:\\\\x[0-9a-fA-F]+)|(?:\\\\.))*\')
   TOKEN = [^,|^ |^\|^\'|\"|^\(|^\)]+
   LPAREN = (
   RPAREN = )
   COMMA = ,
   KEYS = KEYS
   AS = AS
   SIZE = SIZE
   VALUES = VALUES
   KEYVALUES = KEYVALUES
   TEST = TEST
   START = START
   END = END
   REFERENCE = REFERENCE
   BY = BY 
   PERMISSIVE = PERMISSIVE
   TIMEMATCH = TIMEMATCH
   NULLVALUE = NULLVALUE
   DAYS = DAYS
   SAMEDAY = SAMEDAY
   WEEKDAY = WEEKDAY
   WEEKEND = WEEKEND
   FILTER = FILTER
