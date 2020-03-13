
fields
====================================================================================================

개요
----------------------------------------------------------------------------------------------------

검색 결과가 출력 될 field를 설정합니다.

설명
----------------------------------------------------------------------------------------------------

``+`` 혹은 ``-`` 기호를 필드명 앞에 사용하여 검색 결과가 출력 될 field를 설정 할 수 있습니다. 만약 ``+``\ 가 앞에 쓰였다면, 해당 field의 이름과 매칭되는 field들이 검색 결과에 출력됩니다. 만약 ``-``\ 가 앞에 쓰였다면, 현재 검색 결과 데이터의 필드 목록에서 해당 field가 제외된 검색 결과에 출력됩니다. 필드명 뒤에 ``*``\ 가 쓰일 수 있으며, 해당 패턴과 매치되는 모든 필드를 의미합니다.

Examples
----------------------------------------------------------------------------------------------------


* ``HR`` 그리고 ``PLAYERID`` field만을 출력하는 예제 입니다. 

.. code-block:: none

   ..| fields +HR, PLAYERID

.. code-block:: none

   ..| fields HR, PLAYERID

.. list-table::
   :header-rows: 1

   * - HR
     - PLAYERID
   * - 2
     - apple
   * - ...
     - ...

* 전체 필드에서 ``HR``\ 필드 만을 제외한 field를 출력합니다.

.. code-block:: none

   ..| fields -HR

.. list-table::
   :header-rows: 1

   * - TEAMID
     - PLAYERID
     - ...
   * - TOR
     - apple
     - ...
   * - ...
     - ...
     - ...

* ``RAW_`` 로 시작하는 모든 field를 제외한 field를 출력합니다.

.. code-block:: none

   ..| fields -RAW_*

.. list-table::
   :header-rows: 1

   * - TEAMID
     - PLAYERID
     - ...
   * - TOR
     - apple
     - ...
   * - ...
     - ...
     - ...


* 필드명이 한 단어가 아니라도 필드명 그대로 사용가능합니다. (``,`` 로 필드명을 구분 합니다.)

.. code-block:: none

   .. | fields + 필드 A, 필드 B, 필드_C

.. list-table::
   :header-rows: 1

   * - 필드 A
     - 필드 B
     - 필드_C
   * - 1
     - 2
     - 3


Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   ... | fields ([+|-])? FIELD_NAME(*)? (, FIELD_NAME(*)?)*

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - FIELD_NAME
     - field의 이름을 의미합니다.
     - 필수
   * - +|-
     - ``+`` 혹은 ``-``\ 로 주어진 전체 field를 보여지게 할 것인가 말 것인가를 결정 합니다.
     - 옵션
   * - *
     - ``*``\ , wildcard를 의미합니다.
     - 옵션


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   fields : field_list
          | MINUS field_list
          | PLUS field_list

   field_list : tokens
              | field_list COMMA tokens

   tokens : TOKEN
          | tokens TOKEN

   PLUS : +
   MINUS : -
   TOKEN : [^ |^,|^+|^-]+
   COMMA : ,
