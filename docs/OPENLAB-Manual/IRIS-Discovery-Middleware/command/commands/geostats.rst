.. role:: raw-html-m2r(raw)
   :format: html


geostats
====================================================================================================

geostats  명령어 문법 및 연동규격 설명서 입니다.

개요
----------------------------------------------------------------------------------------------------

이 명령어는 위, 경도 데이터를 포함한 두 개의 필드를 기반으로 그룹(지정 지역 클러스터)별 통계정보를 제공합니다.

설명
----------------------------------------------------------------------------------------------------

해당하는 두 개의 필드에 포함된 위, 경도를 십진수 도(DD)로 나타내는(ex 41.40338, 2.17403) 지역들을 사용자의 기준으로 그룹짓고 이에대한 통계(count, sum, avg, min, max 등)결과를 새로운 필드로 생성하여 제공합니다. 생성된 필드는 명령어 순서에 맞게 기존 테이블의 마지막에 위치하게 됩니다.

Examples
----------------------------------------------------------------------------------------------------


* 검색대상이되는 데이터가 다음과 같이 존재합니다.

.. list-table::
   :header-rows: 1

   * - UPDATE_TIME
     - SYS_OUT
     - OUT_TYPE
     - LAT
     - LON
   * - 2018-03-08  1:00
     - a
     - 37.5
     - 127.5
     - 107
   * - 2018-03-08  1:00
     - b
     - 37
     - 126.5
     - 145
   * - 2018-03-08  1:00
     - c
     - 38.5
     - 126
     - 797
   * - 2018-03-08 1:00
     - a
     - 38
     - 128
     - 456
   * - 2018-03-08 1:00
     - d
     - 36.5
     - 127
     - 41
   * - 2018-03-08 1:00
     - c
     - 37
     - 126
     - 179



* LAT, LON 필드값을 이용해 클러스터링 및  COUNT집계함수 실행 결과를 테이블에 추가하는 예제 입니다.

.. code-block:: none

   ... | geostats lat lon count by OUT_TYPE

명령어 이후 테이블 (클러스터링 및 count 필드 추가)

.. list-table::
   :header-rows: 1

   * - cluster_id
     - latitude
     - longitude
     - OUT_TYPE
     - count
   * - 0_6_5
     - 37.75
     - 127.75
     - a
     - 2
   * - 0_6_5
     - 37.75
     - 127.75
     - c
     - 2
   * - 0_6_6
     - 37
     - 126.5
     - b
     - 1
   * - 0_6_6
     - 36.5
     - 127
     - d
     - 1



* LAT, LON 필드값을 이용해 클러스터링 및 SUM 집계함수 실행 결과를 테이블에 추가하는 예제 입니다.

.. code-block:: none

   ... | geostats lat lon sum(SYS_OUT) by OUT_TYPE

명령어 이후 테이블 (클러스터링 및 sum 필드 추가)

.. list-table::
   :header-rows: 1

   * - cluster_id
     - latitude
     - longitude
     - OUT_TYPE
     - sum(SYS_OUT)
   * - 0_6_5
     - 37.75
     - 127.75
     - a
     - 563
   * - 0_6_5
     - 37.75
     - 127.75
     - c
     - 976
   * - 0_6_6
     - 36.5
     - 127
     - d
     - 41



* LAT, LON 필드값을 이용해 클러스터링 및 COUNT,  SUM 집계함수 실행 결과를 테이블에 추가하는 예제 입니다.

.. code-block:: none

   ... | geostats lat lon count,sum(SYS_OUT) by OUT_TYPE

명령어 이후 테이블 (클러스터링 및 count, sum 필드 추가)

.. list-table::
   :header-rows: 1

   * - cluster_id
     - latitude
     - longitude
     - OUT_TYPE
     - count
     - sum(SYS_OUT)
   * - 0_6_5
     - 37.75
     - 127.75
     - a
     - 2
     - 563
   * - 0_6_5
     - 37.75
     - 127.75
     - c
     - 2
     - 976
   * - 0_6_6
     - 37
     - 126.5
     - b
     - 1
     - 145
   * - 0_6_6
     - 36.5
     - 127
     - d
     - 1
     - 41



* LAT, LON 필드값을 이용해 클러스터링 및 COUNT집계함수 실행 결과를 테이블에 추가하는 예제 입니다.( groub by 절 생략.)

.. code-block:: none

   ... | geostats lat lon count

명령어 이후 테이블 (클러스터링 및 count 필드 추가 )

.. list-table::
   :header-rows: 1

   * - cluster_id
     - latitude
     - longitude
     - count
   * - 0_6_5
     - 37
     - 126.5
     - 1
   * - 0_6_5
     - 37.5
     - 127.5
     - 1
   * - 0_6_5
     - 38.5
     - 128
     - 1


Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   ...| geostats latitude longitude aggr_funcs(, aggr_funcs)* (aggr_by)? (cell_size)* (level)* (bounds_sqr)*

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - latitude longitude
     - 위, 경도 한 쌍을 필수로 입력해야하며 십진수 도(DD)(ex 41.40338, 2.17403) 형식을 따라야합니다. (Latitude, 위도 / Longitude, 경도)
     - 필수
   * - aggr_funcs
     - 집계 함수를 나타내며, 통계 함수를 실행합니다. 아래 표와 같은 옵션이 존재합니다.
     - 필수
   * - aggr_by
     - 명령어 사용시 생략 가능하며 필드를 집계 기준으로 두어  ``group by`` 역할을 합니다. ``by`` 다음 ``필드명``\ 이 필요하며 다수의 필드명 입력이 가능합니다.
     - 옵션
   * - cell_size
     - 데이터 클러스터링을 하는 셀의 크기를 설정하며 (위,경도의)도 값을 의미합니다.  해당 옵션 **생략 시** default(size = 22.5) 값이 지정됩니다.\ :raw-html-m2r:`<br/>`\ ex) size = 15.5  (이 결과로 한 셀의 크기는 15.5로 생성됩니다.)
     - 옵션
   * - level
     - 위,경도 데이터를 전달 된 Level 에 따라 각각의 위치를 기록합니다.
     - 옵션
   * - bounds_sqr
     - 검색 초기결과 값 및 표시화면 제한을 위한 두 쌍의 위,경도를 지정(남서, 북동경계 좌표 순)합니다.  **생략 시** 전세계 화면 및 보유한 모든 결과를 보여줍니다.\ :raw-html-m2r:`<br/>`\ ex) bounds(35.73687,125.51806, 35.73687, 128.58325)
     - 옵션



* aggregation function list

.. list-table::
   :header-rows: 1

   * - 함수 명
     - 역할
     - 필수요소
     - 예시
   * - count
     - 대상의 수를 구하는 함수.
     - 괄호 및 필드명 미사용
     - count
   * - sum
     - 대상 필드의 합계를 구하는 함수.
     - 괄호 및 필드명
     - sum(Out)
   * - avg
     - 대상 필드의 평균을 구하는 함수.
     - 괄호 및 필드명
     - avg(Out)
   * - max
     - 대상 필드의 최고 값을 구하는 함수.
     - 괄호 및 필드명
     - max(Out)
   * - min
     - 대상 필드의 최저 값을 구하는 함수
     - 괄호 및 필드명
     - min(Out)


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   geostats_command : latitude longitude aggr_funcs aggr_by cell_size level bound_sqr

   latitude : field

   longitude : field

   aggr_funcs : aggr_funcs COMMA aggr_func
               | aggr_func

   aggr_func : WORD LPAREN field RPAREN
               | WORD

   aggr_by : BY field

   bound_sqr : BOUNDS LPAREN latlon COMMA latlon COMMA latlon COMMA latlon RPAREN

   cell_size : SIZE EQUALS DOUBLE

   level : LEVEL EQUALS NUMBER

   field : WORD

   latlon : DOUBLE

   WORD : \w+
   COMMA : ,
   LPAREN : \(
   RPAREN : \)
   EQUALS : \=
   SIZE : size|SIZE
   LEVEL : level|LEVEL
   BOUNDS : bounds|BOUNDS
   NUMBER : \d+
   BY : by|BY
   DOUBLE : [-+]?[0-9]+(\.([0-9]+)?([eE][-+]?[0-9]+)?|[eE][-+]?[0-9]+)
