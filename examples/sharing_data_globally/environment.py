# environment.py
def before_all(context):
    """Initialize global variables before all scenarios"""
    context.refunded_orders = set()  # Ensure refund tracking persists

def before_scenario(context, scenario):
    """Reset per-scenario variables"""
    context.order_num = None  # Reset order number at the start of each scenario
    context.refund_failed = False  # Ensure refund status is reset
