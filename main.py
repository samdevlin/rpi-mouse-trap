from util.config_loader import load_section_to_env
from service.input_service import register_handler, listen
from service.email_service import notify, add_recipient


def run():
    # configure email stuff
    load_section_to_env('EMAIL')

    # Add your recipients here
    # add_recipient('someperson@example.com')

    register_handler(notify)
    listen()


if __name__ == '__main__':
    run()
