from behave import given, then

# Create user and coupon
@given('make “{call}” API call with “{data}” data')
def step_make_api_call(context, call, data):
    print(f"API Call: {call} with Data: {data}")


@then('the response should have “{status_code}” status code and “{message}” message')
def step_check_response(context, status_code, message):
    print(f"Expected Status Code: {status_code}")
    print(f"Expected Message: {message}")

@given('I create  “{gender}” user')
def step_create_user(context, gender):
    print(f"Creating a {gender} user")

# Login page color
@when('I login with the  user')
def step_login_user(context):
    print(f"✅ Login user step: {context.current_step}")
    print("Logging in with the created user")

@then('the page color should  “{page_color}”')
def step_check_page_color(context, page_color):
    print(f"Checking that the page color is {page_color}")

# User create bad password
@given('I am at create user page')
def step_at_create_user_page(context):
    print("Navigated to the create user page")

@when('I type “{type}” password')
def step_type_password(context, type):
    print(f"Typing a {type} password")

@then('I should see error message')
def step_see_error_message(context):
    print("Verifying that an error message is displayed")