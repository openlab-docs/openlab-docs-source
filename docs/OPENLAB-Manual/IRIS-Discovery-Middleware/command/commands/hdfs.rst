.. role:: raw-html-m2r(raw)
   :format: html


hdfs
====================================================================================================

개요
----------------------------------------------------------------------------------------------------

HDFS에 읽기 및 쓰기를 하는 명령어 입니다.

설명
----------------------------------------------------------------------------------------------------

해당 명령어를 통해 HDFS 혹은 local로 데이터를 읽기 및 쓰기를 할 수 있습니다.

**해당 명령어는 내부 구현 목적으로 주로 사용됩니다. Query string에서는 join 명령어에서 데이터를 읽어 들여 올 때를 제외하고는 읽기 명령은 사용 될 수 없습니다.**

Examples
----------------------------------------------------------------------------------------------------


* 아래 예제는 앞서 처리된 값을 ``/tmp/path`` 라는 local path로 write하는 예제 입니다..

.. code-block:: none

   ... | hdfs csv write /tmp/path option(connector_id '3')


* ``/tmp/path/test.csv`` 를 read 하는 예제입니다.

.. code-block:: none

   ... | hdfs csv read /tmp/path/test.csv option(connector_id '3')

Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   ... | hdfs SOURCE [WRITE|READ] (OPTIONS '(' ((KEY VALUE) (,KEY VALUE)*)? ')')?

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - ``SOURCE``
     - 데이터의 타입을 나타내며, ``csv``\ , ``json``\ , ``parquet`` 와 ``text``\ 등이 될 수 있습니다.
     - 필수
   * - `(WRITE
     - READ)`
     - ``WRITE`` 와 ``READ``\ 는 키워드 이며, 읽을 것인지 쓸 것인지를 나타냅니다.
     - 필수
   * - ``(OPTIONS '(' ((KEY VALUE) (,KEY VALUE)*)? ')')?``
     - ``OPTIONS``\ 는 키워드 이며, ``KEY``\ 와 ``VALUE``\ 는 그에 해당하는 옵션이 될 수 있습니다. 해당 옵션들은 Spark의 read 및 write 옵션과 동일합니다. 또한, ``outputNum`` 옵션으로 output의 file 갯수를 조절 할 수 있습니다.\ :raw-html-m2r:`<br/>`\ **option 중 connector_id 는 필수로 작성을 해야합니다.**
     - 옵션


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   clauses : TOKEN READ STRING_TOKEN
           | TOKEN WRITE STRING_TOKEN
           | TOKEN READ TOKEN
           | TOKEN WRITE TOKEN
           | TOKEN READ STRING_TOKEN OPTION LPAREN RPAREN
           | TOKEN WRITE STRING_TOKEN OPTION LPAREN RPAREN
           | TOKEN READ TOKEN OPTION LPAREN RPAREN
           | TOKEN WRITE TOKEN OPTION LPAREN RPAREN

   clauses_options : TOKEN READ STRING_TOKEN OPTION LPAREN tokens RPAREN
           | TOKEN WRITE STRING_TOKEN OPTION LPAREN tokens RPAREN
           | TOKEN READ TOKEN OPTION LPAREN tokens RPAREN
           | TOKEN WRITE TOKEN OPTION LPAREN tokens RPAREN
   tokens : TOKEN TOKEN
           | TOKEN STRING_TOKEN
           | tokens COMMA TOKEN TOKEN
           | tokens COMMA TOKEN STRING_TOKEN

   STRING_TOKEN = "..."
   LPAREN = (
   RPAREN = )
   COMMA = ,
