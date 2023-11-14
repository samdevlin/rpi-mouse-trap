from gpiozero import Button

#=== GPIO config ===#
# if we need to change the input type/where it's soldered, we can do that here.
switch = Button(2)

# an array of functions to call when a press is detected
handlers = []

def listen():
    # wait_for_active function could be used to control the event loop
    return 0

def execute_handlers():
    return 0

def register_handler():
    return 0

switch.when_activated = execute_handlers