# Created by samfi at 2025/2/6
from behave import given, when, then

# Background steps
@given('Background given step')
def background_given_step(context):
    pass

@when('Background when step')
def background_when_step(context):
    pass

# Scenario 1 steps
@given('Scenario1 given step')
def scenario1_given_step(context):
    pass

@when('Scenario1 when step')
def scenario1_when_step(context):
    pass

@when('Scenario1 when and step 1')
def scenario1_when_and_step1(context):
    pass

@when('Scenario1 when and step 2')
def scenario1_when_and_step2(context):
    pass

@when('Scenario1 but step')
def scenario1_but_step(context):
    pass

@then('Scenario1 then step 1')
def scenario1_then_step1(context):
    pass

@then('Scenario1 then step 2')
def scenario1_then_step2(context):
    pass

@then('Scenario1 then and step 1')
def scenario1_then_and_step1(context):
    pass

@then('Scenario1 then and step 2')
def scenario1_then_and_step2(context):
    pass

@then('Scenario1 then but step')
def scenario1_then_but_step(context):
    pass

# Scenario 2 steps
@given('Scenario2 given step')
def scenario2_given_step(context):
    pass

@when('Scenario2 when step')
def scenario2_when_step(context):
    pass

@when('Scenario2 when and step 1')
def scenario2_when_and_step1(context):
    pass

@when('Scenario2 when and step 2')
def scenario2_when_and_step2(context):
    pass

@when('Scenario2 but step')
def scenario2_but_step(context):
    pass

@then('Scenario2 then step 1')
def scenario2_then_step1(context):
    pass

@then('Scenario2 then step 2')
def scenario2_then_step2(context):
    pass

@then('Scenario2 then and step 1')
def scenario2_then_and_step1(context):
    pass

@then('Scenario2 then and step 2')
def scenario2_then_and_step2(context):
    pass

@then('Scenario2 then but step')
def scenario2_then_but_step(context):
    pass

# Scenario Outline reuses Scenario1 Steps
