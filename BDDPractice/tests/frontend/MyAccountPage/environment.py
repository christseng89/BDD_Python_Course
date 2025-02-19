from BDDPractice.BDDCommon.CommonFuncs.webcommon import go_to
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from BDDCommon.CommonFuncs.webcommon import go_to

def before_all(context):
    """
    Set up the Selenium WebDriver before all tests.
    """
    context.driver = None  # Initialize driver as None

def before_scenario(context, scenario):
    """
    Set up WebDriver before each scenario.
    """

    go_to(context, 'my-account')

def after_scenario(context, scenario):
    """
    Close WebDriver after each scenario.
    """
    if context.driver:
        context.driver.quit()
        context.driver = None

def before_step(context, step):
    """
    Print the name of the step that is about to be
    """
    print(f"🚀 🚀 🚀 Running step: {step.name}")

