import unittest
from unittest.mock import patch

from service.email_service import add_recipient, notify, _is_valid_email
from util.error.InvalidEmailError import InvalidEmailError
from util.error.NoRecipientsError import NoRecipientsError

VALID_EMAIL = "samplemail@mail.com"
INVALID_EMAIL = "some string"


class TestSuccessCases(unittest.TestCase):
    def test_can_add_recipient(self):
        self.assertEqual(add_recipient(VALID_EMAIL), [VALID_EMAIL])

    @patch('service.email_service._send_emails')
    def test_can_notify_recipients(self, send_email_mock):
        notify()
        self.assertEqual(send_email_mock.call_count, 1)

    def test_valid_email(self):
        self.assertNotEqual(_is_valid_email(VALID_EMAIL), None)

    @patch('service.email_service._send_emails')
    def test_email_sent(self, send_email_mock):
        add_recipient(VALID_EMAIL)
        notify()
        self.assertEqual(send_email_mock.call_count, 1)


class TestFailureCases(unittest.TestCase):
    def test_invalid_recipient(self):
        with self.assertRaises(InvalidEmailError):
            add_recipient(INVALID_EMAIL)

    def test_no_recipients(self):
        with self.assertRaises(NoRecipientsError):
            notify()


if __name__ == '__main__':
    unittest.main()
