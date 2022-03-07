Feature: To check The POST method for Skills
Background:
	Given Skills User is on Endpoint: url/Skills with valid username and password


    Scenario Outline: Verify POST for a Skill when user logged with UserName with Password
    When skills User sends POST request body in skills from "<SheetName>" and <RowNumber> with valid JSON Schema
    Then skills User validates the StatusCode and the StatusMessage from "<SheetName>" sheet and <RowNumber> row
    And JSON schema is valid for POST/PUT METHOD in Skills
    And skills User should receive the skill in JSON body from "<SheetName>" and <RowNumber>
    And skills check the Database with Skill id from "<SheetName>" and <RowNumber>
    Examples:
        | SheetName   | RowNumber |
        | Skills_POST | 0         |
        | Skills_POST | 1         |
        | Skills_POST | 2         |
        | Skills_POST | 3         |
        | Skills_POST | 4         |
        | Skills_POST | 5         |
        | Skills_POST | 6         |





