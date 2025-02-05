

Feature: example/demo of scenario outline


Scenario Outline: Users in with shipping address in <state> should get charged sales tax

	Given I login as a new user
	When I add a $40 book to the cart
	And I add a "<state>" shipping address
	Then tax should be calculated

	Examples:
		| state |
		|  CA   |
		|  NY   |
		|  TX   |

