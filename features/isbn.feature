Feature: Check if given number is correct ISBN-13 control number


  Scenario Outline: Given number is of a wrong length
    Given number is in <number>
    When the length of number is not 13
    Then the program should return <wrong_length_error>

    Examples:
      |  number              |  wrong_length_error                  |
      |  273-385-2841-1      |  Length of given number should be 13 |
      |  275-2841-1          |  Length of given number should be 13 |
      |  273-41-1            |  Length of given number should be 13 |
      |  2-1                 |  Length of given number should be 13 |
      |  273-385-2841-1284-2 |  Length of given number should be 13 |


  Scenario Outline: Given number is of a wrong type
    Given number is in <number>
    When the types of all number's digits are not integers
    Then the program should return <wrong_type_error>

    Examples:
      | number               |  wrong_type_error                      |
      | 2598-2385-33abc      | Number should consist of integers only |
      | 2598-3ab-c52-3te            | Number should consist of integers only |
      | 2598-2te-st85-33   | Number should consist of integers only |
      | a-bc-de-ff-jk-naut             | Number should consist of integers only |
      | qw-erty-uiop-asd     | Number should consist of integers only |

  Scenario Outline: Check if number is correct
    Given number is in <number>
    When using isbn function
    Then result should be <result>

    Examples:
      |  number             |  result  |
      |  854-3872-3-380-21  |  True    |
      |  3-15298-982-8947   |  False   |
      |  3235-29-2389-077   |  True    |
      |  14-28-77-2836-723  |  True    |
      |  73-954-5629-54-61  |  False   |