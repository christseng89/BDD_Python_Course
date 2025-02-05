@regression
Feature: Navigation panels in home page

    @smoke
    Scenario: The home page should have all navigation panels

        Given I navigate to the home page
        Then I should see all navigation panels


    @smoke
    Scenario: The left navigation panel should have all options

        Given I navigate to the home page
        Then the left navigation panel should have all options


    Scenario: The top navigation panel should have all options

        Given I navigate to the home page
        Then the top navigation panel should have all options