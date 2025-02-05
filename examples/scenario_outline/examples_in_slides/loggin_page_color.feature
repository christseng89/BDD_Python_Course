
Feature:  page color logged in

    Scenario Outline:  login as  “<gender>”

        Given I create  “<gender>” user
        When I login with the  user
        Then the page color should  “< page color>”

        Examples:
            |  gender | page color |
            |  female |    pink    |
            |   male  |    blue    |

