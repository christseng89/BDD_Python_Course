
  @my_account_smoke  @smoke
  Feature: My Account Smoke Tests


    @TCID-10
    Scenario: Valid user should be able to login

      Given I go to 'my account' page
      When I type 'admin' into username of login form
      And I type 'admin$123' into password of login form
      And I click on the 'login' button
      Then user should be logged in

    @TCID-11
    Scenario: User with wrong password should gt correct error message

      Given I go to 'my account' page
      When I type 'admin' into username of login form
      And I type '123456' into password of login form
      And I click on the 'login' button
      Then error messsage with email 'admin' should be displayed

    @TCID-12
    Scenario: User with none-existing email should get correct error message

      Given I go to 'my account' page
      When I type 'nonexisting@supersqa.com' into username of login form
      And I type '123456' into password of login form
      And I click on the 'login' button
      Then error messsage with 'Unknown email' should be displayed
