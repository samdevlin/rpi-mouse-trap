from gpiozero import Button

# === GPIO config ===#
# if we need to change the input type/where it's soldered, we can do that here.
button = Button(18)

# a set of functions to call when a press is detected
handlers = set()


def listen():
    print('Listening..')
    while True:
        button.wait_for_active()
        print('Button was pressed! Executing handlers..')
        execute_handlers()


def execute_handlers():
    for handler in handlers:
        handler()


def register_handler(handler):
    if not callable(handler):
        raise TypeError('Handler must be a function - please pass a function instead.')

    handlers.add(handler)
    return handlers
