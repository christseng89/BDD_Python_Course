# Example

Feature: Passing parameters to steps

  Scenario: method 1 of passing step parameters


	Given I have a new 'DVD' in my cart
	And I have a new 'BOOK' in my cart
	And I have a new '' in my cart
	When I click on "Next"
	And I click on "FINISH"
	Then I should see "Error"

  Scenario: Add 10 participants in the call

	Given I start a call with "10" participants

  Scenario Outline: Adding items to cart and completing the process
	Given I have a new '<item1>' in my cart
	And I have a new '<item2>' in my cart
	And I have a new '<item3>' in my cart
	When I click on "Next"
	And I click on "FINISH"
	Then I should see "<expected_result>"

	Examples:
	  | item1  | item2   | item3 | expected_result |
	  | DVD    | BOOK    |       | Error           |
	  | LAPTOP | MOUSE   | BAG   | Success         |
	  | PHONE  | HEADSET |       | Error           |