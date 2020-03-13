
iris
====================================================================================================

개요
----------------------------------------------------------------------------------------------------

IRIS에 읽기를 하는 명령어 입니다.

설명
----------------------------------------------------------------------------------------------------

해당 명령어를 통해 IRIS의 데이터를 읽어 들일 수 있습니다.

**해당 명령어는 내부 구현 목적으로 주로 사용됩니다.**

**IRIS에 쓰는 명령은 현재 지원되고 있지 않습니다.**

Examples
----------------------------------------------------------------------------------------------------

 ``EVA .BMI`` 테이블을 읽는 예제입니다.

.. code-block:: none

   * | iris READ EVA.BMI connector_id=2 | search *

``EVA .SYSLOG`` 테이블에서 파티션이 ``20191025140000`` ~ ``20191029150000`` 사이의 데이터를 읽는 예제입니다.

.. code-block:: none

   * | iris READ EVA.SYSLOG connector_id=2 "(PARTITION >= '20191025140000' AND PARTITION < '20191029150000')" | search *

Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   ... | iris ([WRITE|READ])? TABLE CONNECTOR_ID HINT

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - ([WRITE, READ])?
     - ``WRITE`` 와 ``READ``\ 는 키워드 이며, 읽을 것인지 쓸 것인지를 나타냅니다.
     - 필수
   * - TABLE
     - 테이블 이름을 의미합니다.
     - 필수
   * - CONNECTOR_ID
     - 연결 정보 식별자를 의미합니다.
     - 필수
   * - HINT
     - IRIS에서 partition 검색 시 사용되는 힌트 절을 의미합니다.
     - 옵션


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   clauses : TOKEN options
           | READ TOKEN options
           | WRITE TOKEN options

   options : option
           | options option

   option : CONNECTOR_ID EQ NUMBER
          | SAMPLING_RATE EQ FLOAT
          | SAMPLING_RATE EQ NUMBER
          | USE_SAMPLING_TABLE
          | PARTITION
          | location
          | SPACE

   location : TOKEN
            | location TOKEN

   CONNECTOR_ID = (?i)connector_id
   USE_SAMPLING_TABLE = (?i)use_sampling_table
   SAMPLING_RATE = (?i)sampling_rate
   EQ = =
   SPACE = ST[\w()\'= ,.-]*
   FLOAT = \d+\.\d+
   NUMBER = \d+
   PARTITION = (?:"(?:[^"\\n\\r\\\\]|(?:"")|(?:\\\\x[0-9a-fA-F]+)|(?:\\\\.))*")|(?:\'(?:[^\'\\n\\r\\\\]|(?:\'\')|(?:\\\\x[0-9a-fA-F]+)|(?:\\\\.))*\')
   TOKEN = [^ |^\|]+
