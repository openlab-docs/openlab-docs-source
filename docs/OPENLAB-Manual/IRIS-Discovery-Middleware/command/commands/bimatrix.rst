.. role:: raw-html-m2r(raw)
   :format: html


bimatrix
====================================================================================================

개요
----------------------------------------------------------------------------------------------------

bimatrix에 쓰기를 하는 명령어 입니다.

설명
----------------------------------------------------------------------------------------------------

해당 명령어를 통해 bimatrix의 데이터를 쓸 수 있습니다.

**해당 명령어는 내부 구현 목적으로 주로 사용됩니다.**

Examples
----------------------------------------------------------------------------------------------------

앞에서 처리된 데이터를, ``BATTING``\ 이라는 이름의 테이블로 bimatrix에 load 하는 예제 입니다.

.. code-block:: none

     ... | bimatrix LOAD BATTING

Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   ... | bimatrix LOAD TABLE (OPTIONS '(' ((KEY VALUE) (,KEY VALUE)*)? ')')?

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - LOAD
     - ``LOAD`` 는 예약어 입니다.
     - 필수
   * - TABLE
     - 테이블 이름을 의미합니다.
     - 필수
   * - (OPTIONS '(' ((KEY VALUE) (,KEY VALUE)*)? ')')?
     - ``OPTIONS``\ 는 키워드 이며, ``KEY``\ 와 ``VALUE``\ 는 그에 해당하는 옵션이 될 수 있습니다. :raw-html-m2r:`<br />`\ 해당 옵션들은 Spark의 read 및 write 옵션과 동일합니다. :raw-html-m2r:`<br />`\ 또한, ``outputNum`` 옵션으로 output의 file 갯수를 조절 할 수 있습니다.
     - 옵션


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   clauses : LOAD STRING_TOKEN
           | LOAD TOKEN
           | LOAD STRING_TOKEN OPTION LPAREN RPAREN
           | LOAD TOKEN OPTION LPAREN RPAREN
           | LOAD STRING_TOKEN OPTION LPAREN tokens RPAREN
           | LOAD TOKEN OPTION LPAREN tokens RPAREN

   tokens : TOKEN TOKEN
          | TOKEN STRING_TOKEN
          | tokens COMMA TOKEN TOKEN
          | tokens COMMA TOKEN STRING_TOKEN

   STRING_TOKEN = (?:"(?:[^"\\n\\r\\\\]|(?:"")|(?:\\\\x[0-9a-fA-F]+)|(?:\\\\.))*")|(?:\'(?:[^\'\\n\\r\\\\]|(?:\'\')|(?:\\\\x[0-9a-fA-F]+)|(?:\\\\.))*\')
   TOKEN = [^ |^\|^(|^|^,)]+
