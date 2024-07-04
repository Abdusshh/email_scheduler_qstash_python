from upstash_qstash import Client
from .helpers import get_env_variable

def schedule_email(email_data, delay):
    client = Client(get_env_variable("QSTASH_TOKEN"))
    client.publish_json({
        "url": get_env_variable("DEPLOYED_URL"),
        "body": email_data,
        "delay": delay,
    })


# schedule email with cron job
def schedule_email_cronjob(email_data, cron_string):
    client = Client(get_env_variable("QSTASH_TOKEN"))
    schedules = client.schedules()
    response = schedules.create({
        "destination": get_env_variable("DEPLOYED_URL"),
        "cron": cron_string,
        "body": email_data
    })
    return response
