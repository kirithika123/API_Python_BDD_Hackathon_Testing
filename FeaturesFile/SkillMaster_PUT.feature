Feature: To check The PUT method for Skills
Background:
	Given Skills User is on Endpoint: url/Skills with valid username and password


Scenario Outline: Verify PUT for a Skill when user logged with UserName with Password
    When skills User sends PUT request on id and request body in skills from "<SheetName>" and <RowNumber> with valid JSON Schema
    Then skills User validates the StatusCode and StatusMessage from "<SheetName>" sheet and <RowNumber> row
    And JSON schema is valid for POST/PUT METHOD in Skills
    And skills User should receive the skill in JSON body from "<SheetName>" and <RowNumber>
    And skills check the Database with Skill id from "<SheetName>" and <RowNumber>
    Examples:
      | SheetName  | RowNumber |
      | Skills_PUT | 0         |
      | Skills_PUT | 1         |
      | Skills_PUT | 2         |
      | Skills_PUT | 3         |
      | Skills_PUT | 4         |
      | Skills_PUT | 5         |
      | Skills_PUT | 6         |
	  | Skills_PUT | 7         |


