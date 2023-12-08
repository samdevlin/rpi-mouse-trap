# RPi4 Humane Mouse Trap
Software to run a humane mouse trap, written and built in Python 3.8 on a Raspberry Pi 4.

## Development Setup
1. Clone this repository to your local machine.
2. cd to the cloned directory and [intialise a venv](https://docs.python.org/3/library/venv.html) by running the command below
```bash
  python -m venv ./venv
```
3. Use this venv while developing. You can activate the venv using the command below.
```bash
  # mac/linux
  source ./venv/bin/activate

  # windows
  venv\Scripts\activate.bat
```
4. Install the dependencies from the requirements.txt file using pip.
```bash
  pip install gpiozero
  pip install pigpio
  pip install RPi.GPIO
```
5. Start the service
```bash
  python main.py
```

## Using the service
The ```input_service.py``` file defines the configuration for the Raspberry Pi GPIO and executes "handlers" when an input is detected. It is currently configured to read button input from the GPIO18 pin, and call an email handler on button press. 
To test this functionality, you will have to:
1. Wire up a Pi4 with the button at GPIO18 (or change the value in ```input_service.py``` to read from another pin)
2. Add a recipient email address in ```main.py```
3. Add a valid gmail username/app key to act as the sender. [More information on app keys can be found here](https://knowledge.workspace.google.com/kb/how-to-generate-an-app-passwords-000009237?hl=en).
4. Start the service & press the button!

## Extensibility
This service was built with some extensibility in mind. For example, if you also wanted to publish an event to a messaging queue on button press, you would simply write a function to publish a suitable message and register that function as a handler, as shown in ```main.py#run()```. This pattern also confines the configuration details of the service to main.py.  

If this service were to grow in size, an OOP approach could also be considered in which handlers could inherit from a base class & implement their own handler function to be executed when the base class detects input.
