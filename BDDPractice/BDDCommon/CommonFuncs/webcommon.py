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

# Global locator mapping to avoid duplicate code in functions
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

TIMEOUT = 15

def go_to(context, location, **kwargs):
    """
    Function to start an instance of the specified browser and navigate to the specified URL.
    :param location: the URL or page key to navigate to
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
        driver.implicitly_wait(TIMEOUT)
        context.driver = driver

        url = url.strip()
        context.driver.get(url)

    except WebDriverException as e:
        print(f"❌ Failed to load the website: {url}")
        if 'driver' in locals() and driver is not None:
            print("🛑 Closing WebDriver...")
            driver.quit()
        sys.exit(1)

def assert_page_title(context, expected_title):
    """
    Asserts that the current page title matches the expected title.
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
    Asserts that the current URL matches the expected URL.
    """
    current_url = context.driver.current_url
    if not expected_url.startswith('http'):
        expected_url = 'https://' + expected_url + '/'
    assert current_url == expected_url, (
        f"The current URL is not as expected. Actual: {current_url}, Expected: {expected_url}"
    )
    print("✅ The page URL is as expected.")

def url_contains(context, text):
    """
    Returns True if the current URL contains the given text.
    """
    return text in context.driver.current_url

def assert_url_contains(context, text):
    """
    Asserts that the current URL contains the given text.
    """
    contains = url_contains(context, text)
    assert contains, f"Current URL '{context.driver.current_url}' does not contain text '{text}'."

def find_element(context, locator_attribute, locator_text, timeout=TIMEOUT):
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

def find_elements(context, locator_attribute, locator_text, timeout=TIMEOUT):
    """
    Finds multiple elements using an explicit wait and returns a list of element objects.
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
        print(f"❌ Error: element '{locator_text}' not found within '{timeout}' seconds.")
        sys.exit(1)

def is_element_visible(element):
    """
    Checks if an element is visible.
    """
    return element.is_displayed()


def assert_element_visible(context_or_element, locator_att=None, locator_text=None, timeout=TIMEOUT):
    """
    Asserts that an element is visible using an explicit wait.

    If a WebElement is passed directly, it waits until that element is visible.
    Otherwise, it waits for the element specified by the locator to be visible.

    :param context_or_element: Either a WebElement or a context with a driver.
    :param locator_att: The locator attribute (e.g., "id", "xpath") if a WebElement isn't passed.
    :param locator_text: The locator value if a WebElement isn't passed.
    :param timeout: Maximum number of seconds to wait.
    """
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        element = context_or_element
        driver = element.parent  # Retrieves the driver from the element.
        wait = WebDriverWait(driver, timeout)
        try:
            wait.until(EC.visibility_of(element))
        except Exception:
            raise AssertionError(f"The element is not visible within {timeout} seconds.")
    else:
        driver = context_or_element.driver
        if not locator_att or not locator_text:
            raise Exception("Locator attribute and locator text must be provided when not passing a WebElement.")
        wait = WebDriverWait(driver, timeout)
        try:
            # Assumes LOCATOR_MAPPING is a globally defined dictionary mapping locator names to By strategies.
            element = wait.until(
                EC.visibility_of_element_located((LOCATOR_MAPPING[locator_att], locator_text))
            )
        except Exception:
            raise AssertionError(
                f"The element with locator '{locator_att}'='{locator_text}' is not visible within {timeout} seconds.")


def type_into_element(context_or_element, input_value, locator_att, locator_text, timeout=TIMEOUT):
    """
    Types into an element after waiting for its visibility.
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

def click(context_or_element, locator_att=None, locator_text=None, timeout=TIMEOUT):
    """
    Clicks on an element. If a locator is provided, waits until the element is clickable.
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


def element_contains_text(context_or_element, expected_text, locator_att, locator_text, case_sensitive=False,
                          timeout=TIMEOUT):
    """
    Waits until the specified element contains the expected text and returns True.
    Raises a TimeoutException if the expected text is not found within the timeout.
    """
    # Determine the driver and a callable to fetch the element text
    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        # Use the element's parent driver.
        driver = context_or_element.parent
        get_text = lambda: context_or_element.text
    else:
        driver = context_or_element.driver
        # Here, LOCATOR_MAPPING is assumed to be a global dictionary mapping locator types.
        get_text = lambda: driver.find_element(LOCATOR_MAPPING[locator_att], locator_text).text

    wait = WebDriverWait(driver, timeout)

    # Define a condition function based on case sensitivity
    if not case_sensitive:
        condition = lambda d: expected_text.lower() in get_text().lower()
    else:
        condition = lambda d: expected_text in get_text()

    # Wait until the condition is met; a TimeoutException is raised if not.
    wait.until(condition)
    return True


def assert_element_contains_text(context_or_element, expected_text, locator_att, locator_text, case_sensitive=False,
                                 timeout=TIMEOUT):
    """
    Asserts that an element contains the expected text.
    Uses an explicit wait so that the check is retried until the timeout is reached.
    """
    try:
        element_contains_text(context_or_element, expected_text, locator_att, locator_text, case_sensitive, timeout)
        # If wait.until() succeeds, the text is present.
    except Exception as e:
        raise Exception(
            f"Element with locator type '{locator_att}', and locator text '{locator_text}', "
            f"does not contain the text '{expected_text}' after waiting for {timeout} seconds."
        )

def assert_radio_is_selected(context_or_element, locator_att=None, locator_text=None, timeout=TIMEOUT):
    """
    Asserts that a radio button element is selected.
    Waits until the radio button's selected state is True.
    """
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        element = context_or_element
        driver = element.parent
        wait = WebDriverWait(driver, timeout)
        # Wait until the element is selected
        wait.until(lambda d: element.is_selected())
    else:
        driver = context_or_element.driver
        if locator_att not in LOCATOR_MAPPING:
            raise Exception(f"Invalid locator attribute. Approved attributes: {list(LOCATOR_MAPPING.keys())}")
        locator = (LOCATOR_MAPPING[locator_att], locator_text)
        wait = WebDriverWait(driver, timeout)
        # Wait until the element's selection state is True
        wait.until(EC.element_selection_state_to_be(locator, True))
        element = driver.find_element(*locator)

    # Final assertion for clarity
    assert element.is_selected(), f"The radio button '{element.get_attribute('name')}' is not selected."



def get_element_text(context_or_element, locator_att=None, locator_text=None, timeout=TIMEOUT):
    """
    Retrieves the text of an element, waiting until it is visible.

    If a WebElement is provided directly, the function waits for its visibility.
    Otherwise, it uses the provided locator to wait until the element is visible.
    """
    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        element = context_or_element
        # Wait until the element is visible using its parent driver.
        driver = element.parent
        wait = WebDriverWait(driver, timeout)
        wait.until(EC.visibility_of(element))
        return element.text
    else:
        driver = context_or_element.driver
        wait = WebDriverWait(driver, timeout)
        element = wait.until(
            EC.visibility_of_element_located((LOCATOR_MAPPING[locator_att], locator_text))
        )
        return element.text
