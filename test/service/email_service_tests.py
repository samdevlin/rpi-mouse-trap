import unittest
from unittest.mock import patch

from service.email_service import add_recipient, notify, _isValidEmail, _sendEmails
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
    @patch('service.email_service._sendEmail')
    def test_email_sent(self, send_email_mock):
        send_email_mock.return_value = True
        add_recipient(VALID_EMAIL)
        result = notify()

        self.assertEqual(send_email_mock.call_count, 1)
        self.assertEqual(result, { VALID_EMAIL : True })

class TestFailureCases(unittest.TestCase):
    def test_invalid_recipient(self):
        with self.assertRaises(InvalidEmailError):
            add_recipient(INVALID_EMAIL)

    def test_no_recipients(self):
        with self.assertRaises(NoRecipientsError):
            notify()

if __name__ == '__main__':
    unittest.main()