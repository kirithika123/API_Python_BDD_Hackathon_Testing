Feature: Check the Authorization of the LMS API

Scenario Outline: Check the Authorization with with different set of username & password
    Given Skills User with  username & password from "<sheetName>" and <rowNumber> is on Endpoint: url/Skills
    When skills User sends  a request on GET
    Then skills User validates the StatusCode from "<sheetName>" sheet and <rowNumber> row


    Examples:
      | sheetName            | rowNumber |
      | Skills_Authorization | 0         |
      | Skills_Authorization | 1         |
      | Skills_Authorization | 2         |