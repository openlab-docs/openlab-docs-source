Query API
=========

개요
-----

- IRIS Discovery Service 에 검색 명령어를 통해 분석 결과를 도출 하는 API

Fetch SID
----------

URL
"""""

- ``/angora/query/jobs``

Method
"""""""

- ``POST``

Description
""""""""""""

- 처음 검색을 하기 위해서 session ID가 필요합니다. 이를 가져오는 API 입니다. 질의에 필요한 각종 parameters 를 함께 넘겨 주어야 합니다.

Parameters
"""""""""""

.. list-table::
   :header-rows: 1

    * - Parameters
      - Description
      - Default
    * - q
      - [`Command References <../../../command_guide/doc/commands.rst`_]에 정의되어있는 명령어로 구성된 쿼리를 말합니다.
      - null
    * - size
      - 결과의 Row 갯수를 의미합니다. `null`으로 지정 되면 모든 Row 를 가져옵니다.
      - 500
    * - fetch_size
      - 얻어 오고자 하는 데이터의 크기를 fetch_size로 지정한다. (size 단위 500)
      - 1
    * - dataset
      - 결과를 export 할 시, 해당 인자를 참고하여 결과를 export 합니다.
      - null
    * - sample
      - sample 데이터만 조회하여 전체 검색보다 빠른 결과를 도출 합니다.
      - false
    * - schema
      - 데이터의 schema 정보를 도출합니다.
      - false

fetch_size
''''''''''''

- 예제
    1. size = 500, fetch_size = 1 -> 500 * 1 = 500 개의 데이터 반환
    2. size = 500, fetch_size = 10 -> 500 * 10 = 5000 개의 데이터 반환

dataset Parameters
'''''''''''''''''''

.. list-table::
   :header-rows: 1

    * - Parameters
      - Description
      - Default
    * - format
      - csv / iris
      - csv/iris
    * - path
      - ``format`` 이 ``csv``인 경우, 설정해 주어야 합니다. HDFS path가 추천됩니다.
      - csv 시 생략 불가
    * - table
      - ``format`` 이 ``iris``인 경우, 설정해 주어야 합니다.
      - iris 시 생략 불가
    * - option
      - 해당 필드에 필요한 옵션 값을 받습니다. 어떤 값이든 올 수 있습니다.
      - null

option
''''''''

.. list-table::
   :header-rows: 1

    * - Parameters
      - Description
      - Default
    * - sep
      - CSV 전용 옵션 입니다. 컬럼을 분할하는 구분자를 의미합니다.
      - ,
    * - inferSchema
      - CSV 전용 옵션 입니다. 컬럼의 스키마를 데이터로부터 유추합니다. 데이터가 많은 경우 속도저하가 발생합니다.
      - false
    * - ignoreLeadingWhiteSpace
      - CSV 전용 옵션 입니다. 데이터의 선두에 공백이 있는 경우 무시합니다.
      - true
    * - ignoreTrailingWhiteSpace
      - CSV 전용 옵션 입니다. 데이터의 후미에 공백이 있는 경우 무시합니다.
      - true


Example
""""""""

- Request

.. code-block:: bash

    curl -XPOST "http://localhost:6036/angora/query/jobs"
        -H "Authorization: Angora bXktb3JnLW5hbWU6MTIza2V5NGFwaQ=="
        -H "Content-Type: application/json"
        -d '{
            "q" : "model name = syslog start_date = 20191104130300 end_date = 20191104130400 | stats count(*) by datetime",
            "size" : 500,
            "fetch_size" : 10
        }'

- Response

.. code-block:: json

    {
        "sid" : 1461649586.1695
    }

- Exception

.. code-block:: json

    {
        "type": "RuntimeError",
        "message": "This was failed because..."
    }


Fetch Results
--------------

URL
"""""

- ``/angora/query/jobs/[sid]``

Method
"""""""

- ``GET``

Description
""""""""""""

- 질의한 결과를 가져옵니다.

Example
""""""""

- Request

.. code-block:: bash

    curl -XGET "http://localhost:6036/angora/query/jobs/1461649586.1695"
        -H "Authorization: Angora bXktb3JnLW5hbWU6MTIza2V5NGFwaQ=="

- Response

.. code-block:: json

    {
        "status": {
            "current" : 0,
            "total" : 5000
        },
        "isEnd" : true,
        "fields": [
            {
                "name": "DATETIME",
                "type": "string"
            },
            {
                "name": "count(*)",
                "type": "number"
            }
        ],
        "results": [
            ["20180827170300", 5],
            ["20180827171405", 19]
            ...
        ]
    }

- Exception

.. code-block:: json

    {
        "type": "RuntimeError",
        "message": "This was failed because..."
    }


Downloads Results
-------------------

URL
"""""

- ``/angora/query/jobs/[sid]/download?type=[csv|json]&sep=,&file_name=test``

Method
"""""""

- ``GET``

Description
""""""""""""

- 질의한 결과를 streaming으로 해당 ``type`` 형태에 맞게 반환합니다.
- ``type`` 은 ``csv``/``tsv``/``json`` 을 지원합니다. ``sep`` 은 ``csv`` 의 경우, 필드 구분자(``,`` , ``|`` 등)를 의미합니다.

Example
""""""""

- Request (json)

.. code-block:: bash

    curl -XGET "http://localhost:6036/angora/query/jobs/1461649586.1695/download?type=json"
        -H "Authorization: Angora bXktb3JnLW5hbWU6MTIza2V5NGFwaQ=="

- Response (json)

.. code-block:: json

    {
        "fields": [
            {
                "name": "fieldA",
                "type": "string"
            },
            {
                "name": "fieldB",
                "type": "number"
            }
        ],
        "results": [
            {"fieldA" : "a", "fieldB": 1},
            {"fieldA" : "c", "fieldB": 3}
        ]
    }

- Request (csv)

.. code-block:: bash

    curl -XGET "http://localhost:6036/angora/query/jobs/1461649586.1695/download?type=csv"
        -H "Authorization: Angora bXktb3JnLW5hbWU6MTIza2V5NGFwaQ=="

- Response (csv)

.. code-block:: csv

    fieldA,fieldB
    a,2
    c,3

- Exception

.. code-block:: json

    {
        "type": "RuntimeError",
        "message": "This was failed because..."
    }


Export Results
----------------

URL
"""""

- ``/angora/query/jobs/[sid]/export``

Method
"""""""

- ``GET``

Description
""""""""""""

- 질의한 결과를 시초에 POST에 셋업되있는 arguments 형태에 맞게 저장합니다.

Example
""""""""

- Request

.. code-block:: bash

    curl -XGET "http://localhost:6036/angora/query/jobs/1461649586.1695/export"
        -H "Authorization: Angora bXktb3JnLW5hbWU6MTIza2V5NGFwaQ=="

- Response

.. code-block:: json

    {
        "message" : "OK"
    }

- Exception

.. code-block:: json

    {
        "type": "RuntimeError",
        "message": "This was failed because..."
    }


Abort (Close Jobs)
-------------------

URL
"""""

- ``/angora/query/jobs/[sid]/close``

Method
"""""""

- ``DELETE``

Description
""""""""""""

- 검색 중인 session을 종료 합니다.
- 일정 시간이 지날동안 해당 session의 응답이 없으면 자동으로 종료되나, 종료가 예상되는 경우에는 직접 종료해주어야 합니다.

Example
""""""""

- Request

.. code-block:: bash

    curl -XDELETE "http://localhost:6036/angora/query/jobs/1461649586.1695/close"
        -H "Authorization: Angora bXktb3JnLW5hbWU6MTIza2V5NGFwaQ=="

- Response

.. code-block:: json

    {
        "sid": 1461649586.1695
    }

- Exception

.. code-block:: json

    {
        "type": "RuntimeError",
        "message": "This was failed because..."
    }



