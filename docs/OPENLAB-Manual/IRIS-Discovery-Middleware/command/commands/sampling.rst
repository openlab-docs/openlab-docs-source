.. role:: raw-html-m2r(raw)
   :format: html


sampling
====================================================================================================

sampling 명령어 문법 및 연동규격 설명서 입니다.

개요
----------------------------------------------------------------------------------------------------

 이 명령어는 Data-Discovery-Service ML 관련 명령어 이며, 사용자가 입력한 수 만큼의 데이터를 반환합니다.

설명
----------------------------------------------------------------------------------------------------

 이 명령어는 사용자가 입력한 수 만큼  랜덤으로 기존의 데이터 프레임에서 선택하여 반환합니다. Count 와 Ratio 방법을 지원하며, 각각 n개의 랜덤 데이터, n(%)의 랜덤 데이터를 의미합니다. 

Examples
----------------------------------------------------------------------------------------------------


* 앞서 넘어온 데이터가 다음과 같습니다.

.. list-table::
   :header-rows: 1

   * - index
     - id
     - value
   * - 0
     - a
     - 654
   * - 1
     - b
     - 1958
   * - 2
     - c
     - 835
   * - 3
     - d
     - 9841
   * - 4
     - e
     - 65



* COUNT 방법을 적용한 경우.

.. code-block:: none

   ... | sampling COUNT 3

명령어 이후 테이블

.. list-table::
   :header-rows: 1

   * - index
     - id
     - value
   * - 2
     - c
     - 835
   * - 0
     - a
     - 654
   * - 1
     - b
     - 1958



* RATIO 방법을 적용한 경우.

.. code-block:: none

   ... | sampling RATIO 0.2

명령어 이후 테이블

.. list-table::
   :header-rows: 1

   * - index
     - id
     - value
   * - 0
     - a
     - 654


Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   ... | sampling ALG portion

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - ``ALG``
     - sampling 방법 입니다. 아래 표의 alg를 지원합니다.
     - 필수
   * - ``portion``
     - 취하고자 하는 데이터 개수를 의미 합니다. 정수의 숫자는 개수를 의미하고, 소숫점을 포함한 1.0> n > 0.0 의 수는 전체 데이터 중의 비율을 의미합니다.\ :raw-html-m2r:`<br/>`\ ex) 100개의 데이터 중\ :raw-html-m2r:`<br/>`\ ``20`` -> 20개의 데이터\ :raw-html-m2r:`<br/>`\ ``0.4`` -> 40개의 데이터
     - 필수



* ``alg`` list

.. list-table::
   :header-rows: 1

   * - alg
     - description
   * - COUNT
     - n 개의 랜덤 데이터를 반환합니다.
   * - RATIO
     - n(%)의 랜덤 데이터를 반환합니다.


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   sampling_command : alg portion

   alg : COUNT
       | RATIO

   portion : NUMBER
           | double                   

   double : NUMBER DOT NUMBER

   DOT : \.
   COUNT : (?i)count
   RATIO : (?i)ratio
   NUMBER : \d+
