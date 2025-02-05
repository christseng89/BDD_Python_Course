from behave import given, then, when
import logging as logger


@given("I am on checkout page")
def on_checkout_page(context):
    logger.info("ON CHECKOUT")
    logger.info("")

@when("I enter billing info")
def enter_billing_info(context):
    logger.info("ENTER BILLING")
    logger.info("")

@then("I should checkout")
def i_should_checkout(context):
    logger.info("I SHOULD CHECKOUT")
    logger.info("")