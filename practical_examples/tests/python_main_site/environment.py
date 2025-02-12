def after_scenario(context, scenario):
    """Closes the browser after each scenario."""
    if hasattr(context, "driver"):
        context.driver.quit()
