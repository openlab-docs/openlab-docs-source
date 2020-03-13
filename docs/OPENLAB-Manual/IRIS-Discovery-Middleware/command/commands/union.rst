
union
====================================================================================================

개요
----------------------------------------------------------------------------------------------------

이 명령어는 다른 데이터 모델과 union 을 할 때 사용됩니다.

설명
----------------------------------------------------------------------------------------------------

현재 데이터모델에 다른 데이터모델을 union 하는 명령어 입니다.

Examples
----------------------------------------------------------------------------------------------------
* unionA 데이터 모델

.. list-table::
   :header-rows: 1

   * - AAA
     - BBB
   * - 1
     - 2
   * - 3
     - 4
   * - 5
     - 6

* unionB 데이터 모델

.. list-table::
   :header-rows: 1

   * - AAA
     - BBB
   * - 1
     - 2
   * - 5
     - 4
   * - 3
     - 6


* 현재 데이터모델(``unionA``)과 다른 데이터모델(``unionB``)을 조인하는 예제입니다.

* union all 명령 예시

.. code-block:: none

   ... | union all unionB


.. list-table::
   :header-rows: 1

   * - AAA
     - BBB
   * - 1
     - 2
   * - 3
     - 4
   * - 5
     - 6
   * - 1
     - 2
   * - 5
     - 4
   * - 3
     - 6

* union 명령 예시

.. code-block:: none

   ... | union unionB


.. list-table::
   :header-rows: 1

   * - AAA
     - BBB
   * - 1
     - 2
   * - 3
     - 4
   * - 5
     - 6
   * - 5
     - 4
   * - 3
     - 6

* union ... order by ... ASC 명령 예시

.. code-block:: none

   ... | union unionB order by AAA (ASC)


.. list-table::
   :header-rows: 1

   * - AAA
     - BBB
   * - 1
     - 2
   * - 3
     - 4
   * - 3
     - 6
   * - 5
     - 6
   * - 5
     - 4

* union ... order by ... DESC 명령 예시

.. code-block:: none

   ... | union unionB order by AAA DESC


.. list-table::
   :header-rows: 1

   * - AAA
     - BBB
   * - 5
     - 6
   * - 5
     - 4
   * - 3
     - 4
   * - 3
     - 6
   * - 1
     - 2

Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   ... | union (ALL)? MODEL_NAME (ORDER BY field(, field)* (ASC | DESC)? )?

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - ALL
     - ``union all`` 명령은 ``unionA``, ``unionB`` 데이터를 그대로 합치는 명령어 입니다. ``union`` 명령은 중복된 값을 제거하는 명령어입니다.
     - 옵션
   * - MODEL_NAME
     - union을 할 데이터모델의 이름을 의미합니다. **모델명에 공백이 포함되는 경우 ``' '`` (Single quote)로 감싸줘야 합니다.**
     - 필수
   * - (ORDER BY field(, field)* (ASC / DESC)? )?
     - union 을 한 뒤, 데이터를 sort 하는 명령어 입니다. 지정한 ``field`` 를 기준으로 데이터를 정렬하고, ``ASC`` , ``DESC`` 를 지정 할 수 있습니다. 지정 하지 않으면 ``default = ASC`` 입니다.
     - 옵션


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

    clauses : model_name
            | model_name ORDER BY term
            | model_name ORDER BY term is_asc
            | model_name ORDER BY list_term
            | model_name ORDER BY list_term is_asc
            | ALL model_name
            | ALL model_name ORDER BY term
            | ALL model_name ORDER BY term is_asc
            | ALL model_name ORDER BY list_term
            | ALL model_name ORDER BY list_term is_asc

    is_asc : ASC
           | DESC

    model_name : term
               | sq_term_sq

    list_term : term COMMA term
              | list_term COMMA term

    sq_term_sq : SQ term SQ
               | SQ multiple_term SQ

    multiple_term : term term
                  | multiple_term term

    term : STR_TOKEN
         | NUMBER

    t_SQ = r"\'"
    t_COMMA = r","
    t_NUMBER = r"\d+(\.\d+)?"
    t_STR_TOKEN = r"([^\s=\',])+"
