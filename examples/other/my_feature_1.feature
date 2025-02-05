


@f1
Feature: My Feature 1

  @f1s1
  Scenario: Scenario 1 of Feature 1

    Given I am a passing step
      """
      This is just random string in 1st step.
      Second line of 1st string. And
      3rd line of 1st string.
      """
    Then I another a passing step
      """
      {"first_name": "Admas", "last_name": "Kinfu",
      "phone": "4081111111"}
      """

  @f1s2
  Scenario: Scenario 2 of Feature 1

    Given I am a passing step
    Then I am a failing step
    Then I am a passing step
    Then I am a passing step


  Scenario: Scenario 3 of Feature 1

    Given I am a passing step


  Scenario: Scenario 4 of Feature 1

    Given I am a passing step