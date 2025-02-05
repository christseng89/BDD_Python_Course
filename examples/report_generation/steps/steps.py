from behave import given, when, then, step

import logging as logger



@step("I am a passing step")
def i_am_a_passing_steps(context):
    print("Step PASS")
    print("11111")
    logger.info("22222")
    logger.debug("33333")


@step("I am a failing step")
def i_am_a_failing_step(context):
    print("Scenario that is failing")
    print("Step FAIL")
    print("AAAAAAA")
    logger.info("BBBBBBB")
    raise Exception("Failing on purpose")

