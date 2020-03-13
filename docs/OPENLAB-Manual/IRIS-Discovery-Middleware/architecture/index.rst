
Architecture
============


.. image:: images/details.png
   :target: images/details.png
   :alt: details



* **RESTful**

  * RESTful 방식의 외부 연동 인터페이스. ``http://localhost:6036/search?q=[query string]``
  * query string을 입력 받고 Json 포맷으로 반환한다.

* **Engine**

  * query string을 parsing하고 데이터를 분할로 읽어 들일 수 있도록 planning 후, 실행합니다.
  * **Parser** 

    * query string을 parsing. 각 command를 만들고, arguments 등을 parsing 합니다.
    * query string을 파이프('|') 단위로 토크나이징 하고, command와 query를 분리합니다.

  * **Planner**

    * commands를 실행하기 위해 job을 어떻게 실행 시킬지를 planning. (paging, 데이터 분할 검색)
    * 예를 들어, iris 데이터 소스에 대해 파티션 단위로 Spark에 잡을 요청합니다.

  * **Collector**

    * 결과 DataFrame을 Python Object로 수집하여 반환합니다.

* **Commands**

  * 쿼리 기능이 정의된 명령어들 입니다. 각 명령어에 대한 설명은 Commands 문서를 참조해주세요.
