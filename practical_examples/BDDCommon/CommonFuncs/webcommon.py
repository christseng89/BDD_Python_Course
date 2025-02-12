"""
Module containing common function used in several tests.
Functions that are not test or feature specific.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from BDDCommon.CommonConfigs.configurations import get_config


def go_to(url, browser_type=None):
    """
    Start a browser instance and navigate to the specified URL.

    :param url: The URL to navigate to.
    :param browser_type: The browser type (Default is Chrome).

    :return: WebDriver instance.
    """

    chrome_driver_path = get_config()['WEBDRIVER']['chrome_driver_path']

    # Set Chrome options to bypass SSL errors
    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--ignore-ssl-errors=yes")
    chrome_options.add_argument("--disable-gpu")

    # Create WebDriver instance
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

    # Maximize the window
    driver.maximize_window()

    # Navigate to the URL
    url = url.strip()
    driver.get(url)

    return driver  # ✅ Return driver instead of modifying `context`


def assert_page_title(context, expected_title):
    """
    Function to assert title of current page.
    :param expected_title:
    :param context:
    """

    actual_title = context.driver.title

    print("The actual title is: {}".format(actual_title))
    print("The expected title is: {}".format(expected_title))

    assert expected_title == actual_title, "The title is not as expected." \
                                           " Expected: {}, Actual: {}".format(expected_title, actual_title)
    print(f"✅ The page title '{expected_title}' is as expected.")


def assert_current_url(context, expected_url):
    """
    Function to get the current url and assert it is same as the expected url.
    :param context:
    :param expected_url:
    """

    # get the current url
    current_url = context.driver.current_url

    if not expected_url.startswith('http') or not expected_url.startswith('https'):
        expected_url = 'https://' + expected_url + '/'

    assert current_url == expected_url, "The current url is not as expected." \
                                        " Actual: {}, Expected: {}".format(current_url, expected_url)

    print(f"✅ The page URL is as expected '{current_url}'.")

#======================================================================================#
def find_element(context, locator_attribute, locator_text):
    """
    Finds an element and returns the element object.
    :param context:
    :param locator_attribute: what to use to locate (example, id, class, xpath,....)
    :param locator_text: the locator text (ex. the id, the class, the name,...)
    """

    possible_locators = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector"]

    if locator_attribute not in possible_locators:
        raise Exception('The locator attribute provided is not in the approved attributes. Or the spelling and format does not match.\
                            The approved attributes are : %s ' % possible_locators)
    try:
        element = context.driver.find_element(locator_attribute, locator_text)
        return element
    except Exception as e:
        raise Exception(e)
#======================================================================================#
def is_element_visible(element):
    '''
    Checks if element is visible and returns True or False
    '''

    if element.is_displayed():
        return True
    else:
        return False
#======================================================================================#
def assert_element_visible(element):
    '''
    Function to check if the passed in element is visible.
    Raises and exception if it is not exception.
    '''

    if not element.is_displayed():
        raise AssertionError('The element is not displayed')