Feature: To check The DELETE method for Skills
Background:
	Given Skills User is on Endpoint: url/Skills with valid username and password

Scenario Outline: Validate DELETE Skills when user logged with UserName with Password
    When skills User sends DELETE skill id ON DELETE Method from "<SheetName>" and <RowNumber>
    Then skills User validates the StatusCode and the StatusMessage from "<SheetName>" sheet and <RowNumber> row
    And  skills User checks the Database to validate deletion from "<SheetName>" sheet and <RowNumber> row

    Examples:
        | SheetName     | RowNumber |
        | Skills_DELETE | 0         |
        | Skills_DELETE | 1         |
        | Skills_DELETE | 2         |
        | Skills_DELETE | 3         |
        | Skills_DELETE | 4         |
