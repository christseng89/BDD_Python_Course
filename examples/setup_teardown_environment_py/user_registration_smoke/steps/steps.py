from behave import given


@given("I have email of existing user")
def i_have_email_of_existing_user(context):
    context.existing_email = 'foo@bar.com'
    print("FINDING EXISTING USER")

@given("I entery email in field")
def enter_email_in_field(context):
    print("ENTERING EMAIL IN FIELD")

@given("error message 'user exists' should display")
def error_message_user_exists_should_display(context):
    print("VERIFYING THE MESSAGE ON THE PAGE")
