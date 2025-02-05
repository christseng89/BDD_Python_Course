
from behave import given, when, then

#----------------------------------------------------------------------------------------------------------------------#
@given('I find recent order from database')
def find_order_from_db(context):

    print("Finding an order from the database....")
    context.order_num = '112233'

    print("Found an orders. Order number: {}".format(context.order_num))

#----------------------------------------------------------------------------------------------------------------------#
@when('I issue a refund for the order')
def issue_refund(context):

    print("Trying to issue a refund for order number: {}".format(context.order_num))

#----------------------------------------------------------------------------------------------------------------------#
@then('payment should get processed for the user')
def payment_should_process(context):

    print("Payment successfully processed")
    print("Payment is for refund of order number: {}".format(context.order_num))

#----------------------------------------------------------------------------------------------------------------------#
@when('I issue a refund on the same order')
def issue_repeat_refund(context):

    print("Trying to issue refund on same order: {}".format(context.order_num))

#----------------------------------------------------------------------------------------------------------------------#
@then('the refund should fail to process')
def refund_fails(context):

    print("The refund for order {} should vail.".format(context.order_num))