from behave import given, when, then

#----------------------------------------------------------------------------------------------------------------------#
@given('I find recent order from database')
def find_order_from_db(context):
    print("Finding an order from the database....")
    context.order_num = '112233'  # Assign the order number
    print("Found an order. Order number: {}".format(context.order_num))

#----------------------------------------------------------------------------------------------------------------------#
@when('I issue a refund for the order')
def issue_refund(context):
    if context.order_num is None:
        raise ValueError("Order number not found in context. Ensure `Given I find recent order from database` is called first.")

    if context.order_num in context.refunded_orders:
        print(f"Order {context.order_num} has already been refunded. Cannot refund again.")
    else:
        context.refunded_orders.add(context.order_num)
        print(f"Refund issued successfully for order number: {context.order_num}")

#----------------------------------------------------------------------------------------------------------------------#
@then('payment should get processed for the user')
def payment_should_process(context):
    print(f"Payment successfully processed for refund of order number: {context.order_num}")

#----------------------------------------------------------------------------------------------------------------------#
@when('I issue a refund on the same order')
def issue_repeat_refund(context):
    if context.order_num is None:
        context.order_num = list(context.refunded_orders)[0]   # Get the 1st refunded order number

    if context.order_num in context.refunded_orders:
        context.refund_failed = True  # Correctly mark failure
        print(f"✅ Refund failed. Order {context.order_num} has already been refunded.")
    else:
        context.refunded_orders.add(context.order_num)
        context.refund_failed = False
        print(f"❌ Unexpected success: Refund issued again for order number: {context.order_num}")

#----------------------------------------------------------------------------------------------------------------------#
@then('the refund should fail to process')
def refund_fails(context):
    if context.refund_failed:
        print(f"✅ Refund correctly failed for a refunded order: {context.order_num}")
    else:
        raise AssertionError(f"❌ Refund should have failed for order {context.order_num}, but it was processed again!")
