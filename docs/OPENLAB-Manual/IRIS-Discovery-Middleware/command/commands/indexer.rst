
indexer
====================================================================================================

indexer 명령어 문법 및 연동규격 설명서 입니다.

개요
----------------------------------------------------------------------------------------------------

설정한 컬럼의 데이터를 기반으로 indexing하는 명령어 입니다. **컬럼의 데이터가 다를 경우 같은 값이라도 index 결과가 다를 수 있습니다.**

설명
----------------------------------------------------------------------------------------------------

input으로 받은 DataFrame과 파라미터로 머신 러닝에서 label 역할을 하는 field명을 입력받습니다. string 형식으로 되어 있는 label field를 변환해 숫자 형식의 label을 생성합니다.

Examples
----------------------------------------------------------------------------------------------------


* 입력데이터

.. list-table::
   :header-rows: 1

   * - a
     - b
     - c
     - d
     - species
   * - 5.1
     - 3.5
     - 4.0
     - 0.2
     - Iris-setosa
   * - 6.3
     - 3.7
     - 4.9
     - 0.1
     - Iris-setosa
   * - 7.8
     - 2.0
     - 3.5
     - 0.3
     - Iris-versicolor
   * - 6.1
     - 3.1
     - 3.8
     - 0.2
     - Iris-virginica


species(label) 필드를 stringindexer()를 사용한 예
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

fit_transform
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


* 명령어

.. code-block:: none

   ... | indexer fit_transform iris_species_indexing species to s


* 
  파일 저장


  * iris_species_indexing.dat 파일을 HDFS 서버에 저장 

* 
  변형 후 데이터

.. list-table::
   :header-rows: 1

   * - a
     - b
     - c
     - d
     - species
     - s
   * - 5.1
     - 3.5
     - 4.0
     - 0.2
     - Iris-setosa
     - 0.0
   * - 6.3
     - 3.7
     - 4.9
     - 0.1
     - Iris-setosa
     - 0.0
   * - 7.8
     - 2.0
     - 3.5
     - 0.3
     - Iris-versicolor
     - 1.0
   * - 6.1
     - 3.1
     - 3.8
     - 0.2
     - Iris-virginica
     - 2.0


fit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


* 명령어

.. code-block:: none

   ... | indexer fit iris_species_indexing species to s


* 
  파일 저장


  * iris_species_indexing.dat 파일을 HDFS 서버에 저장 

* 
  데이터의 변경은 없음

transform
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


* 명령어

.. code-block:: none

   ... | indexer transform iris_species_indexing species to s


* 
  파일 읽기


  * HDFS 의 iris_species_indexing.dat 파일을 읽어 데이터 변경

* 
  데이터 변경 후 결과

.. list-table::
   :header-rows: 1

   * - a
     - b
     - c
     - d
     - species
     - s
   * - 5.1
     - 3.5
     - 4.0
     - 0.2
     - Iris-setosa
     - 0.0
   * - 6.3
     - 3.7
     - 4.9
     - 0.1
     - Iris-setosa
     - 0.0
   * - 7.8
     - 2.0
     - 3.5
     - 0.3
     - Iris-versicolor
     - 1.0
   * - 6.1
     - 3.1
     - 3.8
     - 0.2
     - Iris-virginica
     - 2.0


invert
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


* 입력데이터

.. list-table::
   :header-rows: 1

   * - a
     - b
     - c
     - d
     - s
   * - 5.1
     - 3.5
     - 4.0
     - 0.2
     - 0.0
   * - 6.3
     - 3.7
     - 4.9
     - 0.1
     - 0.0
   * - 7.8
     - 2.0
     - 3.5
     - 0.3
     - 1.0
   * - 6.1
     - 3.1
     - 3.8
     - 0.2
     - 2.0



* 명령어

.. code-block:: none

   ... | indexer invert iris_species_indexing s to species_new


* 
  파일 읽기


  * HDFS 의 iris_species_indexing.dat 파일을 읽어 데이터 변경

* 
  데이터 변경 후 결과

.. list-table::
   :header-rows: 1

   * - a
     - b
     - c
     - d
     - s
     - species_new
   * - 5.1
     - 3.5
     - 4.0
     - 0.2
     - 0.0
     - Iris-setosa
   * - 6.3
     - 3.7
     - 4.9
     - 0.1
     - 0.0
     - Iris-setosa
   * - 7.8
     - 2.0
     - 3.5
     - 0.3
     - 1.0
     - Iris-versicolor
   * - 6.1
     - 3.1
     - 3.8
     - 0.2
     - 2.0
     - Iris-virginica


species(label) 필드를 indexer를 사용해 직접 변환한 예
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

fit_transform
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


* 명령어

.. code-block:: none

   ... | indexer fit_transform iris_species_indexing species


* 
  파일 저장


  * iris_species_indexing.dat 파일을 HDFS 서버에 저장 

* 
  변형 후 데이터

.. list-table::
   :header-rows: 1

   * - a
     - b
     - c
     - d
     - species
   * - 5.1
     - 3.5
     - 4.0
     - 0.2
     - 0.0
   * - 6.3
     - 3.7
     - 4.9
     - 0.1
     - 0.0
   * - 7.8
     - 2.0
     - 3.5
     - 0.3
     - 1.0
   * - 6.1
     - 3.1
     - 3.8
     - 0.2
     - 2.0


fit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


* 명령어

.. code-block:: none

   ... | indexer fit iris_species_indexing species


* 
  파일 저장


  * iris_species_indexing.dat 파일을 HDFS 서버에 저장 

* 
  데이터의 변경은 없음

transform
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


* 명령어

.. code-block:: none

   ... | indexer transform iris_species_indexing species


* 
  파일 읽기


  * HDFS 의 iris_species_indexing.dat 파일을 읽어 데이터 변경

* 
  데이터 변경 후 결과

.. list-table::
   :header-rows: 1

   * - a
     - b
     - c
     - d
     - species
   * - 5.1
     - 3.5
     - 4.0
     - 0.2
     - 0.0
   * - 6.3
     - 3.7
     - 4.9
     - 0.1
     - 0.0
   * - 7.8
     - 2.0
     - 3.5
     - 0.3
     - 1.0
   * - 6.1
     - 3.1
     - 3.8
     - 0.2
     - 2.0


invert
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


* 입력데이터

.. list-table::
   :header-rows: 1

   * - a
     - b
     - c
     - d
     - s
   * - 5.1
     - 3.5
     - 4.0
     - 0.2
     - 0.0
   * - 6.3
     - 3.7
     - 4.9
     - 0.1
     - 0.0
   * - 7.8
     - 2.0
     - 3.5
     - 0.3
     - 1.0
   * - 6.1
     - 3.1
     - 3.8
     - 0.2
     - 2.0



* 명령어

.. code-block:: none

   ... | indexer invert iris_species_indexing s


* 
  파일 읽기


  * HDFS 의 iris_species_indexing.dat 파일을 읽어 데이터 변경

* 
  데이터 변경 후 결과

.. list-table::
   :header-rows: 1

   * - a
     - b
     - c
     - d
     - s
   * - 5.1
     - 3.5
     - 4.0
     - 0.2
     - Iris-setosa
   * - 6.3
     - 3.7
     - 4.9
     - 0.1
     - Iris-setosa
   * - 7.8
     - 2.0
     - 3.5
     - 0.3
     - Iris-versicolor
   * - 6.1
     - 3.1
     - 3.8
     - 0.2
     - Iris-virginica


Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   ...| indexer (FIT_TRANSFORM | FIT | TRANSFORM | INVERT) index_metadata in_field to out_field(, in_field to out_field)*

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - ``FIT_TRANSFORM``
     - 선택한 컬럼의 데이터를 indexing 한 후, 결과를 **1.파일에 저장하고** **2.string 데이터를 숫자로 변환** 합니다.
     - 필수
   * - ``FIT``
     - 선택한 컬럼의 데이터를 indexing 한 후, 결과를 파일에 저장합니다.
     - 필수
   * - ``TRANSFORM``
     - 저장된 indexing 파일을 읽어와 string 데이터를 숫자로 변환합니다.
     - 필수
   * - ``INVERT``
     - 변환한 indexing 을 저장된 indexing 파일을 통해 원래 string 데이터로 변환합니다.
     - 필수
   * - ``index_metadata``
     - 인덱싱 매핑 정보를 저장하거나, 읽어올 파일이름 입니다.
     - 필수
   * - ``in_field to out_field``
     - ``in_field to out_field`` 으로 이루어져 있습니다. ``out_field``\ 을 적지 않을 경우 ``in_field``\ 을 직접 변환시킵니다.
     - 필수


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   indexer_command : FIT_TRANSFORM index_metadata fields
                   | FIT index_metadata fields
                   | TRANSFORM index_metadata fields
                   | INVERT index_metadata fields

   index_metadata : WORD

   fields : field
           | fields COMMA field

   field : WORD TO WORD

추가 개발사항
----------------------------------------------------------------------------------------------------


#. 현재는 고정된 경로에 지정한 이름으로 저장하지만, 추후 유저마다 저장 할 수 있도록 변경할 것.
