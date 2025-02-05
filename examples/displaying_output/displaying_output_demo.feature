
Feature: Demo of displaying output on console

Scenario: A test that will PASS (stdout demo)

    Given I am at the home page
    When I click on "contact us"
    Then I should see 123 Testing St.



Scenario: A test that will FAIL (stdout demo)

    Given I am at the home page
    When I click on my account
    Then I should see 'Preferences'