from util.config_loader import load_section_to_env
from service.input_service import register_handler, listen
from service.email_service import notify


def run():
    # configure email stuff
    load_section_to_env('EMAIL')

    register_handler(notify)
    listen()


if __name__ == '__main__':
    run()
