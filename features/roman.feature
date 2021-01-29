Feature: Convert given arabic numbers to roman

  Scenario Outline: Conversion of arabic numbers to roman
    Given we have <arabic> number and number convertion program
    When we have <roman> number
    Then the program should return correct roman number

    Examples:
      | arabic | roman   |
      |  1     |  I      |
      |  2     |  II     |
      |  3     |  III    |
      |  4     |  IV     |
      |  5     |  V      |
      |  6     |  VI     |
      |  9     |  IX     |
      |  10    |  X      |
      |  20    |  XX     |
      |  49    |  XLIX   |
      |  50    |  L      |
      |  59    |  LIX    |
      |  163   |  CLXIII |
      |  402   |  CDII   |
      |  575   |  DLXXV  |
      |  911   |  CMXI   |
      |  1024  |  MXXIV  |
      |  3000  |  MMM    |
