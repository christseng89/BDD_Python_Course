from behave import given, when, then, step


import pdb
import json


@step("I am a passing step")
def i_am_a_passing_steps(context):
    print("1ST PASS 1")
    print("1ST PASS 2")
    print("1ST PASS 3")
    # step_text = context.text
    print(f"Context text:\n{context.text}")
    if context.text != None:
        pdb.set_trace()


@step("I another a passing step")
def i_another_a_passing_step(context):
    print("Another PASSING 1")
    print("Another PASSING 2")
    print("Another PASSING 3")

    my_json = json.loads(context.text)
    print(f"Context text:\n{context.text}")
    print(f"✅ Context text Json: {my_json}")
    print(f"✅ First name: {my_json['first_name']}")
    if context.text != None:
        pdb.set_trace()


@step("I am a failing step")
def i_am_a_failing_step(context):

    print("Step FAILING 1")
    print("Step FAILING 2")
    print("Step FAILING 3")
    print("Step FAILING 4")

    # Simulate step failure
    raise Exception("❌ Failing on purpose")
