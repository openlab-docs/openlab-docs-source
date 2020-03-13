.. role:: raw-html-m2r(raw)
   :format: html


scaler
====================================================================================================

개요
----------------------------------------------------------------------------------------------------

scaling을 진행하는 명령어 입니다.

설명
----------------------------------------------------------------------------------------------------

input으로 받은 DataFrame과 파라미터로 scaling하려는 field명을 입력받습니다. 선택한 field끼리 벡터화 한 후,  scaling을 진행하고 결과 벡터값을 다시 field 단위로 쪼개 하나의 숫자로 변환하여 결과적으로 한 field씩 scaling된 결과값을 출력합니다.

Examples
----------------------------------------------------------------------------------------------------

대상이 되는 데이터가 다음과 같이 존재합니다.

.. list-table::
   :header-rows: 1

   * - a
     - b
     - c
     - d
     - species
   * - 5.1
     - 3.5
     - 4.0
     - 0.2
     - Iris-setosa
   * - 6.3
     - 3.7
     - 4.9
     - 0.1
     - Iris-setosa
   * - 7.8
     - 2.0
     - 3.5
     - 0.3
     - Iris-versicolor
   * - 6.1
     - 3.1
     - 3.8
     - 0.2
     - Iris-virginica


a,b,c,d 필드를 minmax scaling한 예

.. code-block:: none

   ... | scaler minmax a to minmax_a, b to minmax_b, c to minmax_c, d to minmax_d

명령어 이후 테이블(minmax 적용)

.. list-table::
   :header-rows: 1

   * - a
     - b
     - c
     - d
     - species
     - minmax_a
     - minmax_b
     - minmax_c
     - minmax_d
   * - 5.1
     - 3.5
     - 4.0
     - 0.2
     - Iris-setosa
     - 0.00
     - 0.88
     - 0.36
     - 0.50
   * - 6.3
     - 3.7
     - 4.9
     - 0.1
     - Iris-setosa
     - 0.44
     - 1.00
     - 1.00
     - 0.00
   * - 7.8
     - 2.0
     - 3.5
     - 0.3
     - Iris-versicolor
     - 1.00
     - 0.00
     - 0.00
     - 1.00
   * - 6.1
     - 3.1
     - 3.8
     - 0.2
     - Iris-virginica
     - 0.37
     - 0.65
     - 0.21
     - 0.50


a,b,c,d 필드를 standard scaling한 예

.. code-block:: none

   ... | scaler standard a to _a, b to _b, c to _c, d to _d

명령어 이후 테이블(standard적용)

.. list-table::
   :header-rows: 1

   * - a
     - b
     - c
     - d
     - species
     - _a
     - _b
     - _c
     - _d
   * - 5.1
     - 3.5
     - 4.0
     - 0.2
     - Iris-setosa
     - 4.57
     - 4.61
     - 6.63
     - 2.44
   * - 6.3
     - 3.7
     - 4.9
     - 0.1
     - Iris-setosa
     - 5.65
     - 4.87
     - 8.12
     - 1.22
   * - 7.8
     - 2.0
     - 3.5
     - 0.3
     - Iris-versicolor
     - 6.99
     - 2.63
     - 5.80
     - 3.67
   * - 6.1
     - 3.1
     - 3.8
     - 0.2
     - Iris-virginica
     - 5.47
     - 4.08
     - 6.30
     - 2.44


Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   SCALER alg fields_as_out

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - alg
     - 사용할 scaler에 대한 정보입니다. :raw-html-m2r:`<br />`\ minmax / standard 중 원하는 scaling방법을 입력할 수 있습니다.
     - 필수
   * - fields_as_out
     - 원하는 input 필드명과 output 필드명들입니다.\ :raw-html-m2r:`<br />`\ 예 : input_name1 to ouput_name1, input_name2 to ouput_name2,...
     - 필수


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   minmaxscaler_command : alg field_as_out

   alg : WORD

   field_as_out : params

   params : param
          | params COMMA param

   param : field TO field
         | field

   field : WORD
   WORD = \w+
   COMMA = ,
   TO = to
      | TO
