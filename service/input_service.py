from gpiozero import Button

#=== GPIO config ===#
# if we need to change the input type/where it's soldered, we can do that here.
switch = Button(2)

# an array of functions to call when a press is detected
handlers = []

def listen():
    # wait_for_active function could be used to control the event loop
    raise NotImplementedError

def execute_handlers():
    raise NotImplementedError

def register_handler():
    raise NotImplementedError

switch.when_activated = execute_handlers