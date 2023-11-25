import unittest
from unittest.mock import MagicMock
from service.input_service import register_handler, execute_handlers


class TestSuccessCases(unittest.TestCase):
    my_mock_function = MagicMock(return_value=print('mock function called'))

    def test_can_register_handler(self):
        self.assertEqual(register_handler(self.my_mock_function), {self.my_mock_function})

    def test_handler_is_executed(self):
        register_handler(self.my_mock_function)
        execute_handlers()
        self.my_mock_function.assert_called_once()


class TestFailureCases(unittest.TestCase):
    def test_cant_register_unsupported_handler_type(self):
        with self.assertRaises(TypeError):
            register_handler('my_mock_function')

    def test_no_handlers(self):
        execute_handlers()


if __name__ == '__main__':
    unittest.main()
