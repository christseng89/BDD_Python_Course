from behave import given, when, then
import logging as logger


@given("I am at the home page")
def at_home_page(context):

    print("I am the code that will open browser and go to 1 home page")
    print("I am the code that will open browser and go to 2 home page")
    print("I am the code that will open browser and go to 3 home page")

    # logger.info("")
    logger.info("I am 1 INFO 1")
    logger.info("I am 1 INFO 2")
    logger.info("I am 1 INFO 3")
    logger.info("\n")

    logger.debug("")
    logger.debug("I am 1 DEBUG 1")
    logger.debug("I am 1 DEBUG 2")
    logger.debug("I am 1 DEBUG 3")


@when('I click on "contact us"')
def click_contact_us(context):

    print('I am clicking on the "contact us" ')
    logger.info("I am 22 INFO 1")
    logger.info("\n")

    logger.debug("I am 22 DEBUG 1")


@then("I should see 123 Testing St.")
def verify_address(context):

    print("I see the correct address")


@when("I click on my account")
def click_my_account(context):

    print("I am clicking on my account")

@then("I should see 'Preferences'")
def see_prefernces(context):

    print("Should see preferences")
    logger.info("I will fail 333 INFO 1")
    logger.info("I will fail 333 INFO 2")
    logger.info("\n")

    logger.debug("I will fail 333 DEBUG 1")
    logger.debug("I will fail 333 DEBUG 2")
    assert 1 == 2, "One is not same as Two"