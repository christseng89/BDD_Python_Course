#from behave import given, when, then
from BDDCommon.CommonSteps.webstepscommon import *
from BDDCommon.CommonConfigs import locatorsconfig
from BDDCommon.CommonFuncs import webcommon


@then('the "{nav_bar}" bar should be visible')
def verify_nav_bars_visible(context, nav_bar):

    # import pdb; pdb.set_trace()
    expected_bars = ['main navigation', 'top navigation', 'options']
    if nav_bar not in expected_bars:
        raise Exception("The passed in nav_bar type is not one of expected."
                            "Actual: {}, Expected in: {}".format(nav_bar, expected_bars))

    locator_info = locatorsconfig.LOCATORS.get(nav_bar)
    locator_type = locator_info['type']
    locator_text = locator_info['locator']

    nav_element = webcommon.find_element(context, locator_type, locator_text)

    webcommon.assert_element_visible(nav_element)