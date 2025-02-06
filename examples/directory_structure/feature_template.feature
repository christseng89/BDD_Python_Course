# Created by samfi at 2025/2/6
Feature: # Enter feature name here
  # Enter feature description here

    Background: Background step
        # Enter steps here
        Given Background given step
        When Background when step

  @tag1 @tag2 @tag3
  Scenario: Scenario1 step
    # Enter steps here
    Given Scenario1 given step
    When Scenario1 when step
    And Scenario1 when and step 1
    And Scenario1 when and step 2
    But Scenario1 but step
    Then Scenario1 then step 1
    Then Scenario1 then step 2
    And Scenario1 then and step 1
    And Scenario1 then and step 2
    But Scenario1 then but step

    @tag1 @tag4 @tag5
  Scenario: Scenario2 step
    # Enter steps here
    Given Scenario2 given step
    When Scenario2 when step
    And Scenario2 when and step 1
    And Scenario2 when and step 2
    But Scenario2 but step
    Then Scenario2 then step 1
    Then Scenario2 then step 2
    And Scenario2 then and step 1
    And Scenario2 then and step 2
    But Scenario2 then but step

  @tag1 @tag4 @tag5
  Scenario Outline: Scenario1 outline step
    Scenario: Scenario1
      Given Scenario1 given step
      When Scenario1 when step
      And Scenario1 when and step 1
      And Scenario1 when and step 2
      But Scenario1 but step
      Then Scenario1 then step 1
      Then Scenario1 then step 2
      And Scenario1 then and step 1
      And Scenario1 then and step 2
      But Scenario1 then but step

#    Examples:
