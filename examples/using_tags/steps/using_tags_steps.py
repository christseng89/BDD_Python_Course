
from behave import given, when, then


@given("I navigate to the home page")
def navigate_to_home_page(context):

    print("I AM AT THE HOME PAGE NOW")

@then("I should see all navigation panels")
def should_see_all_navigation_panels(context):

    print("I SEE ALL NAVIATION PANESL")


@then("the {location} navigation panel should have all options")
def home_page_navigation_panels(context, location):


    print("I AM VERIFYING THE NAVIGATION PANEL ON SIDE: {}".format(location.upper()))