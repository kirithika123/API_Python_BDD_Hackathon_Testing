Feature: To check The GET method for Skills
Background:
   Given Skills User is on Endpoint: url/Skills with valid username and password

Scenario:

    When skills User sends GET request
    Then skills User validates StatusCode
    And skills JSON schema is valid

Scenario Outline: Verify GET for a Skill with specific ID

    When User sends GET request on skill id from "<SheetName>" and <RowNumber>
    Then skills User validates the StatusCode and StatusMessage from "<SheetName>" sheet and <RowNumber> row
    And JSON schema is valid for GET with id in Skills
    And skills check the Database with Skill id from "<SheetName>" and <RowNumber>

    Examples:
      | SheetName  | RowNumber |
      | Skills_GET | 0         |
      | Skills_GET | 1         |
      | Skills_GET | 2         |
      | Skills_GET | 3         |
      | Skills_GET | 4         |
      | Skills_GET | 5         |
