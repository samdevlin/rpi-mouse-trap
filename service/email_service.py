import re, smtplib, os
from email.mime.text import MIMEText

from errors import InvalidEmailError, NoRecipientsError

EMAIL_REGEX = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
recipient_list = []

# === GMAIL ACCOUNT DETAILS ===#
SENDER_USERNAME = os.getenv('username')
SENDER_APP_KEY = os.getenv('app_key')


def add_recipient(email_addr):
    if _is_valid_email(email_addr) is None:
        raise InvalidEmailError("Could not validate the recipient's email address")

    recipient_list.append(email_addr)
    return recipient_list


def notify():
    if not recipient_list:
        raise NoRecipientsError("No email recipients found. Could not notify via email.")

    _send_emails()


def _is_valid_email(email):
    return re.fullmatch(EMAIL_REGEX, email)


def _send_emails():
    # Message Configuration
    msg = MIMEText("Here there's a mouse in the attic ye")
    msg["Subject"] = "You've got mouse"
    msg["Bcc"] = ", ".join(recipient_list)
    msg["From"] = f"{SENDER_USERNAME}@gmail.com"

    # SMTP Config/Execution
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    try:
        smtp_server.login(SENDER_USERNAME, SENDER_APP_KEY)
        smtp_server.send_message(msg)
    # TODO: catch timeout
    except Exception as err:
        print(f"An unexpected error of type {type(err)} occurred: {err}")
    finally:
        smtp_server.quit()
