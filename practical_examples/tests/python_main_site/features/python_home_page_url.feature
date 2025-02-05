

Feature: Verifying the home page url goes to the right place


    Scenario: The Python home page should have correct title

        Given I go to the site "python.org"
        Then the page title should be "Welcome to Python.org"

    Scenario: The Python home page should have correct url

        Given I go to the site "python.org"
        Then current url should be "www.python.org"