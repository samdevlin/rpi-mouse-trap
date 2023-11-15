import re, smtplib
from util.error.InvalidEmailError import InvalidEmailError
from util.error.NoRecipientsError import NoRecipientsError

EMAIL_REGEX = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
recipient_list = []

#=== GMAIL ACCOUNT DETAILS ===#
# TODO: move this to a config file
SENDER_ADDRESS = 'ratsout.notification@gmail.com'
SENDER_APP_KEY = ''

def add_recipient(email_addr):
    if _isValidEmail(email_addr) is None:
        raise InvalidEmailError("Could not validate the recipient's email address")

    recipient_list.append(email_addr)
    return recipient_list

def notify():
    if not recipient_list:
        raise NoRecipientsError("No email recipients found. Could not notify via email.")

    sent = {}

    for recipient in recipient_list:
        sent[recipient] = _sendEmail(recipient)

    return sent

def _isValidEmail(email):
    return re.fullmatch(EMAIL_REGEX, email)

def _sendEmail(recipient):
    raise NotImplementedError