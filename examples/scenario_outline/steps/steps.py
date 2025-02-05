

from behave import given, when, then


@given("I login as a new user")
def login_as_new_user(context):

    print("I am logged in as a new user. ")


@when('I add a "{state}" shipping address')
def add_shipping_address(context, state):

    print('Adding address in state: {}'.format(state))


@given("I have {quantity} items in my cart")
def add_items_to_cart(context, quantity):

    print('Adding {} items to the cart'.format(quantity))
    print('I am the logic to add {} items to cart'.format(quantity))


@when("I checkout using \"{payment}\"")
def checkout(context, payment):

    if payment.lower() == 'credit card':
        print("logic to use credit cart")
        print("I am using VISA")

    elif payment.lower() == 'gift card':
        print("I will use gift card")
        print("I love gift cards")

    else:
        raise Exception("The passed in parameter for payment is in not one of expected. Actual: {act}, "
                        "Expected: {exp}".format(act=payment, exp=['credit card', 'gift card']))

@then("my order should be placed")
def verify_order_placed(context):

    print("I am checking my order is placed")
    print("Yey my order is success :) ")

@when("I add a $40 book to the cart")
def add_book_to_cart(context):
    pass

@then("tax should be calculated")
def tax_should_calculate(context):
    pass

