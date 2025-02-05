

  Feature: Registration smoke

    Scenario: Navigate to registration and register with valid info

      Given I go to registration page
      When I fill in the form
      And I click on submit
      Then I should get success message


    Scenario: Registration with existing email should show correct error message

      Given I fill in the registration form and submit
      Then the error message 'User Exists Already' should be displayed