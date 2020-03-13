.. role:: raw-html-m2r(raw)
   :format: html


forecasts
====================================================================================================

개요
----------------------------------------------------------------------------------------------------

주어진 데이터의 미래 시점 데이터를 예측합니다.

설명
----------------------------------------------------------------------------------------------------

input dataframe의 데이터를 선택한 알고리즘을 이용하여 미래 시점 데이터를 예측합니다. 이 때 예측하는 데이터의 기간은 변경 가능합니다.

예를 들어 데이터가 다음과 같이 존재합니다.

.. list-table::
   :header-rows: 1

   * - **DATETIME_10M**
     - **CNT**
   * - **2018-11-04 05:20:00**
     - 300
   * - **2018-11-04 05:30:00**
     - 301
   * - **2018-11-04 05:40:00**
     - 302
   * - ...
     - ...
   * - **2018-11-04 11:30:00**
     - 900
   * - **2018-11-04 11:40:00**
     - 901
   * - **2018-11-04 11:50:00**
     - 902


forecasts 명령어를 수행하면  기존 dataframe 에 예측 결과를 합쳐서 보여줍니다.

.. list-table::
   :header-rows: 1

   * - **DATETIME_10M**
     - **CNT**
     - Forecasts
   * - **2018-11-04 05:20:00**
     - 300
     - false
   * - **2018-11-04 05:30:00**
     - 301
     - false
   * - **2018-11-04 05:40:00**
     - 302
     - false
   * - ...
     - ...
     - ...
   * - **2018-11-05 05:20:00**
     - 1000
     - true
   * - **2018-11-05 05:30:00**
     - 1001
     - true
   * - **2018-11-05 05:40:00**
     - 1002
     - True


seasonal 알고리즘의 경우 예측 신뢰구간( lower  / upper ) 도 함께 반환됩니다.

.. list-table::
   :header-rows: 1

   * - **DATETIME_10M**
     - **CNT**
     - **lower CNT**
     - **upper CNT**
     - Forecasts
   * - **2018-11-04 05:20:00**
     - 300
     - 0.0
     - 0.0
     - false
   * - **2018-11-04 05:30:00**
     - 301
     - 0.0
     - 0.0
     - false
   * - **2018-11-04 05:40:00**
     - 302
     - 0.0
     - 0.0
     - false
   * - ...
     - ...
     - ...
     - ...
     - ...
   * - **2018-11-05 05:40:00**
     - 1000.02
     - 989.11
     - 1021.22
     - true


Example
----------------------------------------------------------------------------------------------------


* syslog 모델의 Host의 값이 ``tsdn-svr1``\ 인 레코드를 검색하여, 10분단위 레코드 개수를 선형회귀방법으로 예측한다.

.. code-block:: none

   # 모델 : syslog
   HOST='tsdn-svr1' | sql "select CONCAT(SUBSTR(DATETIME,1,11),'000') as DATETIME_10M, * from angora" | stats COUNT(*) as CNT by DATETIME_10M, HOST | forecasts DATETIME_10M CNT alg=linear


* syslog 모델의 Host의 값이 ``tsdn-svr1``\ 인 레코드를 검색하여, 10분단위 레코드 개수를 ARIMA모델로 예측한다.

.. code-block:: none

   HOST='tsdn-svr1' | sql "select CONCAT(SUBSTR(DATETIME,1,11),'000') as DATETIME_10M, * from angora" | stats COUNT(*) as CNT by DATETIME_10M, HOST | forecasts DATETIME_10M CNT alg=seasonal

**현재 시계열 컬럼의 시간 간격의 정도가 고려되지 않기 때문에, 소스데이터를 일정한 시간간격으로 그룹핑하여  전처리 한다.**

Parameters
----------------------------------------------------------------------------------------------------

Alg = linear
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

   ... | forecasts index target [alg=linear] [f_coeff=0]

linear regression 으로 예측을 수행 합니다.

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - index
     - 시계열 데이터의 time  필드 입니다.
     - 필수
   * - target
     - 예측하고자 하는 target 필드 입니다.
     - 필수
   * - alg
     - 시계열 데이터 예측에 사용되는 알고리즘. default 로  linear 알고리즘.
     - 옵션
   * - f_coeff
     - 예측값이 계산되어 결과로 나오는 기간을 구하는 데 사용되는 계수.  default = 0 으로 입력 데이터의 기간의 1/2 를 예측합니다. :raw-html-m2r:`<br />`\ 원하는 기간이 있다면 단위 기간의 개수를 입력합니다.\ :raw-html-m2r:`<br />`\ 예) f_coeff = 12 이고,  입력데이터 시간 단위가 1분이면  입력값의 시간 이후  +12분의 시간을 예측합니다.
     - 옵션


Alg = seasonal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

   ... | forecasts index target alg=seasonal [f_coeff=10] [deviation=1]

계절성과 시간적 변화에 따라 예측을 수행 합니다. 내부적으로  ARIMA 알고리즘이 적용되며, AIC 를 최소화 하는 order 를 구해서 모델링합니다.

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - index
     - 시계열 데이터의 time  필드 입니다.
     - 필수
   * - target
     - 예측하고자 하는 target 필드 입니다.
     - 필수
   * - alg
     - 시계열 데이터 예측에 사용되는 알고리즘. default 로  linear 알고리즘.
     - 옵션
   * - f_coeff
     - 예측값이 계산되어 결과로 나오는 기간을 구하는 데 사용되는 계수.  default = 0 으로 입력 데이터의 기간의 1/2 를 예측합니다. :raw-html-m2r:`<br />`\ 원하는 기간이 있다면 단위 기간의 개수를 입력합니다.\ :raw-html-m2r:`<br />`\ 예) f_coeff = 12 이고,  입력데이터 시간 단위가 1분이면  입력값의 시간 이후  +12분의 시간을 예측합니다.
     - 옵션
   * - deviation
     - 예측된 값의 신뢰구간의 범위 계수입니다.
     - 옵션


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   forecasts_command : index target params
   index : WORD
   target : WORD
   params : param
          | params param
   param : WORD EQUALS WORD
         | WORD EQUALS NUMBER
         | WORD EQUALS double
   double : NUMBER DOT NUMBER

   NUMBER : d+
   WORD : w+
   EQUALS : =
   DOT : .
