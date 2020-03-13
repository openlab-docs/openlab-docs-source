RESTful API Example
====================

개요
---------

- RESTful API 를 코드를 통해서 간단하게 호출 및 결과 확인을 할 수 있는 과정을 설명 해 놓은 문서

코드 예제
----------

Auth API 를 통해 Token 발행
"""""""""""""""""""""""""""""

.. code-block:: none

    #!/usr/bin/env python
    # coding=UTF-8
    import json
    from httplib import HTTPConnection
    import sys

    addr = "192.168.100.180"
    port = 6036

    q = "model name = 'syslog' model_owner = eva start_date = 20191213151300 end_date = 20191213151430"
    size = 10

    user_id = "root"
    user_passwd = '' # TODO: 암호 입력 필요

    # We are going to shutdown this restful server for each test.
    host, port = (addr, 6036)
    parameters = {}
    parameters['q'] = q
    parameters['size'] = size
    parameters['save'] = True

    # get token.
    http_conn = HTTPConnection(host, port)

    http_conn.request(
        "POST",
        "/angora/auth",
        json.dumps({"id": user_id, "password": user_passwd}))
    token = json.load(http_conn.getresponse())["token"]
    http_conn.close()

Query API 를 통해 seesion id 발행 & 결과 도출
"""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: none

    # Query / Fetch Session ID
    headers = {}
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = "Angora %s" % token
    body = json.dumps(parameters)

    http_conn = HTTPConnection(host, port)

    http_conn.request("POST", "/angora/query/jobs", body=body, headers=headers)
    r = json.load(http_conn.getresponse())
    try :
        sid = r["sid"]
    except Exception, e:
        sys.exit()

    http_conn.close()

    # Fetch results
    http_conn = HTTPConnection(host, port)
    http_conn.request(
        "GET",
        "/angora/query/jobs/%s" % sid,
        headers=headers)
    response = json.loads(http_conn.getresponse().read())

    #try:
    #    for data in response['fields']:
    #        print data
    #except:
    #    pass

    for item in response['results']:
        print str(item)

예제 코드 UI를 통해 가져오는 방법
----------------------------------

- IRIS UI 검색 화면에서 Data-Discovery-Service 에 검색 한 내용에 대한 코드를 복사 할 수 있습니다.
- 아래 스크린샷을 참고

.. image:: images/ex1.PNG
   :alt: Open Search window

.. image:: images/ex2.PNG
   :alt: Select Datamodel

.. image:: images/ex3.PNG
   :alt: Get result of query about selected Datamodel

.. image:: images/ex4.PNG
   :alt: Copy source code about query

- 복사한 코드 편집기에 붙여넣기
    - ex) ``$ vi test.py``

- 복사한 코드를 실행하여 결과 확인하기
    - ex) ``$ python test.py``

