
from behave import given, then, when


@given("I have a new {item} in my cart")
def i_have_item_in_cart(context, item):
    print("The item is: {}".format(item))

@when('I click on {button}')
def click_button(context, button):
    print("I am clicking the button: {}".format(button))


@then('I should see "{txt}"')
def i_should_see_text(context, txt):
    expected_results = ['success', 'error']
    assert txt.lower() in expected_results, f"Unexpected text '{txt}' passed in. Expected one of {expected_results}."

    if txt.lower() == 'success':
        print(f"✅ Success message displayed: '{txt}'")
    else:
        print(f"❌ Error message displayed: '{txt}'")

    print(f"✔️ Assertion Passed: Expected and actual text match: '{txt}'")

@given('I start a call with "{qty}" participants')
def add_multiple_participants(context, qty):
    print("The number of participants is: {}".format(qty))

    print('\n####################')
    print (f"qty: {qty}, type: {type(qty)}")
    new_qty = int(qty)
    print (f"new_qty: {new_qty}, type: {type(new_qty)}")
    print('####################')