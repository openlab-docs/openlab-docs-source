
## 디렉토리 구조

### 기본 디렉토리 구조 및 설명
- build       문서를 패키지 하기위한 프로그램
- conf.py     sphinx 기본 환경 파일
- doc         패키지할 매뉴얼이 들어 있는 디렉토리
- lib         패키지시 사용되는 라이브러리

### 생성되는 디렉토리
- t_build     임시 디렉토리 - 빌드 전
- t_source    임시 디렉토리 - 빌드 후
- out         최종 컴파일된 문서 보관


## 지원 문서 종류

rst, md 문서 포맷을 지원 하며, rst 로 작성하는 것을 추천

## 환경 구축 방법

### Python 환경 구축 하기

1. 기본적으로 사용중인 운영체제에 python 3.6이상을 설치 한다.

   - https://www.python.org/downloads/

   설치를 완료한 이후 `python`, `pip` 명령어가 정상적으로 동작하는지 확인한다. 만약 정상적으로 동작하지 않는다면, 환경 변수를 확인해야 한다.

2. `virtualenv` 를 설치한다. 만약 `virtualenv`가 설치되어 있다면 해당 과정을 생략할수 있다.

   ```
   pip install virtualenv
   ```

### git clone 받기

적당한 경로에 `IRIS-Documents` 를 clone 받는다.

```
git clone https://github.com/mobigen/IRIS-Documentation.git
```

### virtualenv 환경 구축하기

clone 받은 IRIS-Documentation 디렉토리 안에서 다음과 같이 명령어를 실행한다.

- for mac & linex

  ```
  $ python -m virtualenv venv
  $ source venv/bin/activate
  (venv) $ pip install -r requirements.txt
  ```

- for windows

  ```
  > python -m virtualenv venv
  > call venv\Scripts\activate
  (venv) > pip install -r requirements.txt
  ```

### 문서 빌드하기

다음과 같이 패키지 작업을 진행함

1. doc 디렉토리에 빌드하기를 원하는 문서를 저장

    현재 git submodule 로 관리중에 있으며, 필요에 따라 추가적인 매뉴얼을 저장

    다음 명령어로 관리중인 최신 메뉴얼 문서를 가져올 수 있음

    - for mac & linux

      ```shell
      (venv) $ ./get_document
      ```

    - for windows

      ```powershell
      (venv) > get_document.bat
      ```

    위와 같이 사용시 `docs` 디렉토리에 다음과 같이 문서가 생성됨

    ```
    IRIS-Data-Discovery-Service_Doc
    IRIS-DB_Doc
    IRIS-WEB_Doc
    SMS_Doc
    ```

2.  문서 빌드 하기

    문서는 다음과 같은 방식으로 빌드를 진행함

    - for mac & linux

      ```shell
      (venv) $ ./build_web ALL
      ```

    - for windows

      ```powershell
      (venv) > build_web.bat
      ```

    위와 같이 빌드를 완료할 경우 최종 결과 파일은 `out` 디렉토리에 파일이 저장됨  

3. 빌드 문서 확인하기

    `out/IRIS/index.html` 을 통해 최종 빌드된 문서를 웹으로 확인할 수 있음


### info.conf

매뉴얼의 정보를 담고 있는 파일입니다.
해당 내용은 다음과 같은 구조로 되어있습니다.

```
[info]
title = IRIS-Doc Documentation
project = IRIS-DB Doc
copyright = 2018, team IRIS-DB
author = team IRIS-DB
version =
release = 0.1


[index]
doc/01.instruction.rst
doc/02.operating_command.rst
doc/03.system_management.rst
doc/04.monitoring.rst
```

`info` section에 대한 항목은 문서의 버전 및 title 등의 항목을 기재 합니다.

`index` section에 대한 항목은 각 문서의 목록을 기재 합니다.


