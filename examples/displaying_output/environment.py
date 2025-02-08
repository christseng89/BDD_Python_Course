import logging
import sys
import io

# Custom log filter to modify log names
class CustomLogFilter(logging.Filter):
    def filter(self, record):
        if record.name == "root":
            record.name = "info"  # Change 'root' to 'info'
        elif record.name == "print":
            record.name = "print"  # Ensure print logs show correctly
        return True

# Configure logger with custom filter and formatter
log_formatter = logging.Formatter("\t%(levelname)s:%(name)s: %(message)s")
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("root")  # Main logger
logger.addFilter(CustomLogFilter())

# Separate logger for print() statements
print_logger = logging.getLogger("print")
print_logger.setLevel(logging.INFO)
print_logger.addFilter(CustomLogFilter())

# Ensure handlers use the correct formatter
for handler in logging.getLogger().handlers:
    handler.setFormatter(log_formatter)

# https://behave.readthedocs.io/en/stable/behave.html
def before_all(context):
    """Disables Behave's built-in capturing to remove 'Captured stdout' and 'Captured logging'."""
    context.config.stdout_capture = False
    context.config.stderr_capture = False
    context.config.log_capture = False

def before_step(context, step):
    """Stores the current step name inside context and redirects stdout."""
    context.step_name = f"{step.keyword} {step.name}"
    context.stdout_buffer = io.StringIO()  # Capture print output
    context.original_stdout = sys.stdout
    sys.stdout = context.stdout_buffer  # Redirect stdout

def after_step(context, step):
    """Restores stdout, logs captured print output as 'PRINT', and prints a blank line."""
    sys.stdout = context.original_stdout  # Restore stdout
    captured_output = context.stdout_buffer.getvalue().strip()
    context.stdout_buffer.close()

    # Log print output as 'PRINT' and immediately print it
    if captured_output:
        for line in captured_output.split("\n"):
            print_logger.info(line)  # Log each print() statement
            # print(f"\tprint: {line}")  # Ensure it appears in real-time
