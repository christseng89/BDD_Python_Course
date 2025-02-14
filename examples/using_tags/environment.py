# environment.py
def before_step(context, step):
    context.current_step = step.name

def before_tag(context, tag):
    context.current_tag = tag