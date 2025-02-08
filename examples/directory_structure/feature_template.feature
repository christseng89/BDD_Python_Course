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
    Scenario: Scenario1
      Given Scenario1 given step 1
      And Scenario1 given step 2
      When Scenario1 when step 1
      And Scenario1 when step 2
      And Scenario1 when step 3
      But Scenario1 when but step
      Then Scenario1 then step 1
      And Scenario1 then step 2
      And Scenario1 then step 3
      And Scenario1 then step 4
      But Scenario1 then but step

    @tag1 @tag4 @tag5
    Scenario: Scenario2
      Given Scenario2 given step 1
      And Scenario2 given step 2
      When Scenario2 when step 1
      And Scenario2 when step 2
      And Scenario2 when step 3
      But Scenario2 when but step
      Then Scenario2 then step 1
      And Scenario2 then step 2
      And Scenario2 then step 3
      And Scenario2 then step 4
      But Scenario2 then but step

  @tag1 @tag4 @tag5
  Scenario Outline: Scenario1 outline step
    Scenario: Scenario1
      Given Scenario1 given step 1
      And Scenario1 given step 2
      When Scenario1 when step 1
      And Scenario1 when step 2
      And Scenario1 when step 3
      But Scenario1 when but step
      Then Scenario1 then step 1
      And Scenario1 then step 2
      And Scenario1 then step 3
      And Scenario1 then step 4
      But Scenario1 then but step

#    Examples:
