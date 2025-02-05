


@f1
Feature: My Feature 1

  @f1s1
  Scenario: Scenario 1 of Feature 1

    Given I am a passing step
#    Then I am a passing step

  @f1s2
  Scenario: Scenario 2 of Feature 1

    Given I am a passing step
    Then I am a failing step
    Then I am a passing step
    Then I am a passing step

      @f1s1
  Scenario: Scenario 3 of Feature 1

    Given I am a passing step

          @f1s1
  Scenario: Scenario 4 of Feature 1

    Given I am a passing step