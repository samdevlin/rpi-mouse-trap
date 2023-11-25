from gpiozero import Button

# === GPIO config ===#
# if we need to change the input type/where it's soldered, we can do that here.
# TODO - uncomment when connected to PI
# switch = Button(2)
switch = None

# a set of functions to call when a press is detected
handlers = set()


def listen():
    # wait_for_active function could be used to control the event loop
    raise NotImplementedError


def execute_handlers():
    for handler in handlers:
        handler()


def register_handler(handler):
    if not callable(handler):
        raise TypeError('Handler must be a function - please pass a function instead.')

    handlers.add(handler)
    return handlers

# TODO - uncomment when connected to PI
# switch.when_activated = execute_handlers
