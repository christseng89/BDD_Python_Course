import logging

logger = logging.getLogger("behave_logger")
logger.setLevel(logging.INFO)

def before_scenario(context, scenario):
    """Closes the browser after each scenario."""
    logger.info(f"Scenario '{scenario.name}' is starting...")

def after_scenario(context, scenario):
    """Closes the browser after each scenario."""
    if hasattr(context, "driver"):
        context.driver.quit()

    """Log the outcome of the scenario."""
    if scenario.status == "failed":
        logger.error(f"Scenario '{scenario.name}' failed.")
    else:
        logger.info(f"Scenario '{scenario.name}' passed.")
