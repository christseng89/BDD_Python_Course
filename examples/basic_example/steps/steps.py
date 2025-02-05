
from behave import given, when, then
import user
import assertions
import pdb

@given("I create a new user")
def create_new_user(context):
    """
    Step to create a new user.
    :return:
    """
    print("I am creating a new user")
    print(":) :) :) :) :) :)")
    print("More code would go here")
    # user.user_creator()
    prefix = context.config.userdata.get('prefix')

    pdb.set_trace()

@when("I type email")
def type_the_email(context):
    """
    Step to type email address in the email field
    :return:
    """

    print("Typing the email in the email field.")
    # email_field = driver.find_element('id', 'email')
    # email_field.send_keys('test@supersqa.com')
    print("Just finished typing the email :)")

@when("I type password")
def type_the_password(context):
    """
    Step to type email address in the password field
    :return:
    """
    print("Typing the password in the password field")
    # pass_field = driver.find_element_by_id('password')
    # pass_field.send_keys('123456')
    print("Just typed the password. :)")

@when("I click on 'Login'")
def click_login(context):
    """
    Step to click login
    :return:
    """
    print("I am clicking login!!!!")

@then("I should see the text Welcome")
def see_welcome_text(context):
    """
    Step to verify text is displayed
    :return:
    """
    assertions.assert_text_visible('Welcome')
    print("checking if 'Welcome' text is displayed")
    print("Yep it sure is there!!!")
    print("PASS!!!")

@when("I type correct email")
def type_correct_email(context):
    print("Typing correct email.")