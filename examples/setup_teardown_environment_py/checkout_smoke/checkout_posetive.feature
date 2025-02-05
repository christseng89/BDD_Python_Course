

  @smoke  @checkout
  Feature: Checkout Smoke

    @checkout_new_user  @TCID-22
    Scenario: checkout with new user

      Given I am on checkout page
      When I enter billing info
      Then I should checkout