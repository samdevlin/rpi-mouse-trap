import unittest
from service.email_service import add_recipient, notify, _isValidEmail
from util.error.InvalidEmailError import InvalidEmailError
from util.error.NoRecipientsError import NoRecipientsError

VALID_EMAIL = "samplemail@mail.com"
INVALID_EMAIL = "somestring"
class TestSuccessCases(unittest.TestCase):
    def test_can_add_recipient(self):
        self.assertEqual(add_recipient(VALID_EMAIL), [ VALID_EMAIL ])

    def test_can_notify_recipients(self):
        self.assertEqual(notify(), True)

    def test_valid_email(self):
        self.assertNotEqual(_isValidEmail(VALID_EMAIL), None)

class TestFailureCases(unittest.TestCase):
    def test_invalid_recipient(self):
        with self.assertRaises(InvalidEmailError):
            add_recipient(INVALID_EMAIL)

    def test_no_recipients(self):
        with self.assertRaises(NoRecipientsError):
            notify()

if __name__ == '__main__':
    unittest.main()