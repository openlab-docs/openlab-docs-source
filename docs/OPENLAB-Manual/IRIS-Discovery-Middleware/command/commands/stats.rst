.. role:: raw-html-m2r(raw)
   :format: html


stats
====================================================================================================

개요
----------------------------------------------------------------------------------------------------

각종 통계 데이터를 구하는 명령어 입니다.

설명
----------------------------------------------------------------------------------------------------

해당 검색 결과에 각종 함수를 적용하여 통계 값을 구합니다. 마치 SQL의 aggregation과 비슷합니다. 만약 각종 통계 값들이 ``BY`` 절 없이 쓰인다면, 전체 결과를 aggregation을 하여, 하나의 열만 검색 결과로 출력 될 것입니다. 만약 ``BY`` 절에 의하여 그룹핑할 field가 주어진다면, 해당 field의 유니크한 값들의 개수 만큼의 열이 검색 결과로 출력 될 것 입니다.

Examples
----------------------------------------------------------------------------------------------------


* ``HR`` 이라는 필드 이름으로 그룹핑 된 결과 에서, 전체 의 갯수, ``YEARID`` 필드의 최대값, 최소값 그리고 평균값을 구합니다.

.. code-block:: none

   ... | stats count(*), max(YEARID), min(YEARID) BY HR

.. list-table::
   :header-rows: 1

   * - HR
     - count(*)
     - max(YEARID)
     - min(YEARID)
   * - 8
     - 1000
     - 2015
     - 1881
   * - ...
     - ...
     - ...
     - ...

* 팀별, 시간별 HR의 평균을 구합니다

.. code-block:: none

   ... | stats avg(HR) by date_group(FTS_PARTITION_TIME, "1H"), TEAMID

.. list-table::
   :header-rows: 1

   * - dategroup
     - TEAMID
     - avg(HR)
   * - 20160510180000
     - CHA
     - 2.91176470588235
   * - 20160505180000
     - BSN
     - 1.08
   * - ...
     - ...
     - ...

* quote 문자를 사용하여 단어가 아닌 필드명도 사용할 수 있습니다.

.. code-block:: none

   ... | stats avg(HR) as '평균(홈런)', count(HR) as '홈런 개수' by date_group(FTS_PARTITION_TIME, "1H"), TEAMID

.. list-table::
   :header-rows: 1

   * - dategroup
     - TEAMID
     - 평균(홈런)
     - 홈런 개수
   * - 20160510180000
     - CHA
     - 2.91176470588235
     - 34
   * - 20160505180000
     - BSN
     - 1.08
     - 125
   * - ...
     - ...
     - ...
     - ...

Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   ... | stats FUNCTION (AS ALIAS_NAME)?(, FUNCTION (AS ALIAS_NAME)?)* (BY FIELD_NAME (, FIELD_NAME)*)?

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - ``FUNCTION``
     - ``agg_func(FIELD_NAME)``\ 을 뜻합니다. 지원하는 ``agg_func``\ 는 아래 표와 같습니다. ``FIELD_NAME``\ 은 field의 이름입니다.
     - 필수
   * - ``AS ALIAS_NAME``
     - ``AS ALIAS_NAME``\ 입니다. ``AS``\ 는 키워드 이며 ``ALIAS_NAME``\ 은 변경 할 이름을 뜻합니다.
     - 옵션
   * - ``BY FIELD_NAME``
     - ``BY``\ 는 키워드를 나타내고, ``FIELD_NAME``\ 는 그룹핑 할 field명을 의미 합니다. 각 field는 ``,``\ 으로 구분 됩니다. :raw-html-m2r:`<br>`\ ``FIELD_NAME`` 은 ``date_group(FIELD, UNIT)`` 함수를 사용 할 수 있습니다. 시간 단위(\ ``UNIT``\ , 초/분/시간/일/월/년)로 ``FIELD``\ 를 그룹핑합니다. ``FIELD``\ 는 시간 필드를 의미합니다. ``UNIT``\ : 기준 시간 단위는 ``"10y"``\ , ``"1y"``\ , ``"10m"``\ , ``"1m"``\ , ``"10d"``\ , ``"1d"``\ , ``"10H"``\ , ``"1H"``\ , ``"10M"``\ , ``"1M"``\ , ``"10S"`` 과 ``"1S"`` 이 될 수 있습니다.
     - 옵션



* aggregation functions list

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
     - 모든 Type 가능
   * - ``distinct_count()``
     - 유니크한 개별 값의 개수를 구합니다
     - 모든 Type 가능
   * - ``first()``
     - 가장 처음의 값을 구합니다.
     - ``TEXT``\ , ``BINARY``\ , ``BOOLEAN`` 불가능
   * - ``last()``
     - 가장 마지막 값을 구합니다.
     - ``TEXT``\ , ``BINARY``\ , ``BOOLEAN`` 불가능
   * - ``max()``
     - 가장 큰 값을 구합니다
     - ``TEXT``\ , ``BINARY``\ , ``BOOLEAN`` 불가능
   * - ``median()``
     - 중간 값을 구합니다.
     - ``TEXT``\ , ``BINARY``\ , ``BOOLEAN`` 불가능
   * - ``min()``
     - 제일 작은 값을 구합니다.
     - ``TEXT``\ , ``BINARY``\ , ``BOOLEAN`` 불가능
   * - ``stdev()``
     - 표준편차 값을 구합니다 (SQL 의 STDEV와 동일).
     - ``TEXT``\ , ``BINARY``\ , ``BOOLEAN`` 불가능
   * - ``stdevp()``
     - 표준편차 값을 구합니다 (SQL 의 STDEVP와 동일).
     - ``TEXT``\ , ``BINARY``\ , ``BOOLEAN`` 불가능
   * - ``sum()``
     - 전체의 합을 구합니다.
     - ``TEXT``\ , ``BINARY``\ , ``BOOLEAN`` 불가능
   * - ``var()``
     - 표본의 분산 값을 구합니다.
     - ``TEXT``\ , ``BINARY``\ , ``BOOLEAN`` 불가능
   * - ``iqr()``
     - 사분위수 범위(IQR) 값을 구합니다.
     - ``TEXT``\ , ``BINARY``\ , ``BOOLEAN`` 불가능


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   clauses : funcs
           | funcs BY byclause

   byclause : byexpr
           | byclause COMMA byexpr

   byexpr : TOKEN
           | func

   funcs : funcs COMMA func
           | func

   func : TOKEN LPAREN TOKEN RPAREN
       | TOKEN LPAREN TOKEN RPAREN AS TOKEN
       | TOKEN LPAREN TOKEN COMMA TOKEN RPAREN
       | TOKEN LPAREN TOKEN COMMA TOKEN RPAREN AS TOKEN


   TOKEN : [^,|^ |^\|^(|^)|^\'|\"]+
   COMMA : ,
   LPAREN : (
   RPAREN : )
   BY : (i?)BY
