from behave import given, then, when


@given("I go to registration page")
def go_to_registration_page(context):
    print("Going to registration page")

@when("I fill in the form")
def fill_in_the_form(context):
    print("I am filling in the form")

@when("I click on submit")
def click_on_submit(context):
    print("I click on submit")

@then("I should get success message")
def i_should_get_success_message(context):
    print("I get success message")

@given("I fill in the registration form and submit")
def fill_in_registration_form_and_submit(context):

    context.execute_steps(u"""
                Given I go to registration page
                When I fill in the form
                And I click on submit
                """)

@then("the error message 'User Exists Already' should be displayed")
def verify_error_message(context):
    pass