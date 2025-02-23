"""
Module containing common functions used in several tests.
Functions that are not test or feature specific.
"""
import sys
import time
import logging as logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from BDDCommon.CommonConfigs import urlconfig
from BDDCommon.CommonConfigs.configurations import get_config

# Global locator mapping to be used by all functions
LOCATOR_MAPPING = {
    "id": By.ID,
    "xpath": By.XPATH,
    "link text": By.LINK_TEXT,
    "partial link text": By.PARTIAL_LINK_TEXT,
    "name": By.NAME,
    "tag name": By.TAG_NAME,
    "class name": By.CLASS_NAME,
    "css selector": By.CSS_SELECTOR,
}


def go_to(context, location, **kwargs):
    """
    Function to start instance of the specified browser and navigate to the specified url.
    :param location: the url or page key to navigate to
    :param context: Behave context containing the driver
    """
    if not location.startswith('http'):
        _url = urlconfig.URLCONFIG.get(location, "")
        base_url = urlconfig.URLCONFIG.get('base_url', "")

        if not _url or not base_url:
            print(f"❌ Invalid URL configuration. base_url={base_url}, _url={_url}, location={location}")
            sys.exit(1)  # Exit if URL is invalid

        url = base_url + _url
    else:
        url = location

    browser = context.config.userdata.get('browser', 'chrome')

    try:
        if browser.lower() == 'chrome':
            chrome_driver_path = get_config()['WEBDRIVER']['chrome_driver_path']
            print(f"✅ Chrome driver path: {chrome_driver_path}")
            options = webdriver.ChromeOptions()
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("--disable-gpu")
            driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

        elif browser.lower() == 'headlesschrome':
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            driver = webdriver.Chrome(options=options)

        elif browser.lower() in ('ff', 'firefox'):
            driver = webdriver.Firefox()

        else:
            print(f"❌ Unsupported browser type: {browser}")
            sys.exit(1)  # Exit if browser is not supported

        driver.maximize_window()
        driver.implicitly_wait(10)
        context.driver = driver

        url = url.strip()
        context.driver.get(url)

    except WebDriverException as e:
        print(f"❌ Failed to load the website: {url}")
        if 'driver' in locals() and driver is not None:
            print("🛑 Closing WebDriver...")
            driver.quit()
        sys.exit(1)  # Exit if unable to reach the website


def assert_page_title(context, expected_title):
    """
    Function to assert title of current page.
    :param expected_title: The expected title of the page.
    :param context: Behave context containing the driver.
    """
    actual_title = context.driver.title
    print("The actual title is: {}".format(actual_title))
    print("The expected title is: {}".format(expected_title))
    assert expected_title == actual_title, (
        f"The title is not as expected. Expected: {expected_title}, Actual: {actual_title}"
    )
    print(f"✅ The page title '{expected_title}' is as expected.")


def assert_current_url(context, expected_url):
    """
    Function to get the current url and assert it is same as the expected url.
    :param context: Behave context containing the driver.
    :param expected_url: The expected URL.
    """
    current_url = context.driver.current_url
    if not (expected_url.startswith('http') or expected_url.startswith('https')):
        expected_url = 'https://' + expected_url + '/'
    assert current_url == expected_url, (
        f"The current url is not as expected. Actual: {current_url}, Expected: {expected_url}"
    )
    print("✅ The page URL is as expected.")


def url_contains(context, text):
    current_url = context.driver.current_url
    return text in current_url


def assert_url_contains(context, text):
    contains = url_contains(context, text)
    assert contains, f"Current url '{context.driver.current_url}' does not contain text '{text}'."


def find_element(context, locator_attribute, locator_text, timeout=20):
    """
    Finds an element using an explicit wait and returns the element object.
    """
    if locator_attribute not in LOCATOR_MAPPING:
        raise Exception(f"Invalid locator attribute. Approved attributes: {list(LOCATOR_MAPPING.keys())}")

    try:
        wait = WebDriverWait(context.driver, timeout)
        element = wait.until(
            EC.presence_of_element_located((LOCATOR_MAPPING[locator_attribute], locator_text))
        )
        return element
    except Exception as e:
        raise Exception(e)


def find_elements(context, locator_attribute, locator_text, timeout=20):
    """
    Finds multiple elements using an explicit wait and returns the list of element objects.
    :param context: The Behave context containing the driver.
    :param locator_attribute: The attribute to locate the elements (e.g., id, xpath, css selector).
    :param locator_text: The value of the locator.
    :param timeout: Time in seconds to wait for the elements to be present.
    """
    if locator_attribute not in LOCATOR_MAPPING:
        raise Exception(f"Invalid locator attribute. Approved attributes: {list(LOCATOR_MAPPING.keys())}")

    try:
        wait = WebDriverWait(context.driver, timeout)
        elements = wait.until(
            EC.presence_of_all_elements_located((LOCATOR_MAPPING[locator_attribute], locator_text))
        )
        return elements
    except Exception as e:
        raise Exception(e)


def is_element_visible(element):
    """
    Checks if element is visible and returns True or False.
    """
    return element.is_displayed()


def assert_element_visible(context_or_element, locator_att=None, locator_text=None):
    """
    Function to check if the passed in element is visible.
    Raises an exception if it is not.
    """
    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        element = context_or_element
    else:
        element = context_or_element.driver.find_element(locator_att, locator_text)

    if not element.is_displayed():
        raise AssertionError('The element is not displayed')


def type_into_element(context_or_element, input_value, locator_att, locator_text, timeout=20):
    """
    Types into an element after waiting for it to be visible.
    """
    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        element = context_or_element
    else:
        if locator_att not in LOCATOR_MAPPING:
            raise Exception(f"Invalid locator attribute. Approved attributes: {list(LOCATOR_MAPPING.keys())}")
        wait = WebDriverWait(context_or_element.driver, timeout)
        element = wait.until(
            EC.visibility_of_element_located((LOCATOR_MAPPING[locator_att], locator_text))
        )
    element.send_keys(input_value)


def click(context_or_element, locator_att=None, locator_text=None, timeout=20):
    """
    Clicks on an element. If a locator is provided, it waits until the element is clickable.
    """
    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        element = context_or_element
    else:
        if locator_att not in LOCATOR_MAPPING:
            raise Exception(f"Invalid locator attribute. Approved attributes: {list(LOCATOR_MAPPING.keys())}")
        wait = WebDriverWait(context_or_element.driver, timeout)
        element = wait.until(
            EC.element_to_be_clickable((LOCATOR_MAPPING[locator_att], locator_text))
        )
    element.click()


def element_contains_text(context_or_element, expected_text, locator_att, locator_text, case_sensitive=False):
    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        element = context_or_element
    else:
        element = context_or_element.driver.find_element(locator_att, locator_text)

    element_text = element.text
    if not case_sensitive:
        return expected_text.lower() in element_text.lower()
    else:
        return expected_text in element_text


def assert_element_contains_text(context_or_element, expected_text, locator_att, locator_text, case_sensitive=False):
    max_try = 5
    sleep_bn_try = 2
    for i in range(max_try):
        try:
            contains = element_contains_text(context_or_element, expected_text, locator_att, locator_text, case_sensitive)
            assert contains, "Element does not contain text"
            break
        except AssertionError:
            print(f"Checking if element contains text. Retry number: {i}")
            time.sleep(sleep_bn_try)
    else:
        raise Exception(
            f"Element with locator type '{locator_att}', and locator text '{locator_text}', does not contain the text '{expected_text}'. "
            f"Retried {max_try * sleep_bn_try} seconds"
        )


def assert_radio_is_selected(context_or_element, locator_att=None, locator_text=None):
    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        element = context_or_element
    else:
        element = context_or_element.driver.find_element(locator_att, locator_text)

    is_checked = element.get_attribute('checked')
    assert is_checked, f"The radio is not selected {element.get_attribute('name')}"


def get_element_text(context_or_element, locator_att=None, locator_text=None):
    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        return context_or_element.text
    else:
        element = context_or_element.driver.find_element(locator_att, locator_text)
        return element.text
