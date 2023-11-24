from util.config.config_loader import load_section_to_env
from service.input_service import register_handler, listen


def run():
    load_section_to_env('EMAIL')
    # TODO: register the handler here
    listen()


if __name__ == '__main__':
    run()
