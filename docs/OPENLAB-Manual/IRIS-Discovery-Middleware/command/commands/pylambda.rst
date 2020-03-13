.. role:: raw-html-m2r(raw)
   :format: html


pylambda
====================================================================================================

개요
----------------------------------------------------------------------------------------------------

해당 명령어는 Python의 lambda 함수를 실행 합니다.

설명
----------------------------------------------------------------------------------------------------

검색 결과에 Python lambda 함수를 실행합니다. 입력은 전달 되어진 테이블의 각 열을 의미하며, 해당 열을 가공하여 출력으로 보낼 수 있습니다. ``WITH`` 절에는 출력의 스키마를 입력해야 합니다. 만약 해당 부분이 생략 된다면, 자동으로 출력의 스키마를 계산합니다. 해당 계산 과정이 정확하지 않을 수 있고, 데이터가 많은 경우에는 많은 시간을 소요 할 수 있기 때문에, 스키마를 명시적으로 입력 하는 것이 좋습니다.

Examples
----------------------------------------------------------------------------------------------------

0번째 컬럼의 데이터중 ``2018``\ 이라는 숫자를 년도를 ``****``\ 으로 변환

.. code-block:: none

   ..| pylambda row: row[0].replace('2018', '****')

.. code-block:: none

   ..| pylambda row: row[0].replace('2018', '****') WITH output: STRING

입력 데이터에 1번째 컬럼의 데이터를 추가

.. code-block:: none

   ..| pylambda row: row + [row[1]]

.. code-block:: none

   ..| pylambda row: row + [row[0]] WITH a: string, b: string, c: int

입력 데이터의 0번째 컬럼이 "abc" 를 포함하는지 각 bool 값을 출력

.. code-block:: none

   ..| pylambda row: "abc" in row[0]

.. code-block:: none

   ..| pylambda row: "abc" in row[0] WITH output: boolean

입력 데이터의 LEVEL, HOST 필드를 선택하여 모든 필드의 값에서 ``info``\ 라는 값을 를 ``****``\ 으로 변환

.. code-block:: none

   * | fields LEVEL, HOST | pylambda row: [r.replace('info', '****') for r in row]

.. code-block:: none

   * | fields LEVEL, HOST | pylambda row: [r.replace('info', '****') for r in row] WITH log_level: string, host: string

Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   ... | pylambda lambda_expr [WITH schema]

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - lambda_expr
     - Python 의 lambda expression을 의미합니다. 단, ``lambda`` 키워드는 포함하지 않습니다. 또한, 인자는 ``row`` 하나만 들어오게 됩니다.\ :raw-html-m2r:`<br />`\ 예 : row: row[0].replace('2018', '****') (O)\ :raw-html-m2r:`<br />`\ 예 : lambda row: row[0].replace('2018', '****') (X)
     - 필수
   * - WITH schema
     - ``WITH`` 는 스키마를 직접 지정하겠음을 지시하는 예약어이며, ``schema``\ 는 schema 표현으로 col_name: *data_type 포맷입니다.\ :raw-html-m2r:`<br />`\ 예 : WITH column1: string, column2: int
     - 옵션


*data_type

.. list-table::
   :header-rows: 1

   * - 타입
   * - INT
   * - BIGINT
   * - BOOLEAN
   * - FLOAT
   * - DOUBLE
   * - STRING
   * - BINARY
   * - TIMESTAMP
   * - DECIMAL
   * - DECIMAL(precision, scale)
   * - DATE


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   clauses : tokens
           | tokens WITH tokens

   tokens : TOKEN
          | tokens TOKEN

   TOKEN = [^ ]+
