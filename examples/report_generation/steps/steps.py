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
    try:
        print("Scenario that is failing")
        print("Step TRY")
        logger.info("BBBBBBB")

        # Simulate an error
        raise Exception("❌ Failing on purpose")

    except Exception as e:
        print(f"Exception caught: {e}")
        logger.error(f"Exception caught: {e}")

        # Optional: Fail the step manually
        assert False, f"Step failed due to exception: {e}"