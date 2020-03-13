
modeldata
====================================================================================================

modeldata명령어 문법 및 연동규격 설명서 입니다.

개요
----------------------------------------------------------------------------------------------------

 이 명령어는 Data-Discovery-Service ML 관련 명령어 이며, 사용자가 입력한 한 데이터를 데이터 프레임으로 반환 합니다.

설명
----------------------------------------------------------------------------------------------------

 이 명령어는 사용자가 입력한 데이터를 데이터 프레임으로 생성 후, 다음 명령어의 input data로 전달합니다. 학습된 ML 모델을 확인하거나 명령어의 기능을 확인할 때 사용 가능합니다.

Examples
----------------------------------------------------------------------------------------------------


* 앞서 넘어온 데이터와 무관하게 작동 합니다.

.. list-table::
   :header-rows: 1

   * - None
     - None
     - None
   * - ...
     - ...
     - ...



* 3개의 a, b ,c 필드를 지정한 예.

.. code-block:: none

   ... | modeldata [[a,b,c],[0,0,0],[1,1,1],[2,2,2]]

명령어 이후 테이블

.. list-table::
   :header-rows: 1

   * - a
     - b
     - c
   * - 0
     - 0
     - 0
   * - 1
     - 1
     - 1
   * - 2
     - 2
     - 2



* 
  1개의 a 필드를 지정한 예.

  .. code-block:: none

     ... | modeldata [[a],[0],[1],[2],[3],[4]]

명령어 이후 테이블

.. list-table::
   :header-rows: 1

   * - a
   * - 0
   * - 1
   * - 2
   * - 3
   * - 4



* 
  3개의 asd213123, asdf_aa, afsdd_Aa 필드를 지정한 예.

  .. code-block:: none

     ... | modeldata [[asd213123,asdf_aa,afsdd_Aa],[0,1,2],[2,3,4]]

명령어 이후 테이블

.. list-table::
   :header-rows: 1

   * - asd213123
     - asdf_aa
     - afsdd_Aa
   * - 0
     - 1
     - 2
   * - 2
     - 3
     - 4


Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   ...| modeldata [[field(, field)*],[data(, data)*](,[data(, data)*])*]

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - field
     - 테이블의 필드 이름이 되는 데이터. ``,``\ 로 구분
     - 필수
   * - data
     - 테이블의 row 데이터. ``,``\ 로 구분. *주의: 각 column의 데이터 포멧은 일정 해야합니다.*
     - 필수


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   modeldata_command : table

   table : LBRAKET all_data RBRAKET

   all_data : data
           | all_data COMMA data

   data : LBRAKET part RBRAKET

   part : any
       | part COMMA any

   any : WORD
       | NUMBER
       | double
       | word_number

   double : NUMBER DOT NUMBER

   word_number : WORD NUMBER
               | NUMBER WORD

   WORD : \w+
   COMMA : ,
   LBRACKET : \[
   RBRACKET : \]
   DOT : \.
   NUMBER : \d+
