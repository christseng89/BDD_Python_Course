from behave import given, when, then, step

# Background steps
given("Background given step")(lambda context: print("Executing Background Given Step"))
when("Background when step")(lambda context: print("Executing Background When Step"))

# Scenario1 steps
@given("Scenario1 given step 1")
def step_impl(context):
    print("Executing Scenario1 Given Step 1")

@given("Scenario1 given step 2")
def step_impl(context):
    print("Executing Scenario1 Given Step 2")

@when("Scenario1 when step 1")
def step_impl(context):
    print("Executing Scenario1 When Step 1")

@when("Scenario1 when step 2")
def step_impl(context):
    print("Executing Scenario1 When Step 2")

@when("Scenario1 when step 3")
def step_impl(context):
    print("Executing Scenario1 When Step 3")

@when("Scenario1 when but step")
def step_impl(context):
    print("Executing Scenario1 When But Step")

@then("Scenario1 then step 1")
def step_impl(context):
    print("Executing Scenario1 Then Step 1")

@then("Scenario1 then step 2")
def step_impl(context):
    print("Executing Scenario1 Then Step 2")

@then("Scenario1 then step 3")
def step_impl(context):
    print("Executing Scenario1 Then Step 3")

@then("Scenario1 then step 4")
def step_impl(context):
    print("Executing Scenario1 Then Step 4")

@then("Scenario1 then but step")
def step_impl(context):
    print("Executing Scenario1 Then But Step")

# Scenario2 steps
@given("Scenario2 given step 1")
def step_impl(context):
    print("Executing Scenario2 Given Step 1")

@given("Scenario2 given step 2")
def step_impl(context):
    print("Executing Scenario2 Given Step 2")

@when("Scenario2 when step 1")
def step_impl(context):
    print("Executing Scenario2 When Step 1")

@when("Scenario2 when step 2")
def step_impl(context):
    print("Executing Scenario2 When Step 2")

@when("Scenario2 when step 3")
def step_impl(context):
    print("Executing Scenario2 When Step 3")

@when("Scenario2 when but step")
def step_impl(context):
    print("Executing Scenario2 When But Step")

@then("Scenario2 then step 1")
def step_impl(context):
    print("Executing Scenario2 Then Step 1")

@then("Scenario2 then step 2")
def step_impl(context):
    print("Executing Scenario2 Then Step 2")

@then("Scenario2 then step 3")
def step_impl(context):
    print("Executing Scenario2 Then Step 3")

@then("Scenario2 then step 4")
def step_impl(context):
    print("Executing Scenario2 Then Step 4")

@then("Scenario2 then but step")
def step_impl(context):
    print("Executing Scenario2 Then But Step")

# Scenario1 Outline steps (Reusing Scenario1 steps)
