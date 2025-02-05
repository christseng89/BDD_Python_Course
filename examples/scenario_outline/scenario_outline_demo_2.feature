
Feature: 2nd example/demo of scenario outline


Scenario Outline: "<quantity>" and "<payment method>"

	Given I have "<quantity>" items in my cart
	When I checkout using "<payment method>"
	Then my order should be placed


	Examples:
		| quantity | payment method |
		|    1     |  credit card   |
		|   10     |  credit card   |
		|   15     |  credit card   |
		|    1     |   gift card    |
		|   10     |   gift card    |
		|   15     |   gift card    |

