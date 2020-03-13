Auth API
=========

개요
-----

- IRIS Discovery Service 의 API 를 사용하기 위해 ID, Password 를 이용하여 토큰을 발행하기 위한 API

Generate token
---------------

URL
"""""

- ``/angora/auth``

Method
"""""""

- ``POST``

Description
""""""""""""

- 토큰을 발급 받는 API

Parameters
"""""""""""

.. list-table::
   :header-rows: 1

    * - Arguments
      - Description
      - Default
    * - id
      - IRIS 계정의 id를 의미합니다.
      - root
    * - Arguments
      - IRIS 계정의 비밀번호를 의미합니다.
      -
    * - group_id
      - 해당 계정의 유져 그룹 아이디를 의미합니다.
      - root

Example
""""""""

- Request

.. code-block:: bash

    curl -XPOST "http://localhost:6036/angora/auth" -H "Content-Type: application/json" -d '{
        "id" : "root",
        "password" : "password",
        "group_id" : "groupA"
    }'

- Success Response

.. code-block:: json

    {
        "status" : "OK",
        "token" : "cm9vdA=="
    }

- Error Response

.. code-block:: json

    {
        "status" : "ERROR",
        "token" : null
    }

- Exception

.. code-block:: json

    {
        "type": "RuntimeError",
        "message": "This was failed because..."
    }

