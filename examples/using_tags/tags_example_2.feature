@regression
Feature: Navigation panels in home page

    @smoke @homepage @logged_out
    Scenario: The home page should have all navigation panels

        Given I navigate to the home page
        Then I should see all navigation panels


    @smoke @homepage
    Scenario: The left navigation panel should have all options

        Given I navigate to the home page
        Then the left navigation panel should have all options

    @logged_in
    Scenario: The top navigation panel should have all options

        Given I navigate to the home page
        Then the top navigation panel should have all options