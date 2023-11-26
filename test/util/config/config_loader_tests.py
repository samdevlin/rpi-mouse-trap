import unittest, os
from util.config_loader import load_section_to_env


class TestSuccessCases(unittest.TestCase):
    def test_config_is_loaded(self):
        load_section_to_env('TEST')
        self.assertEqual(os.environ['username'], 'test_user')
        self.assertEqual(os.environ['app_key'], 'test_key')


if __name__ == '__main__':
    unittest.main()
