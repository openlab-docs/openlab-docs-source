.. role:: raw-html-m2r(raw)
   :format: html


geoip
====================================================================================================

geoip  명령어 문법 및 연동규격 설명서 입니다.

개요
----------------------------------------------------------------------------------------------------

이 명령어는 ip가 포함된 필드를 기반으로 위, 경도 등의 추가정보를 제공합니다.

설명
----------------------------------------------------------------------------------------------------

해당 필드에 포함된 x.x.x.x (IPV4) 형식의 ip 주소에 해당하는 위도, 경도 와 해당국가, 도, 시 그리고 ZIP code(postal code) 정보를 사용자의 요청에 맞게 새로운 필드로 제공합니다. 생성된 필드는 기존 테이블의 마지막에 위치하게 됩니다.  

Examples
----------------------------------------------------------------------------------------------------


* 명령어 이전 테이블

.. list-table::
   :header-rows: 1

   * - UPDATE_TIME
     - IP_address
     - IN_BYTES_AVG
   * - 2018/03/08 01:00:00
     - 211.219.77.93
     - 107
   * - 2018/03/08 01:00:00
     - 118.130.235.213
     - 145
   * - 2018/03/08 01:00:00
     - 61.74.127.215
     - 797



* A. IP_address 필드값을 이용해 default 값인 위도와 경도를 테이블에 추가하는 예제 입니다.

.. code-block:: none

   ... | geoip IP_address

명령어 이후 테이블 (lat, lon필드 추가)

.. list-table::
   :header-rows: 1

   * - UPDATE_TIME
     - IP_address
     - IN_BYTES_AVG
     - LATITUDE
     - LONGITUDE
   * - 03/08 01:00:00
     - 211.219.77.93
     - 107
     - 37.43861
     - 127.13778
   * - 03/08 01:00:00
     - 118.130.235.213
     - 145
     - 37.47722
     - 126.86639
   * - 03/08 01:00:00
     - 61.74.127.215
     - 797
     - 37.56826
     - 126.97783



* B. IP_address 필드값을 이용해 모든 정보를 추가하는 예제 입니다.

.. code-block:: none

   ... | geoip IP_address ALL

  명령어 이후 테이블 (lat, lon, ctry, state, city, zip - 모든 정보 필드 추가)

.. list-table::
   :header-rows: 1

   * - UPDATE_TIME
     - IP_address
     - IN_BYTES_AVG
     - LATITUDE
     - LONGITUDE
     - ...
     - ZIP_CODE
   * - 03/08 01:00:00
     - 211.219.77.93
     - 107
     - 37.43861
     - 127.13778
     - ...
     - 461-805
   * - 03/08 01:00:00
     - 118.130.235.213
     - 145
     - 37.47722
     - 126.86639
     - ...
     - 423-836
   * - 03/08 01:00:00
     - 61.74.127.215
     - 797
     - 37.56826
     - 126.97783
     - ...
     - 100-101



* C. IP_address 필드값을 이용해 사용자 설정 정보를 추가하는 예제 입니다.

.. code-block:: none

   ... | geoip IP_address state, city, zip

  명령어 이후 테이블 ( 사용자가 선택한 옵션 - state, city, zip 필드 추가)

.. list-table::
   :header-rows: 1

   * - UPDATE_TIME
     - IP_address
     - IN_BYTES_AVG
     - STATE
     - CITY
     - ZIP_CODE
   * - 03/08 01:00:00
     - 211.219.77.93
     - 107
     - Gyeonggi-do
     - Seongnam
     - 461-805
   * - 03/08 01:00:00
     - 118.130.235.213
     - 145
     - Gyeonggi-do
     - Kwangmyong
     - 423-836
   * - 03/08 01:00:00
     - 61.74.127.215
     - 797
     - Gyeonggi-do
     - Seoul
     - 100-101


Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   ...| geoip field (option(, option)*)?

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - field
     - 대상인 필드를 의미하며, x.x.x.x (IPV4) 형식의 ip 주소만 가능합니다.
     - 필수
   * - option
     - 기존 테이블에 추가될 정보를 설정합니다. 생략 시 default 정보가 추가되며, ``ALL`` 또는 다중입력으로 사용자가 추가될 정보를 설정할 수 있습니다.\ :raw-html-m2r:`<br/>`\ ``default``\ -위도(lat)와 경도(lon)가 추가됩니다.\ :raw-html-m2r:`<br/>`\ ``ALL``\ -모든 정보를 출력합니다.  ``DEL``\ 명령어로 사용하지 않을 데이터를 생략 가능합니다.\ :raw-html-m2r:`<br/>`\ 사용자 설정-\ ``lat`` 위도(latitude), ``lon`` 경도(longitude),\ ``ctry`` 국가(counrty),\ ``state`` 도,\ ``city`` 시,\ ``zip`` zip 코드\ :raw-html-m2r:`<br/>`\ 주어진 IP 주소에 대한 데이터가 존재하지 않으면 다음과 같이 default 값이 설정 됩니다. (\ ``default = na``\ )
     - 옵션


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   geoip_command : GEOIP field options

   options : options COMMA option
           | option

   option : WORD

   field : WORD

   t_WORD     = \w+
   t_COMMA    = ,
