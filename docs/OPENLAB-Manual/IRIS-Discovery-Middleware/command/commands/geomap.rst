.. role:: raw-html-m2r(raw)
   :format: html


geomap
====================================================================================================

개요
----------------------------------------------------------------------------------------------------

 이 명령어는 업로드 되어있는 컬렉션을 기반으로 사용자가 요청하는 테이블에 지역 경계(geometry) 정보를 제공합니다.

설명
----------------------------------------------------------------------------------------------------

 사용자가 선택한 컬렉션을 기반으로 지역 경계정보를 생성 합니다. 생성된 정보는 ``시각화`` 탭에 위치한 지도상에 표현됩니다. 사용자는 ``컬렉션 명``\ , 컬렉션과 같은 단위(국가, 도, 시 등) 정보를 포함한 ``대상 필드``\ 를 필히 입력하여야 합니다. 

Examples
----------------------------------------------------------------------------------------------------

검색대상이되는 데이터가 다음과 같이 존재합니다.

.. list-table::
   :header-rows: 1

   * - lat
     - lon
     - user_addr
     - OUT_TYPE
     - sum(SYS_OUT)
   * - 37.75
     - 127.75
     - 송파구
     - a
     - 563
   * - 37.75
     - 127.75
     - 강남구
     - c
     - 976
   * - 37
     - 126.5
     - 광진구
     - b
     - 145
   * - 36.5
     - 127
     - 과천시
     - d
     - 41


City 라는 컬렉션과 그의 대상이 되는 user_addr 필드를 지정한 예.

.. code-block:: none

   ... | geostats lat lon sum(sys_out) by OUT_TYPE | geomap City user_addr

명령어 이후 테이블 (Collection 적용)

.. list-table::
   :header-rows: 1

   * - lat
     - lon
     - user_addr
     - collection
     - geometry
     - sum(SYS_OUT)
   * - 37.75
     - 127.75
     - 송파구
     - City
     - "geometry": { "type": "Polygon", "coordinates": [ [ [ 42.24123, 32.65007 ], [ 27.23065, 27.27066 ], .. ] ] }
     - 563
   * - 37.75
     - 127.75
     - 강남구
     - City
     - "geometry": { ...
     - 976
   * - 37
     - 126.5
     - 광진구
     - City
     - "geometry": { ...
     - 145
   * - 36.5
     - 127
     - 과천시
     - City
     - "geometry": { ...
     - 41


City 라는 컬렉션과 그의 대상이 되는 user_addr 필드를 지정한 예 ( all_feature 사용).

.. code-block:: none

   ... | geostats lat lon sum(sys_out) by OUT_TYPE | geomap City user_addr ALL

명령어 이후 테이블 (Collection 적용, all 옵션 적용)

.. list-table::
   :header-rows: 1

   * - lat
     - lon
     - user_addr
     - sum(SYS_OUT)
     - collection
     - geometry
   * - 37.75
     - 127.75
     - 송파구
     - City
     - "geometry": { "type": "Polygon", "coordinates": [ [ [ 42.24123, 32.65007 ], [ 27.23065, 27.27066 ], .. ] ] }
     - 563
   * - 37.75
     - 127.75
     - 강남구
     - City
     - "geometry": { ...
     - 976
   * - 37
     - 126.5
     - 광진구
     - City
     - "geometry": { ...
     - 145
   * - 36.5
     - 127
     - 과천시
     - City
     - "geometry": { ...
     - 41
   * - None
     - None
     - 하남시
     - City
     - "geometry": { ...
     - None
   * - None
     - None
     - 서초구
     - City
     - "geometry": { ...
     - None
   * - ...
     - ...
     - ...
     - ...
     - ...
     - ...


City 라는 컬렉션과 그의 대상이 되는 user_addr 필드를 지정한 예.

.. code-block:: none

   * | geomap City user_addr

명령어 이후 테이블 (Collection 적용)

.. list-table::
   :header-rows: 1

   * - user_addr
     - collection
     - geometry
     - sum(SYS_OUT)
   * - 송파구
     - City
     - "geometry": { "type": "Polygon", "coordinates": [ [ [ 42.24123, 32.65007 ], [ 27.23065, 27.27066 ], .. ] ] }
     - 563
   * - 강남구
     - City
     - "geometry": { ...
     - 976
   * - 광진구
     - City
     - "geometry": { ...
     - 145
   * - 과천시
     - City
     - "geometry": { ...
     - 41


Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   GEOMAP collection target_field value_field all_feature bound_sqr

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - collection
     - 콜렉션의 이름이며, 사용자가 업로드하거나 앞서 업로드 된 콜렉션 명을 입력합니다.
     - 필수
   * - target_field
     - 현재 보유한 테이블의 필드 중 컬렉션의 정보와 매칭할 타겟 필드입니다.
     - 필수
   * - value_field
     - 앞서 생성된 통계의 결과가 다수일 경우에 한하여 사용되며, geomap에 사용될 데이터가 포함된 필드를 선택 해야합니다. :raw-html-m2r:`<br />`\ 생략 시 인풋 데이터 프레임의 마지막 필드로 지정 됩니다.
     - 옵션
   * - all_feature
     - 생략 시 인풋 데이터 프레임의 마지막 필드로 지정 됩니다.'all' 입력 시 데이터를 포함하지 않는 collection 까지 모두 반환 됩니다.
     - 옵션
   * - bounds_sqr
     - 검색 초기결과 값 및 표시화면 제한을 위한 두 쌍의 위,경도를 지정(남서, 북동경계 좌표 순)합니다.  미 입력시 전세계 화면 및 보유한 모든 결과를 보여줍니다.\ :raw-html-m2r:`<br />`\ 예 : bounds(35.73687,125.51806, 35.73687, 128.58325)
     - 옵션


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   geomap_command : collection target_field value_field all_feature bound_sqr
   collection : WORD
   target_field : FIELD
   value_field : FIELD
               |
   all_feature : ALL
               | 
   bound_sqr : BOUNDS LPAREN latlon COMMA latlon COMMA latlon COMMA latlon RPAREN
             |
   latlon : DOUBLE
   FIELD : WORD

   GEOMAP = geomap
   WORD = \w+
   COMMA = ,
   LPAREN = \(
   RPAREN = \)
   ALL = all | ALL
   BOUNDS = bounds | BOUNDS
   DOUBLE = [-+]?[0-9]+(\.([0-9]+)?([eE][-+]?[0-9]+)?|[eE][-+]?[0-9]+)

API Request & Response
----------------------------------------------------------------------------------------------------


* 
  POST


  * 
    URL

    .. code-block:: none

       POST /angora/iris-figure/jobs?

  * 
    body

    .. code-block:: none

       { ...   
           "q" : "* | GEOMAP collection target_field value_field all_feature
                  bounds(south_lat,west_lon,north_lat,east_lon)"
       ...}

  * 
    Example(Request)

    .. code-block:: none

       { ...
           "q" : "* | geomap City user_addr value ALL
               bounds(33.2815850538,125.5167675782,35.73680912846,128.5832363282)"
       ...}

* 
  GET


  * 
    URL

    .. code-block:: none

       GET /angora/iris-figure/jobs/[sid]?

  * 
    Reponse (명령어 : geomap City user_addr ALL)통계 탭

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
             "name": "latitude"
           }
           {
             "grouped": false, 
             "type": "LONG", 
             "name": "longitude"
           },
           {
             "grouped": true, 
             "type": "TEXT", 
             "name": "user_addr"
           }, 
           {
             "grouped": false, 
             "type": "TEXT", 
             "name": "collection"
           },
           {
             "grouped": false, 
             "type": "TEXT", 
             "name": "geometry"
           },
           {
             "grouped": false, 
             "type": "LONG", 
             "name": "count"
           }
         ], 
         "isEnd": true, 
         "results": [
           [
             "33.36727",
             "126.52918",
             "송파구",
             "City",
             ""geometry": { "type": "Polygon", "coordinates": [ [ [ 42.24757091725737, 32.650072333309225 ], [ 27.230651483005886, 27.270663967422294 ] ] ] }"
             1
         }

           ], 
           [
             "33.367237",
             "126.529198",
             "강남구",
             "City",
             ""geometry": { "type": "Polygon", "coordinates": [ [ [ 61.210817091725737, 35.650072333309225 ], [ 62.230651483005886, 35.270663967422294 ] ] ] }",
             3
           ]
         ]
       }

  * 
    Response (collection 명 오타 상황)

    .. code-block:: none

       {
         "message": "[Cityy] is Not in Collection list.", 
         "type": "<class 'angora.exceptions.AngoraException'>"
       }
