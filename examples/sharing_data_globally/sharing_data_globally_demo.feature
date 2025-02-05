# demo to show how to pass around data from step to step

Feature: Sharing data globally

    Scenario: Refund should process

        Given I find recent order from database
        When I issue a refund for the order
        Then payment should get processed for the user

    Scenario: Refund should fail on a refunded item

        When I issue a refund on the same order
        Then the refund should fail to process