from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from .helpers import get_env_variable

def send_email(to_email, subject, content):
    message = Mail(
        from_email=get_env_variable('SENDGRID_SENDER_EMAIL_ADDRESS'),
        to_emails=to_email,
        subject=subject,
        plain_text_content=content)
    try:
        sg = SendGridAPIClient(get_env_variable('SENDGRID_API_KEY'))
        response = sg.send(message)
        print("RESPONSE INFO")
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
