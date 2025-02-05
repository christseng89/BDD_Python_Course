from behave import given, when, then, step


import pdb
import json


@step("I am a passing step")
def i_am_a_passing_steps(context):
    print("1ST PASS")
    print("1ST PASS")
    print("1ST PASS")
    step_text = context.text
    # pdb.set_trace()


@step("I another a passing step")
def i_another_a_passing_step(context):
    print("Another PASSING")
    print("Another PASSING")
    print("Another PASSING")
    my_json = json.loads(context.text)
    # pdb.set_trace()



@step("I am a failing step")
def i_am_a_failing_step(context):
    print("")
    print("Step FAILING")
    print("Step FAILING")
    print("Step FAILING")
    print("Step FAILING")
    raise Exception("Failing on purpose")

