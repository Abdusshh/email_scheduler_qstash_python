from upstash_qstash import Client
from .helpers import get_env_variable

def schedule_email(email_data, delay):
    client = Client(get_env_variable("QSTASH_TOKEN"))
    client.publish_json({
        "url": "https://firstqstashmessage.requestcatcher.com/",  # Update with your server's URL
        "body": email_data,
        "delay": delay,
    })
