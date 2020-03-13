.. role:: raw-html-m2r(raw)
   :format: html


tokenizer
====================================================================================================

개요
----------------------------------------------------------------------------------------------------

지정한 필드에 대해 tokenizer를 진행하는 명령어 입니다.

설명
----------------------------------------------------------------------------------------------------

input으로 받은 DataFrame과 tokenize할 field명을 입력받습니다.  선택한 필드를 tokenizer를 이용해 원하는 단위로 잘라 그 결과값을 새로운 필드를 추가해 출력합니다.

Examples
----------------------------------------------------------------------------------------------------

데이터가 다음과 같이 존재합니다.

.. list-table::
   :header-rows: 1

   * - id
     - Sentence
   * - 0
     - Hi I heard about Spark
   * - 1
     - I wish Java could use case classes
   * - 2
     - Logistic,regression,models,are,neat


Sentence 필드값을 이용해 word단위로 쪼개 테이블에 추가하는 예

.. code-block:: none

   ... | tokenizer Sentence to words

명령어 이후 테이블

.. list-table::
   :header-rows: 1

   * - id
     - Sentence
     - words
   * - 0
     - Hi I heard about Spark
     - [Hi, I , heard , about , Spark]
   * - 1
     - I wish Java could use case classes
     - [I , wish , Jave , could , use , classes]
   * - 2
     - Logistic,regression,models,are,neat
     - [Logistic , regression , models , are , neat]


Parameters
----------------------------------------------------------------------------------------------------

.. code-block:: none

   ... | tokenizer fields (pattern)

.. list-table::
   :header-rows: 1

   * - 이름
     - 설명
     - 필수/옵션
   * - fields
     - tokenizer를 사용할 필드명 입니다.\ :raw-html-m2r:`<br />`\ input_col to output_col 또는 input_col 으로 이루어져 있습니다.\ :raw-html-m2r:`<br />`\ 예 :
     - 필수
   * - pattern
     - tokenize를 할 때 사용할 단위에 대한 정보입니다. :raw-html-m2r:`<br />`\ Default는 공백단위로 tokenize를 진행하고, option을 설정해 공백 이외에 추가적으로 tokenize를 진행합니다.\ :raw-html-m2r:`<br />`\ **현재 미개발 상태입니다.**
     - 옵션


Parameters BNF
----------------------------------------------------------------------------------------------------

.. code-block:: none

   tokenizer_command : fields pattern

   fields : field
          | fields COMMA field

   field : WORD TO WORD
         | WORD

   pattern : WORD EQUALS QUOTE COMMA QUOTE
           | WORD EQUALS QUOTE WORD QUOTE
           | WORD EQUALS QUOTE DOT QUOTE
           |

   WORD = \w+
   QUOTE = \'
   EQUALS = \=
   COMMA = \,
   DOT = \.

개발사항
----------------------------------------------------------------------------------------------------


* field를 1개가 아니라 여러개를 입력할 수 있는지 -> 구현 완료
* pattern 을 잘못 이해하고 있었음 -> 추가 개발 사항

  * pattern = ',' -> , 단위로 토큰을 자른다
  * pattern = '\w+' -> word 단위로 토큰을 자른다
  * 정규표현식 입력해야함
  * 그냥 Tokenizer() 에는 pattern 파라미터가 없음
  * RegExTokenizer() 안에 pattern 포함
  * 우선 pattern 고려 안하고 Tokenizer만 사용
