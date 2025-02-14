
from behave import given, when, then

def print_current_step(context):
    print(f"Step Name: '{context.current_step}', Tag: '@{context.current_tag}'")

@given("I navigate to the home page")
def navigate_to_home_page(context):

    print_current_step(context)

@then("I should see all navigation panels")
def should_see_all_navigation_panels(context):

    print_current_step(context)

@then("the {location} navigation panel should have all options")
def home_page_navigation_panels(context, location):

    print_current_step(context)
    print("I AM VERIFYING THE NAVIGATION PANEL ON SIDE: {}".format(location.upper()))