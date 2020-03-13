.. role:: raw-html-m2r(raw)
   :format: html


adv
===

개요
----

테이블의 각종 통계 정보를 구하거나 pivoting 할 수 있습니다. 고급시각화 화면에 사용되는 명령어 모음입니다.

설명
----


* 기본적으로 ``| adv operation parameters`` 형태입니다. 
* ``operation`` 은 고급시각화 다이어그램의 종류와 일치합니다. 총 10가지 타입(\ ``keyword``\ )을 지원합니다. ``operation`` 에 맞춰 ``parameters`` 를 구성해야합니다.
* ``LINE | BAR | HISTOGRAM | PIE | HEATMAP | SANKEY`` 의 6가지 타입은 aggregation 함수와 ``SPLITROW``\ , ``SPLITCOL``\ , ``AS`` 문구를 지원합니다. ``SPLITROW``\ 는 가로축 기반으로 aggregation 하며, ``SPLITCOL``\ 은 세로축 기준으로 데이터를 회전하여 aggregation 합니다. ``AS``\ 는 결과 값의 field의 별칭을 줄 수 있습니다.
* ``MOTION | SCATTER | SUMMARY | OUTLIER`` 의 4가지 타입은 ``TARGETS`` 문구를 지원합니다. ``TARGETS`` 에 이어지는 컬럼들을 기준으로 ``operation`` 에 따라 aggregation 합니다.

operation keyword
^^^^^^^^^^^^^^^^^

.. code-block:: none

   operation : [ LINE | BAR | HISTOGRAM | PIE | HEATMAP | SANKEY | MOTION | SCATTER | SUMMARY | OUTLIER ]

Examples
--------


* 'SCORE' 의 합계를 'STUDENT' 별로 그룹화하여 'DATETIME'에 따라 1 일 기준으로 피벗 한 ``LINE | BAR | PIE | HEATMAP`` 예입니다. 

.. code-block:: none

   ... | adv (line | bar | pie | heatmap) sum(SCORE) SPLITROW DATETIME SPLITCOL STUDENT


* ``SCORE`` 의 평균값 상위 100건에 대해 ``DATETIME``\ , ``REGION``\ , ``STUDENT`` 의 상호관계 흐름을 파악하기 위한 ``sankey`` 예제입니다.

.. code-block:: none

   ... | adv sankey avg(SCORE) HEAD 100 SPLITROW DATETIME,REGION,STUDENT


* ``REGION``\ (x축)과 ``STUDENT``\ (y축)에 따른 ``SCORE`` 의 분포를 얻기 위한 ``scatter`` 예제입니다.

.. code-block:: none

   ... | adv scatter TARGETS REGION, STUDENT, SCORE


* ``DATETIME`` 의 흐름에 따른 ``SCORE`` 변화량을 얻는 ``motion`` 예제입니다. 그룹핑을 위해 각 ``SCORE`` 의 ``ID``\ , ``TEST_ID``\ , ``STUDENT`` 데이터도 포함합니다.

.. code-block:: none

   ... | adv motion TARGETS DATETIME, ID, TEST_ID, SCORE, STUDENT


* ``SCORE`` 필드의 기술통계량(레코드수, 평균, 중간값, 최소값, 최대값, 1Q 사분위수, 3Q 사분위수, \*NA의 수) or 이상치 기술통계량을 얻기 위한 ``summary`` 또는 ``outlier`` 예제입니다. (\*NA : 결측치)

.. code-block:: none

   ... | adv (summary | outlier) TARGETS SCORE

Parameters
----------

LINE | BAR | PIE | HEATMAP
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

   ... | adv (LINE | BAR | PIE | HEATMAP) FUNCTION (AS ALIAS_NAME)?(, FUNCTION (AS ALIAS_NAME)?)* (SPLITROW FIELD_NAME(, FIELD_NAME)*)? (SPLITCOL FIELD_NAME(, FIELD_NAME)*)? (SORTROW order)? (SORTCOL order)?

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - ``LINE or BAR or PIE or HEATMAP``
     - 차트의 종류를 나타냅니다.
     - 필수
   * - ``FUNCTION``
     - \*aggregation 함수의 종류를 나타냅니다. :raw-html-m2r:`<br/>`\ ``,`` 구분자를 기준으로 여러개의 aggregation 함수를 사용 할 수 있습니다.\ :raw-html-m2r:`<br/>`\ ``FUNCTION`` = ``agg_func(FIELD_NAME)``  형태 입니다. :raw-html-m2r:`<br/>`\ 지원하는 ``FUNCTION``\ 은 아래 표와 같습니다. ``FIELD_NAME``\ 은 field 이름을 뜻합니다.
     - 필수
   * - ``(AS ALIAS_NAME)?``
     - ``AS``\ 는 키워드 이며 ``ALIAS_NAME``\ 은 ``FUNCTION`` 의 별칭을 뜻합니다.
     - 옵션
   * - ``(SPLITROW FIELD_NAME(, FIELD_NAME)*)?``
     - ``SPLITROW``\ 는 키워드 이며 ``FIELD_NAME``\ 는 field 이름을 뜻합니다. 여기에 정의된 field명을 기준으로 그룹핑 합니다. 각 ``FIELD_NAME``\ 는 ``,`` 로 구분 됩니다.
     - 옵션
   * - ``(SPLITCOL FIELD_NAME(, FIELD_NAME)*)?``
     - ``SPLITCOL``\ 는 키워드 이며 ``FIELD_NAME``\ 는 field 이름을 뜻합니다. 여기에 정의된 field명을 기준으로 pivoting 합니다. 각 ``FIELD_NAME``\ 는 ``,`` 로 구분 됩니다.
     - 옵션
   * - ``(SORTROW order)?``
     - ``SORTROW``\ 는 키워드이며 ``order``\ 은 ``asc/desc``\ 의 값이 들어 갑니다. ``SPLITROW``\ 로 지정된 필드에 대한 Sort 결과를 나타내 줍니다.\ :raw-html-m2r:`<br />`\ 예 : sortrow desc
     - 옵션
   * - ``(SORTCOL order)?``
     - ``SORTCOL``\ 은 키워드이며 ``order``\ 은 ``asc/desc``\ 의 값이 들어 갑니다. ``SPLITCOL``\ 로 지정된 필드의 피벗 결과에 대한 Sort 결과를 나타내 줍니다.\ :raw-html-m2r:`<br />`\ 예 : sortcol desc
     - 옵션
   * - ``order``
     - ``ASC``\ , ``DESC``\ 는 일반적인 정렬을 의미합니다.\ :raw-html-m2r:`<br />`\ 요일 정렬: ``WEEK ASC``\ , ``WEEK DESC``\ :raw-html-m2r:`<br />`\ 달 정렬: ``MONTH ASC``\ , ``MONTH DESC``\ :raw-html-m2r:`<br />`\ 계절 정렬: ``SEASON ASC``\ , ``SEASON DESC``
     - 옵션


aggregation functions list

.. list-table::
   :header-rows: 1

   * - Arguments
     - Description
     - ETC
   * - ``avg()``
     - 평균 값을 구합니다.
     - ``TEXT``\ , ``BINARY``\ , ``BOOLEAN`` 불가능
   * - ``count()``
     - 카운트를 구합니다.
     - 모든Type 가능
   * - ``first()``
     - 첫 번째 값을 구합니다.
     - 모든Type 가능
   * - ``last()``
     - 마지막 값을 구합니다.
     - 모든Type 가능
   * - ``max()``
     - 제일 큰 값을 구합니다.
     - ``TEXT``\ , ``BINARY``\ , ``BOOLEAN`` 불가능
   * - ``min()``
     - 제일 작은 값을 구합니다.
     - ``TEXT``\ , ``BINARY``\ , ``BOOLEAN`` 불가능
   * - ``median()``
     - 중간 값을 구합니다.
     - ``TEXT``\ , ``BINARY``\ , ``BOOLEAN`` 불가능
   * - ``sum()``
     - 전체 값을 구합니다.
     - ``TEXT``\ , ``BINARY``\ , ``BOOLEAN`` 불가능
   * - ``stddev()``
     - 표준편차 값을 구합니다.
     - ``TEXT``\ , ``BINARY``\ , ``BOOLEAN`` 불가능
   * - ``countDistinct()``
     - 유니크한 값의 갯수를 구합니다.
     - 모든Type 가능


요일 정렬

아래 이름이나 별명에 대해 우선적으로 정렬합니다.

.. list-table::
   :header-rows: 1

   * - 이름
     - 별명
     - 설명
   * - Monday
     - MON
     - 월요일
   * - Tuesday
     - TUE
     - 화요일
   * - Wednesday
     - WED
     - 수요일
   * - Thursday
     - THU
     - 목요일
   * - Friday
     - FRI
     - 금요일
   * - Saturday
     - SAT
     - 토요일
   * - Sunday
     - SUN
     - 일요일


달 정렬

아래 이름이나 별명에 대해 우선적으로 정렬합니다.

.. list-table::
   :header-rows: 1

   * - 이름
     - 별명
     - 설명
   * - January
     - JAN
     - 1월
   * - February
     - FEB
     - 2월
   * - March
     - MAR
     - 3월
   * - April
     - APR
     - 4월
   * - May
     - 
     - 5월
   * - June
     - 
     - 6월
   * - July
     - 
     - 7월
   * - August
     - AUG
     - 8월
   * - September
     - SEPT
     - 9월
   * - October
     - OCT
     - 10월
   * - November
     - NOV
     - 11월
   * - December
     - DEC
     - 12월


계절 정렬

아래 이름에 대해 우선적으로 정렬합니다.

.. list-table::
   :header-rows: 1

   * - 이름
     - 의미
   * - spring
     - 봄
   * - summer
     - 여름
   * - fall, autumn
     - 가을
   * - winter
     - 겨울


HISTOGRAM
^^^^^^^^^

.. code-block:: none

   ... | adv HISTOGRAM count(FIELD_NAME) (AS ALIAS_NAME)? (SPLITROW FIELD_NAME(, FIELD_NAME)*)? (SPLITCOL FIELD_NAME(, FIELD_NAME)*)?

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - ``HISTOGRAM``
     - 차트의 종류를 나타냅니다.
     - 필수
   * - ``count(FIELD_NAME)``
     - ``HISTOGRAM`` 의 경우 ``count`` 함수만 지원합니다. ``FIELD_NAME`` 은 필드 이름을 뜻하며 ``*`` 인 경우 전체 레코드의 개수를 의미합니다.
     - 필수
   * - ``(AS ALIAS_NAME)?``
     - ``AS``\ 는 키워드 이며 ``ALIAS_NAME``\ 은 ``FUNCTION`` 의 별칭을 뜻합니다.
     - 옵션
   * - ``(SPLITROW FIELD_NAME(, FIELD_NAME)*)?``
     - ``SPLITROW``\ 는 키워드 이며 ``FIELD_NAME``\ 는 field 이름을 뜻합니다. 여기에 정의된 field명을 기준으로 그룹핑 합니다. 각 ``FIELD_NAME``\ 는 ``,`` 로 구분 됩니다.
     - 옵션
   * - ``(SPLITCOL FIELD_NAME(, FIELD_NAME)*)?``
     - ``SPLITCOL``\ 는 키워드 이며 ``FIELD_NAME``\ 는 field 이름을 뜻합니다. 여기에 정의된 field명을 기준으로 pivoting 합니다. 각 ``FIELD_NAME``\ 는 ``,`` 로 구분 됩니다.
     - 옵션


SANKEY
^^^^^^

.. code-block:: none

   ... | adv SANKEY FUNCTION (HEAD N | TAIL N)? (AS ALIAS_NAME) (SPLITROW FIELD_NAME(, FIELD_NAME)*)? (SPLITCOL FIELD_NAME(, FIELD_NAME)*)?

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - ``SANKEY``
     - 차트의 종류를 나타냅니다.
     - 필수
   * - ``FUNCTION``
     - aggregation 함수의 종류를 나타냅니다. :raw-html-m2r:`<br/>`\ ``,`` 구분자를 기준으로 여러개의 aggregation 함수를 사용 할 수 있습니다.\ :raw-html-m2r:`<br/>`\ ``FUNCTION`` = ``agg_func(FIELD_NAME)``  형태 입니다. :raw-html-m2r:`<br/>`\ 지원하는 ``FUNCTION``\ 은 아래 표와 같습니다. ``FIELD_NAME``\ 은 field 이름을 뜻합니다.
     - 필수
   * - ``(HEAD N or TAIL N)?``
     - SANKEY 의 경우만 적용되는 옵션입니다. HEAD N 은 상위 N 건을 의미합니다. TAIL N 은 하위 N 건을 의미합니다. N 은 양의 정수입니다. 둘 중 하나만 적용가능합니다.
     - 옵션
   * - ``(AS ALIAS_NAME)?``
     - ``AS``\ 는 키워드 이며 ``ALIAS_NAME``\ 은 ``FUNCTION`` 의 별칭을 뜻합니다.
     - 옵션
   * - ``(SPLITROW FIELD_NAME(, FIELD_NAME)*)?``
     - ``SPLITROW``\ 는 키워드 이며 ``FIELD_NAME``\ 는 field 이름을 뜻합니다. 여기에 정의된 field명을 기준으로 그룹핑 합니다. 각 ``FIELD_NAME``\ 는 ``,`` 로 구분 됩니다.
     - 옵션
   * - ``(SPLITCOL FIELD_NAME(, FIELD_NAME)*)?``
     - ``SPLITCOL``\ 는 키워드 이며 ``FIELD_NAME``\ 는 field 이름을 뜻합니다. 여기에 정의된 field명을 기준으로 pivoting 합니다. 각 ``FIELD_NAME``\ 는 ``,`` 로 구분 됩니다.
     - 옵션


aggregation functions list

.. list-table::
   :header-rows: 1

   * - Arguments
     - Description
     - ETC
   * - ``avg()``
     - 평균 값을 구합니다.
     - ``TEXT``\ , ``BINARY``\ , ``BOOLEAN`` 불가능
   * - ``count()``
     - 카운트를 구합니다.
     - 모든Type 가능
   * - ``first()``
     - 첫 번째 값을 구합니다.
     - 모든Type 가능
   * - ``last()``
     - 마지막 값을 구합니다.
     - 모든Type 가능
   * - ``max()``
     - 제일 큰 값을 구합니다.
     - ``TEXT``\ , ``BINARY``\ , ``BOOLEAN`` 불가능
   * - ``min()``
     - 제일 작은 값을 구합니다.
     - ``TEXT``\ , ``BINARY``\ , ``BOOLEAN`` 불가능
   * - ``median()``
     - 중간 값을 구합니다.
     - ``TEXT``\ , ``BINARY``\ , ``BOOLEAN`` 불가능
   * - ``sum()``
     - 전체 값을 구합니다.
     - ``TEXT``\ , ``BINARY``\ , ``BOOLEAN`` 불가능
   * - ``stddev()``
     - 표준편차 값을 구합니다.
     - ``TEXT``\ , ``BINARY``\ , ``BOOLEAN`` 불가능
   * - ``countDistinct()``
     - 유니크한 값의 갯수를 구합니다.
     - 모든Type 가능


MOTION | SCATTER | SUMMARY | OUTLIER
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

   ... | adv (MOTION | SCATTER | SUMMARY | OUTLIER) TARGETS FIELD_NAME(, FIELD_NAME)*

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - ``MOTION or SCATTER or SUMMARY or OUTLIER``
     - 차트의 종류를 나타냅니다.
     - 필수
   * - ``TARGETS``
     - ``TARGETS fieldA, fieldB, fieldC`` 형태로 ``,`` 구분자를 사용합니다. ``fieldA~C`` 는 field 이름을 뜻합니다. 여기 정의 된 필드를 기준으로 aggregation 합니다.
     - 필수


Parameters BNF
--------------

.. code-block:: none

   clauses : op funcs
       | op funcs SPLITROW fields
       | op funcs SPLITCOL fields
       | op funcs SPLITROW fields SPLITCOL fields
       | op funcs FILTER tokens
       | op funcs SPLITROW fields FILTER tokens
       | op funcs SPLITCOL fields FILTER tokens
       | op funcs SPLITROW fields SPLITCOL fields FILTER tokens
       | op funcs COLSIZE NUMBER
       | op funcs SPLITROW fields COLSIZE NUMBER
       | op funcs SPLITCOL fields COLSIZE NUMBER
       | op funcs SPLITROW fields SPLITCOL fields COLSIZE NUMBER
       | op funcs FILTER tokens COLSIZE NUMBER
       | op funcs SPLITROW fields FILTER tokens COLSIZE NUMBER
       | op funcs SPLITCOL fields FILTER tokens COLSIZE NUMBER
       | op funcs SPLITROW fields SPLITCOL fields FILTER tokens COLSIZE NUMBER
       | op funcs SORT order
       | op funcs SPLITROW fields SORT order
       | op funcs SPLITCOL fields SORT order
       | op funcs SPLITROW fields SPLITCOL fields SORT order
       | op funcs FILTER tokens SORT order
       | op funcs SPLITROW fields FILTER tokens SORT order
       | op funcs SPLITCOL fields FILTER tokens SORT order
       | op funcs SPLITROW fields SPLITCOL fields FILTER tokens SORT order
       | op funcs COLSIZE NUMBER SORT order
       | op funcs SPLITROW fields COLSIZE NUMBER SORT order
       | op funcs SPLITCOL fields COLSIZE NUMBER SORT order
       | op funcs SPLITROW fields SPLITCOL fields COLSIZE NUMBER SORT order
       | op funcs FILTER tokens COLSIZE NUMBER SORT order
       | op funcs SPLITROW fields FILTER tokens COLSIZE NUMBER SORT order
       | op funcs SPLITCOL fields FILTER tokens COLSIZE NUMBER SORT order
       | op funcs SPLITROW fields SPLITCOL fields FILTER tokens COLSIZE NUMBER SORT order
       | op TARGETS fields
       | op TARGETS fields FILTER tokens
       | op TARGETS fields FILTER tokens SORT order
       | op TARGETS fields FILTER tokens COLSIZE NUMBER
       | op TARGETS fields FILTER tokens COLSIZE NUMBER SORT order
       | op TARGETS fields COLSIZE NUMBER
       | op TARGETS fields COLSIZE NUMBER SORT order
       | op TARGETS fields SORT order
       | op TARGETS fields RELATIVE_ERROR tokens
       | op TARGETS fields FILTER tokens RELATIVE_ERROR tokens
       | op TARGETS fields FILTER tokens SORT order RELATIVE_ERROR tokens
       | op TARGETS fields FILTER tokens COLSIZE NUMBER RELATIVE_ERROR tokens
       | op TARGETS fields FILTER tokens COLSIZE NUMBER SORT order RELATIVE_ERROR tokens
       | op TARGETS fields COLSIZE NUMBER RELATIVE_ERROR tokens
       | op TARGETS fields COLSIZE NUMBER SORT order RELATIVE_ERROR tokens
       | op TARGETS fields SORT order RELATIVE_ERROR tokens

   fields : field
          | fields COMMA field

   field : TOKEN
         | TOKEN AS TOKEN

   op : TOKEN

   funcs : funcs COMMA func
         | func

   func : FUNC
           | FUNC funcopts

   funcopts : FILLNA fillopt
           | FILLNA fillopt HEAD NUMBER
           | FILLNA fillopt TAIL NUMBER
           | FILLNA fillopt AS TOKEN
           | FILLNA fillopt HEAD NUMBER AS TOKEN
           | FILLNA fillopt TAIL NUMBER AS TOKEN
           | HEAD NUMBER
           | TAIL NUMBER
           | HEAD NUMBER AS TOKEN
           | TAIL NUMBER AS TOKEN
           | AS TOKEN

   fillopt : LPAREN TOKEN RPAREN
           | LPAREN TOKEN COMMA TOKEN RPAREN
           | LPAREN TOKEN COMMA NUMBER RPAREN

   tokens : TOKEN
           | tokens TOKEN
           | NUMBER
           | tokens NUMBER
           | LPAREN
           | tokens LPAREN
           | RPAREN
           | tokens RPAREN

   order : DESC
         | ASC

   TOKEN : [^,|^ |^\|^(|^)|^\'|\"]+
   COMMA : ,
   LPAREN : (
   RPAREN : )
   FUNC : [^\s\(,]+\([^\s\)]+\)
   SPLITROW : (?i)SPLITROW
   SPLITCOL : (?i)SPLITCOL
   FILTER : (?i)FILTER
   AS : (?i)AS
   COLSIZE : (?i)COLSIZE
   SORT : (?i)SORT
   ASC : (?i)ASC
   DESC : (?i)DESC
