.. role:: raw-html-m2r(raw)
   :format: html


anomalies
====================================================================================================

개요
----------------------------------------------------------------------------------------------------

주어진 input 데이터에서 일반적인 범위를 벗어난 비정상적인 값을 찾아내는 기능입니다.

설명
----------------------------------------------------------------------------------------------------

Input 으로 받은 Data 를 대상으로 anomaly 한 값을 찾습니다.
옵션으로 입력한 이상탐지 알고리즘(basic / robust) 을 적용하여 anomal 여부를 알 수 있는 컬럼을 추가하여 Dataframe 형식의 data를  결과로 반환합니다.

옵션으로 명령어 실행 결과에서 anomalies 로  판명된 값만 따로 뽑아내는 것도 가능합니다.

Examples
----------------------------------------------------------------------------------------------------

데이터 샘플 : time,  host, value 컬럼

.. list-table::
   :header-rows: 1

   * - time
     - host
     - value
   * - 2011-11-1
     - h1
     - 5
   * - 2011-11-2
     - h1
     - 10
   * - 2011-11-3
     - h1
     - 15
   * - 2011-11-4
     - h1
     - 20
   * - .
     - .
     - .
   * - .
     - .
     - .
   * - .
     - .
     - .
   * - 2011-11-16
     - h3
     - 95
   * - 2011-11-17
     - h3
     - 300
   * - 2011-11-18
     - h3
     - 105
   * - .
     - .
     - .
   * - .
     - .
     - .
   * - 2011-11-29
     - h3
     - 160
   * - 2011-11-30
     - h3
     - 165


basic 알고리즘을 사용 하는 예

.. code-block:: none

   ... | anomalies time value
   ... | anomalies time value by=host
   ... | anomalies time value alg=basic bound=2 direct=below

 by  가 없을 때

.. list-table::
   :header-rows: 1

   * - time
     - value
     - upper
     - lower
     - anomaly
   * - 2011-11-1
     - 5
     - threshold
     - threshold
     - False
   * - 2011-11-2
     - 10
     - threshold
     - threshold
     - False
   * - 2011-11-3
     - 15
     - threshold
     - threshold
     - False
   * - 2011-11-4
     - 20
     - threshold
     - threshold
     - False
   * - .
     - .
     - .
     - .
     - .


  by  가 있을 때

.. list-table::
   :header-rows: 1

   * - time
     - host
     - value
     - upper
     - lower
     - anomaly
   * - 2011-11-1
     - h1
     - 5
     - threshold
     - threshold
     - False
   * - 2011-11-2
     - h1
     - 10
     - threshold
     - threshold
     - False
   * - 2011-11-3
     - h1
     - 15
     - threshold
     - threshold
     - False
   * - 2011-11-4
     - h1
     - 20
     - threshold
     - threshold
     - False
   * - .
     - .
     - .
     - .
     - .
     - .
   * - 2011-11-17
     - h3
     - 300
     - threshold
     - threshold
     - True
   * - 2011-11-18
     - h3
     - 105
     - threshold
     - threshold
     - False
   * - .
     - .
     - .
     - .
     - .
     - .


robust 알고리즘을 사용 하는 예

.. code-block:: none

   ... | anomalies time value alg=robust

명령어 이후 DataFrame

.. list-table::
   :header-rows: 1

   * - time
     - value
     - residuals
     - upper
     - lower
     - anomaly
   * - 2011-11-1
     - 5
     - NaN
     - threshold
     - threshold
     - False
   * - 2011-11-2
     - 10
     - NaN
     - threshold
     - threshold
     - False
   * - 2011-11-3
     - 15
     - 1.062
     - threshold
     - threshold
     - False
   * - 2011-11-4
     - 20
     - 1.053
     - threshold
     - threshold
     - False
   * - .
     - .
     - .
     - .
     - .
     - .
   * - .
     - .
     - .
     - .
     - .
     - .
   * - .
     - .
     - .
     - .
     - .
     - .
   * - 2011-11-16
     - 95
     - 0.690
     - 1.229
     - 0.567
     - False
   * - 2011-11-17
     - 300
     - 1.716
     - 1.361
     - 0.700
     - True
   * - 2011-11-18
     - 105
     - 0.717
     - 1.333
     - 0.672
     - False
   * - .
     - .
     - .
     - .
     - .
     - .
   * - .
     - .
     - .
     - .
     - .
     - .
   * - 2011-11-29
     - 160
     - NaN
     - threshold
     - threshold
     - False
   * - 2011-11-30
     - 165
     - NaN
     - threshold
     - threshold
     - False


alert_window 옵션으로  수행 했을 때, 설정 기간동안 나온 이상 값 만 반환.

.. code-block:: none

   ... | anomalies time value alg=basic alert_window=last_100s

명령어 결과 Dataframe

.. list-table::
   :header-rows: 1

   * - time
     - value
     - upper
     - lower
     - anomaly
   * - 2011-11-17
     - 300
     - 282.8897323
     - 23.1286923
     - True


.. code-block:: none

   ... | anomalies time value alg=basic direct=below alert_window=last_60s

.. code-block:: none

   - detection 방향이 below 일때, lower 값 보다 낮은 anomaly 값만을 찾고 Last_60s 기준으로  anomaly 한 값이 없으므로  빈 dataframe반환


   명령어 결과  Dataframe

     | time  | value | upper | lower | anomaly |
     | :---: | :---: | :---: | :---: | :-----: |
     | Empty | Empty | Empty | Empty |  Empty  |

Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   anomalies_command : index target params

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - index
     - 시계열 데이터에서 시간 필드명 입니다.
     - 필수
   * - target
     - anomaly 탐지할 대상 데이터 필드명 입니다.
     - 필수
   * - params
     - \*옵션을 지정합니다.
     - 옵션


*옵션

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 기본값
   * - alg
     - *basic,  *\ robust 알고리즘을 선택합니다.  각각 기본통계,  STL decomposition을 수행합니다. :raw-html-m2r:`<br />`\ 예 : alg=robust
     - basic
   * - by
     - 그룹으로 각각의 이상탐지를 시행할 수 있습니다.\ :raw-html-m2r:`<br />`\ 예 : by=fieldA
     - None
   * - bound
     - 임계값 범위의 scale을 지정합니다. 위의 수식에 z값의 배수값으로  bound가 커지면  upper / lower limit 의 범위가 늘어납니다.
     - 2
   * - direct
     - anomaly 한 값을 판정할 때 limit 를 **below** / **above** / **both** 로 선택할 수 있습니다.
     - both
   * - alert_window
     - 이 옵션이 설정되면  설정된 시간동안 발생한 anomaly 값만 return 합니다.  실정된 기간동안 anomaly 한 값이 없으면 빈 값이 반환됩니다.\ :raw-html-m2r:`<br />`\ 최근 시간 범위 내 이상치 값을 탐지합니다.\ :raw-html-m2r:`<br/>`\ 예 : last_60s 이면 최근 60초 이내 데이터 중 이상치를 탐지합니다.\ :raw-html-m2r:`<br/>`\ 예 : last_1m 이면 최근 1분 이내 데이터 중 이상치를 탐지합니다.\ :raw-html-m2r:`<br />`\ 예 : last_1h 이면 최근 1시간 이내 데이터 중 이상치를 탐지합니다.
     - last_60s


``alg`` : **basic**\ ,   **robust** 알고리즘을 선택합니다.  각각 기본통계,  STL decomposition을 수행합니다. 기본값 = **basic**.

*basic : 단순 통계적 방법을 사용하였습니다. 1.959964는 신뢰구간 95% z상수 값입니다. z상수 값으로 upper limit와 lower limit 를 구하여 이상치를 판단합니다.
$$
\bar x \pm \frac{1.959964 \times s}{\sqrt n}
$$

*robust : Seasonal_Decomposition을 사용한 알고리즘입니다. 계절성, 추세, 잔차 값을 구별하여 잔차 값으로 임계값을 구하여 이상치를 판단합니다.

Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   anomalies_command : index target params
   index : WORD
   target : WORD
   params : param
          | params param
          |
   param : WORD EQUALS WORD
          | WORD EQUALS NUMBER
          | WORD EQUALS double
   double : NUMBER DOT NUMBER

   WORD = \w+
   EQUALS = \=
   DOT = \.
   NUMBER = \d+
