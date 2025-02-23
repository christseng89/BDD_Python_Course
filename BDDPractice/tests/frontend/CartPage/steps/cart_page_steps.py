from behave import then, when, given
from BDDCommon.CommonConfigs.locatorsconfig import CART_PAGE_LOCATORS
from BDDCommon.CommonFuncs import webcommon
import logging as logger
import time

@when("I click on 'Proceed to Checkout' button in the cart page")
def i_click_on_proceed_to_checkout_button_in_the_cart_page(context):
    """

    """
    proceed_button = CART_PAGE_LOCATORS['proceed_to_checkout_btn']

    max_try = 3
    try_count = 0
    while try_count < max_try:
        try:
            webcommon.click(context, proceed_button['type'], proceed_button['locator'])
            break
        except Exception as e:
            try_count += 1
            print(f"Failed to click on 'Proceed to checkout' Retry number: {try_count}")
    else:
        raise Exception(f"Failed to click on 'Proceed to checkout' after retrying '{max_try}' times.")
    
    logger.info("✅ Clicked on 'Proceed to checkout' button in the cart page")
    print("✅ Clicked on 'Proceed to checkout' button in the cart page")

@when("I get the total dollar amount of the cart")
def i_get_the_total_dollar_amount_of_the_cart(context):
    time.sleep(2)
    total_locator = CART_PAGE_LOCATORS['total_cart_value']

    total_raw = webcommon.get_element_text(context, total_locator['type'], total_locator['locator'])
    context.cart_total = total_raw.replace('$', '')

    print(f"✅ Cart total amount: {context.cart_total}")


@when("I apply the coupon to the cart")
def i_apply_the_coupon_to_the_cart(context):
    print(f"✅ Applying coupon code: {context.coupon_code} starts...")

    # Retrieve the 'Add a coupon' button using webcommon.find_element.
    add_a_coupon_locator = CART_PAGE_LOCATORS['add_a_coupon_button']
    dropdown = webcommon.find_element(context, add_a_coupon_locator['type'], add_a_coupon_locator['locator'])

    # Scroll the element into view if needed.
    context.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)

    # Click the 'Add a coupon' button using webcommon.click.
    webcommon.click(context, add_a_coupon_locator['type'], add_a_coupon_locator['locator'])
    print("  ✅ Clicked on 'Add a coupon' button")

    # Enter the coupon code in the input field.
    coupon_field_locator = CART_PAGE_LOCATORS['coupon_code_field']
    webcommon.type_into_element(context, context.coupon_code,
                                coupon_field_locator['type'],
                                coupon_field_locator['locator'])
    print(f"  ✅ Entered coupon {context.coupon_code}")

    # Click the 'Apply coupon' button.
    apply_coupon_locator = CART_PAGE_LOCATORS['apply_coupon_button']
    webcommon.click(context, apply_coupon_locator['type'], apply_coupon_locator['locator'])
    print("  ✅ Clicked on 'Apply coupon' button")

    print(f"✅ Applied coupon code: {context.coupon_code} successfully")


import math
@then("the total should be reduced by {pct}%")
def the_total_should_be_reduced_by_pct(context, pct):
    original_total = context.cart_total

    # Apply the discount percentage and round to the nearest whole number
    expected_new_total = math.ceil(float(original_total) * (1 - float(pct) / 100))

    # Recalculate the total after applying the coupon
    context.execute_steps("when I get the total dollar amount of the cart")
    new_total = context.cart_total

    assert float(new_total) == expected_new_total, \
        f"❌ Cart total after applying {pct}% coupon is not as expected. " \
        f"Original: {original_total}, Expected: {expected_new_total}, Actual: {new_total}"

    print(f"✅ Cart total {original_total} correctly reduced by {pct}% to {new_total}.")
