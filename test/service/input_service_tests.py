import unittest
from service.input_service import register_handler


class TestSuccessCases(unittest.TestCase):
    def test_can_register_handler(self):
        def my_mock_function():
            return 0

        self.assertEqual(register_handler(my_mock_function), {my_mock_function})


class TestFailureCases(unittest.TestCase):
    def test_cant_register_unsupported_handler_type(self):
        with self.assertRaises(TypeError):
            register_handler('my_mock_function')


if __name__ == '__main__':
    unittest.main()
