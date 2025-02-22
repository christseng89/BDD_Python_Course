from behave import then, when, given
from BDDCommon.CommonConfigs.locatorsconfig import ORDER_RECEIVED_LOCATORS
from BDDCommon.CommonFuncs import webcommon
import time

@then("order received page should load with correct data")
def order_received_page_should_load_with_correct_data(context):

    print("\nWaiting for 15 seconds for the order to be processed...")
    time.sleep(15)
    print ("✅ Order receive page check ...")
    context.execute_steps("""
        then Order received heading should be displayed
        then Thank you message should be displayed
        then Verify order number and label displayed
    """)
    print ("✅ Order received page loaded with correct data successfully")

@then("Order received heading should be displayed")
def order_received_heading_should_be_displayed(context):
    # time.sleep(2)

    header_locator = ORDER_RECEIVED_LOCATORS['page_header']
    webcommon.assert_element_contains_text(context, 'Order received', header_locator['type'], header_locator['locator'])
    print ("  ✅ Order received heading displayed successfully")


@then("Thank you message should be displayed")
def thank_you_message_should_be_displayed(context):

    # time.sleep(2)
    header_locator = ORDER_RECEIVED_LOCATORS['page_header']
    webcommon.assert_element_contains_text(context, 'Order received', header_locator['type'], header_locator['locator'])
    print ("  ✅ Thank you message displayed successfully")

@then("Verify order number and label displayed")
def verify_order_number_and_label_displayed(context):

    order_detail_locator = ORDER_RECEIVED_LOCATORS['order_details_order']
    elm = webcommon.find_element(context, order_detail_locator['type'], order_detail_locator['locator'])
    order_text = elm.text
    order_text_list = order_text.split('\n')
    label = order_text_list[0]
    order_id = order_text_list[1]

    assert label == 'ORDER NUMBER:', f"'Order received' page the label for order number is not correct. Expected 'ORDER NUMBER:' actual {label}"
    assert order_id.isnumeric(), f"'Order received' page the order id is not numeric. Actual: {order_id}"

    context.order_id = order_id
    print ("  ✅ Order number verified successfully")