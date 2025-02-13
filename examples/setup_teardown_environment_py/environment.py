import logging
import pdb


logger = logging.getLogger("behave_logger")
logger.setLevel(logging.INFO)


def before_feature(context, feature):
    """Log the start of feature execution."""
    logger.info(f"Before feature: '{feature.name}'")

def after_feature(context, feature):
    """Log the completion of a feature."""
    logger.info(f"After feature: '{feature.name}'")

def before_scenario(context, scenario):
    """Before each scenario."""
    logger.info(f"Before scenario '{scenario.name}'.")

def after_scenario(context, scenario):
    """Log the outcome of the scenario."""
    if scenario.status == "failed":
        logger.error(f"After scenario '{scenario.name}' failed.")
    else:
        logger.info(f"After scenario '{scenario.name}' passed.")

    # pdb.set_trace()
    # scenario.status
    # dir(scenario.status)
    # scenario.status.value
    # scenario.status.name
    # dir(scenario)


def before_step(context, step):
    """Log each step before execution."""
    logger.info(f"Before step: '{step.name}'")

def after_step(context, step):
    """Log the result of each step."""
    if step.status == "failed":
        logger.error(f"After step '{step.name}' failed.")
    else:
        logger.info(f"After step '{step.name}' passed.")

def before_tag(context, tag):
    """Special setup for scenarios tagged with @high_priority."""
    logger.info(f"Before tag: '{tag}'")

def after_tag(context, tag):
    """Special teardown for scenarios tagged with @high_priority."""
    logger.info(f"After tag: '{tag}'")
