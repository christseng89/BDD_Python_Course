# environment.py
def before_step(context, step):
    context.current_step = step.name