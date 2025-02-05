
Feature:  Create user with bad password

    Scenario Outline:  try password “<type>”

        Given I am at create user page
        When I type “<type>” password
        Then I should see error message

        Examples:
            | type         |
            | too long     |
            | too short    |
            | all numbers  |
            | all letters  |
