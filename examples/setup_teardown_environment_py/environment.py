
import logging as logger

import pdb


def before_all(context):
    logger.info("AAAAAA - BEFORE ALL")
    logger.info("")
    # pdb.set_trace()

def after_all(context):
    logger.info("AAAAA- AFTER ALL")
    logger.info("AAAAA- AFTER ALL")
    logger.info("AAAAA- AFTER ALL")
    # pdb.set_trace()


def before_feature(context, feature):

    all_tags = feature.tags

    if 'smoke' in all_tags:
        context.smoke = True

    logger.info("FFFFF - BEFORE FEATURE")
    logger.info("")

def after_feature(context, feature):


    logger.info("FFFFF - AFTER FEATURE")
    logger.info("")


def before_scenario(context, scenario):

    logger.info("SSSSSS - BEFORE SCENARIO")
    logger.info("")
    if scenario.name == 'checkout with new user':
        # setup for the scenario
        # call()
        pass


def after_scenario(context, scenario):

    logger.info("SSSS - AFTER SCENARIO")
    logger.info("")
    pdb.set_trace()


def before_step(context, step):

    logger.info("STSTST - BEFORE STEP")
    logger.info("")

def after_step(context, step):

    if step.status.name == 'failed':
        # take screen shot
        pass

def before_tag(context, tag):

    logger.info("TTTT - BEFORE TAG")
    logger.info("")

def after_tag(context, tag):
    logger.info("TTTTT - AFTER TAG")
    logger.info("")
