
join
====================================================================================================

개요
----------------------------------------------------------------------------------------------------

이 명령어는 다른 데이터 모델과 join을 할 때 사용됩니다.

설명
----------------------------------------------------------------------------------------------------

이 명령어는 다른 데이터 모델과 join을 할 때 사용됩니다. ``JOIN_TYPE`` 은 ``INNER`` 및 ``OUTER`` 조인 등 조인의 타입을 설정해 줄 수 있으며, ``JOIN_MODEL`` 은 조인할 데이터 모델을 지정할 수 있습니다. ``CONDITIONS`` 는 조인 조건절을 의미합니다. 

Examples
----------------------------------------------------------------------------------------------------


* 
  현재 데이터모델(\ ``DEPT``\ )과 다른 데이터모델(\ ``EMP``\ )을 조인하는 예제입니다.

* 
  ``CROSS`` 조인(조건 없음)

.. code-block:: none

   ... | join EMP


* ``INNER`` 조인(동등 조인)

.. code-block:: none

   ... | join inner EMP DEPT.ID = EMP.ID


* 다중 조건절 조인

.. code-block:: none

   ... | join inner EMP DEPT.ID = EMP.ID and EMP.ID > 34


* 데이터모델에 공백이 있는 경우(\ ``DEPT`` 와 ``EMP test`` 데이터모델)

.. code-block:: none

   ... | join inner 'EMP test' DEPT.ID = EMP test.ID and EMP test.ID > 34

Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   ... | join (JOIN_TYPE)? MODEL_NAME (CONDITIONS)?

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - JOIN_TYPE
     - ``CROSS``\ , ``INNER``\ , ``OUTER``\ , ``LEFT_OUTER`` 과 ``RIGHT_OUTER`` 가 올 수 있습니다. 기본값은 ``CROSS`` 입니다.
     - 옵션
   * - MODEL_NAME
     - 조인을 할 데이터모델의 이름을 의미합니다. **모델명에 공백이 포함되는 경우 ``' '``\ (Single quote)로 감싸줘야 합니다.**
     - 필수
   * - CONDITIONS
     - 조인 조건을 의미합니다. SQL JOIN QUERY 의 ON 절과 유사합니다. ``CROSS`` 조인의 경우 생략할 수 있습니다.
         예를 들어, ``DEPT``\ , ``EMP`` 두 모델의 ``ID`` 가 일치하는 조인을 수행하는 경우 ``join EMP DEPT.ID = EMP.ID`` 와 같이 사용할 수 있습니다.
     - 옵션


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   clauses : tokens
           | jointype tokens
           | tokens conditions
           | jointype tokens conditions

   jointype : CROSS
           | INNER
           | OUTER
           | LEFT_OUTER
           | RIGHT_OUTER

   tokens : TOKEN
           | STRING

   conditions : TOKEN
               | STRING
               | TOKEN conditions
               | STRING conditions
