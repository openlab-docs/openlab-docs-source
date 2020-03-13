
search
====================================================================================================

개요
----------------------------------------------------------------------------------------------------

이 명령어는 전문 검색(full-text search)을 하는데 사용 됩니다.

설명
----------------------------------------------------------------------------------------------------

주어진 키워드를 기반으로 전문 검색(full-text search) 실행하게 됩니다. 키워드, 혹은 인용 부호(\ ``"`` 혹은 ``'``\ )로 감싸져 있는 단어 및 문장, wildcard 등을 이용하여 검색이 가능합니다. 이 명령어는 암묵적으로 제일 앞에서 실행 될 때 생략 될 수 있습니다. ``search`` 뒤로는 keyword들의 나열이 올 수 있습니다. 이 경우 ``AND`` 조건이 생략되어 들어가 있는 것으로 인식합니다. 또한, ``*`` 혹은 ``search`` 두 가지는 명령어 혹은 keyword를 생략한 형태로, 전체 검색을 의미하게 됩니다. 명시적으로 ``OR`` 조건을 줄 수 있습니다.

Examples
----------------------------------------------------------------------------------------------------

``player1``\ , ``player2`` 그리고 ``player3``\ 에 관련된 문서를 검색합니다.

.. code-block:: none

   player1 player2 player3

전체 검색을 합니다.

.. code-block:: none

   *

Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   ... | search (KEYWORD (([AND|OR])? KEYWORD)*)?

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - KEYWORD
     - 검색할 키워드를 의미합니다.
     - 필수
   * - [AND|OR]
     - ``AND``\ /\ ``and`` 혹은 ``OR``\ /\ ``or``\ 를 뜻합니다. ``AND``\ 는 생략 될 수 있습니다.
     - 옵션


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   clauses : TIMES
           | TIMES search_condition
           | search_condition

   search_condition : search_condition OR search_condition
                    | search_condition AND search_condition
                    | search_condition search_condition
                    | NOT search_condition
                    | LPAREN search_condition RPAREN
                    | comparison_predicate

   comparison_predicate : scalar_exp EQ scalar_exp
                        | scalar_exp NE scalar_exp
                        | scalar_exp LT scalar_exp
                        | scalar_exp LE scalar_exp
                        | scalar_exp GT scalar_exp
                        | scalar_exp GE scalar_exp
                        | scalar_exp NSEQ scalar_exp
                        | scalar_exp NEQ scalar_exp
                        | scalar_exp IS NULL
                        | scalar_exp IS NOT NULL
                        | scalar_exp LIKE STRING
                        | scalar_exp IN scalar_exp
                        | scalar_exp

   scalar_exp : LPAREN scalar_exp RPAREN
              | atom

   atom : NUMBER
        | TOKEN
        | STRING
        | NUMBER COMMA atom
        | TOKEN COMMA atom
        | STRING COMMA atom

   GT : >
   GE : >=
   LT : <
   LE : <=
   EQ : =
   NE : !=
   NSEQ : <=>
   NEQ : <>
   LPAREN : (
   RPAREN : )
   TIMES : *
   NUMBER : \d+
   COMMA = \,
   STRING : (?:"(?:[^"\\n\\r\\\\]|(?:"")|(?:\\\\x[0-9a-fA-Fㄱ-ㅎ가-힣]+)|(?:\\\\.))*")|(?:\'(?:[^\'\\n\\r\\\\]|(?:\'\')|(?:\\\\x[0-9a-fA-Fㄱ-ㅎ가-힣]+)|(?:\\\\.))*\')
   TOKEN : [a-zA-Z_0-9ㄱ-ㅎ가-힣\.\-\+][a-zA-Z_0-9ㄱ-ㅎ가-힣\.\:]*\*?
