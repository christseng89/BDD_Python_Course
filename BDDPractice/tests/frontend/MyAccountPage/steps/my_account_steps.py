from behave import *
from BDDCommon.CommonFuncs import webcommon
from BDDCommon.CommonConfigs.locatorsconfig import MY_ACCOUNT_LOCATORS
import pdb


@step("I type '{email}' into username of login form")
def type_email_into_username_of_login_form(context, email):
    """

    :param context:
    :param email:
    :return:
    """
    email_locator_type = MY_ACCOUNT_LOCATORS['login_user_name']['type']
    email_locator_string = MY_ACCOUNT_LOCATORS['login_user_name']['locator']

    webcommon.type_into_element(context, email, email_locator_type, email_locator_string)


@step("I type '{password}' into password of login form")
def type_password_into_password_of_login_form(context, password):
    """

    :param context:
    :return:
    """

    pass_locator_type = MY_ACCOUNT_LOCATORS['login_user_password']['type']
    pass_locator_string = MY_ACCOUNT_LOCATORS['login_user_password']['locator']

    webcommon.type_into_element(context, password, pass_locator_type, pass_locator_string)


@step("I click on the '{btn_name}' button")
def i_click_on_the_login_button(context, btn_name):
    """

    :param context:
    :param btn_name:
    :return:
    """
    if btn_name.lower() in ('login', 'log in'):
        login_btn_locator_type = MY_ACCOUNT_LOCATORS['login_btn']['type']
        login_btn_locator_string = MY_ACCOUNT_LOCATORS['login_btn']['locator']
    else:
        raise Exception("Not implemented")

    webcommon.click(context, login_btn_locator_type, login_btn_locator_string)


@step("user should be logged in")
def user_should_be_logged_in(context):
    """

    :param context:
    :return:
    """

    nav_bar_type = MY_ACCOUNT_LOCATORS['left_nav']['type']
    nav_bar_text = MY_ACCOUNT_LOCATORS['left_nav']['locator']

    logout_type = MY_ACCOUNT_LOCATORS['left_nav_logout_btn']['type']
    logout_text = MY_ACCOUNT_LOCATORS['left_nav_logout_btn']['locator']

    webcommon.assert_element_visible(context, nav_bar_type, nav_bar_text)
    webcommon.assert_element_visible(context, logout_type, logout_text)


@step("error messsage with email '{email}' should be displayed")
def error_message_with_email_should_be_displayed(context, email):
    """
    Step to verify that the error message appears when a wrong password is entered.
    """

    expected_msg = f"Error: The password you entered for the email address {email} is incorrect. Lost your password?".lower()

    error_box_type = MY_ACCOUNT_LOCATORS['error_box']['type']
    error_box_text = MY_ACCOUNT_LOCATORS['error_box']['locator']

    actual_message = webcommon.get_element_text(context, error_box_type, error_box_text).lower()

    if expected_msg in actual_message:
        print(f"✅ Test Passed: Message '{expected_msg}' displayed correctly.")
    else:
        print(f"❌ Test Failed: Expected error message '{expected_msg}', but got '{actual_message}'")
        assert False, f"Authentication {email} failed with '{actual_message}' error."

    # pdb.set_trace()

@step("error messsage with 'Unknown email' should be displayed")
def error_message_with_unknown_email_should_be_displayed(context):
    """

    """
    expected_error_msg = "unknown email address. check again or try your username."

    error_box_type = MY_ACCOUNT_LOCATORS['error_box']['type']
    error_box_text = MY_ACCOUNT_LOCATORS['error_box']['locator']

    actual_message = webcommon.get_element_text(context, error_box_type, error_box_text).lower()
    print (f"Actual message: {actual_message}")
    if actual_message not in expected_error_msg:
        print('Passed...')
    else:
        # raise Exception("Correct error message not displayed at failed loggen. None existing email: {}")
        assert False, f"❌ Unknown email address. check again or try your username."
    # pdb.set_trace()