
  @smoke  @registration
  Feature: Registration smoke negative

    @existing_user
    Scenario: I try to register with existing email

      Given I have email of existing user
      Given I entery email in field
      Given error message 'user exists' should display
