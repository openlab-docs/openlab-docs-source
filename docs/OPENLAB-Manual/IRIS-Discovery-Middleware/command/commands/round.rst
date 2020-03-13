.. role:: raw-html-m2r(raw)
   :format: html


round
====================================================================================================

개요
----------------------------------------------------------------------------------------------------

이 명령어는 지정된 **실수형 필드**\ 의 소수점을 **반올림** 하는 명령어 입니다.

설명
----------------------------------------------------------------------------------------------------

실수형 필드의 소수점을 반올림 합니다. 예를 들어, ``3.14159265359`` 값을 소수점 3자리로 반올림하면 ``3.142`` 로 결과가 도출됩니다.

Examples
----------------------------------------------------------------------------------------------------

모든 숫자 필드를 소수점 5자리로 반올림합니다.

.. code-block:: none

   ... | round 5

``AAA``\ 필드를 소수점 5자리로 반올림합니다.

.. code-block:: none

   ... | round 5 col=AAA
   ... | round 5 col=[AAA]
   ... | round [5] col=[AAA]

``AAA`` 필드를 소수점 5자리로 반올림하고, ``BBB`` 필드를 소수점 2자리로 반올림합니다. 

.. code-block:: none

   ... | round [5,2] col=[AAA, BBB]

``AAA`` 필드와 ``BBB`` 필드를 모두 소수점 5자리로 반올림합니다. 

.. code-block:: none

   ... | round 5 col=[AAA, BBB]
   ... | round [5,5] col=[AAA, BBB]

index가 1 인 필드 ``AAA`` 를 소수점 5자리로 반올림합니다.

.. code-block:: none

   ... | round 5 idx=1
   ... | round 5 idx=[1]
   ... | round [5] idx=[1]

index가 1 인 필드 ``AAA`` 는 소수점 5자리, index가 2 인 필드 ``BBB``\ 는 소수점 2자리로 반올림합니다.

.. code-block:: none

   ... | round [5,2] idx=[1,2]

결과 데이터의 포멧을 ``string``\ 으로 지정을 하기 위해서는 ``toSring``\ 옵션을 ``True``\ 로 지정 해야합니다.

.. code-block:: none

   ... | round 5 col=[AAA, BBB] toString=True

Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   round [N|LIST] ([col|idx]=[field_name|field_idx|LIST])? (toString=[True|False])?

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - [%s|%s]
     - or 조건입니다. 1개만 사용할 수 있습니다.\ :raw-html-m2r:`<br />`\ 예 : [col|idx] -> col
     - -
   * - LIST
     - LIST 형태로 작성할 수 있는 파라미터 입니다.
     - -
   * - N
     - 숫자 필드의 반올림 위치 입니다.\ :raw-html-m2r:`<br />`\ :raw-html-m2r:`<br />`\ LIST로 작성할 경우 선택한 필드 각각의 반올림 위치 입니다.\ :raw-html-m2r:`<br />`\ :raw-html-m2r:`<br />`\ 반올림 위치를 ``LIST``\ 로 작성시 ``col/idx`` 의 값도 ``LIST``\ 로 작성해야합니다.\ :raw-html-m2r:`<br />`\ 예 : 5 :raw-html-m2r:`<br />`\ 예 : [5, 2]
     - 필수
   * - col
     - 필드 이름을 사용합니다.
     - 옵션
   * - idx
     - 필드 인덱스를 사용합니다.\ :raw-html-m2r:`<br />`\ 인덱스는 0 에서 시작합니다.
     - 옵션
   * - field_name
     - 반올림 할 필드 이름입니다.\ :raw-html-m2r:`<br />`\ 예 : [field1, field2,...]\ :raw-html-m2r:`<br />`\ 예 : field1
     - 옵션
   * - field_idx
     - 반올림 할 필드의 인덱스 입니다.\ :raw-html-m2r:`<br />`\ 예 : [field_index1, field_index1,...]\ :raw-html-m2r:`<br />`\ 예 : field_index1
     - 옵션
   * - toString
     - 결과의 리턴 포멧을 정하는 옵션입니다. (\ ``default = False``\ )\ :raw-html-m2r:`<br />`\ ``True``\ 로 설정한다면 반환 포멧은 ``string``\ 입니다.\ :raw-html-m2r:`<br />`\ 예 : data=\ ``3.14`` , 반올림=\ ``4``\ , toString=\ ``True`` --> ``"3.1400"``\ :raw-html-m2r:`<br />`\ 예 : data=\ ``3.14`` , 반올림=\ ``4``\ , toString=\ ``False`` --> ``3.14``\ :raw-html-m2r:`<br />`\ 예 : data=\ ``3.14159`` , 반올림=\ ``4``\ , toString=\ ``True`` --> ``"3.1416"``\ :raw-html-m2r:`<br />`\ 예 : data=\ ``3.14159`` , 반올림=\ ``4``\ , toString=\ ``False`` --> ``3.1416``
     - 옵션


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   round_expr : NUMBER
               | NUMBER COL EQUAL TOKEN
               | NUMBER COL EQUAL LIST
               | NUMBER IDX EQUAL NUMBER
               | NUMBER IDX EQUAL LIST
               | LIST COL EQUAL LIST
               | LIST IDX EQUAL LIST
               | NUMBER TOSTRING EQUAL TOKEN
               | NUMBER COL EQUAL TOKEN TOSTRING EQUAL TOKEN
               | NUMBER COL EQUAL LIST TOSTRING EQUAL TOKEN
               | NUMBER IDX EQUAL NUMBER TOSTRING EQUAL TOKEN
               | NUMBER IDX EQUAL LIST TOSTRING EQUAL TOKEN
               | LIST COL EQUAL TOKEN TOSTRING EQUAL TOKEN
               | LIST COL EQUAL LIST TOSTRING EQUAL TOKEN
               | LIST IDX EQUAL NUMBER TOSTRING EQUAL TOKEN
               | LIST IDX EQUAL LIST TOSTRING EQUAL TOKEN

   NUMBER : \d+
   COL : col|COL
   IDX : idx|IDX
   TOSTRING : toString
   EQUAL : \=
   LIST : \[[^\[\]]+\]
   TOKEN : [^ \t=]+
