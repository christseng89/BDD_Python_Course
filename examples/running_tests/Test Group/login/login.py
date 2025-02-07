from behave import then

@then("I am in a Python file in the subdirectory")
def in_another_py(context):
    print("I am in a Python file in the subdirectory")
    pass