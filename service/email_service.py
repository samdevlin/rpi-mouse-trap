import re, smtplib
from email.mime.text import MIMEText
from util.error.InvalidEmailError import InvalidEmailError
from util.error.NoRecipientsError import NoRecipientsError

EMAIL_REGEX = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
recipient_list = []

#=== GMAIL ACCOUNT DETAILS ===#
# TODO: move this to a config file
SENDER_USERNAME = 'ratsout.notification'
SENDER_APP_KEY = ''

def add_recipient(email_addr):
    if _isValidEmail(email_addr) is None:
        raise InvalidEmailError("Could not validate the recipient's email address")

    recipient_list.append(email_addr)
    return recipient_list

def notify():
    if not recipient_list:
        raise NoRecipientsError("No email recipients found. Could not notify via email.")

    _sendEmails()

def _isValidEmail(email):
    return re.fullmatch(EMAIL_REGEX, email)

def _sendEmails():

    # Message Configuration
    msg = MIMEText("Here there's a mouse in the attic ye")
    msg["Subject"] = "You've got mouse"
    msg["Bcc"] = ", ".join(recipient_list)
    msg["From"] = f"{SENDER_USERNAME}@gmail.com"

    # SMTP Config/Execution
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(SENDER_USERNAME, SENDER_APP_KEY)
    try:
        smtp_server.send_message(msg)
    except Exception as err:
        print(f"An unexpected error of type {type(err)} occurred: {err}")
    finally:
        smtp_server.quit()
