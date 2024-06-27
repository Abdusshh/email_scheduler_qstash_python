import re
from upstash_qstash import Client
from .helpers import get_env_variable

def schedule_email(email_data, delay):
    client = Client(get_env_variable("QSTASH_TOKEN"))
    client.publish_json({
        "url": "https://email-scheduler-dun.vercel.app/scheduler/send-email",  # Update with your server's URL
        "body": email_data,
        "delay": delay,
    })



# schedule email with cron job
def schedule_email_cronjob(email_data, cron_string):
    client = Client(get_env_variable("QSTASH_TOKEN"))
    schedules = client.schedules()
    response = schedules.create({
        "destination": "https://email-scheduler-dun.vercel.app/scheduler/send-email",  # Update with your server's URL
        "cron": cron_string,
        "body": email_data
    })
    return response

CRON_REGEX = re.compile(r'^(?#minute)(\*|(?:[0-9]|(?:[1-5][0-9]))(?:(?:\-[0-9]|\-(?:[1-5][0-9]))?|(?:\,(?:[0-9]|(?:[1-5][0-9])))*)) (?#hour)(\*|(?:[0-9]|1[0-9]|2[0-3])(?:(?:\-(?:[0-9]|1[0-9]|2[0-3]))?|(?:\,(?:[0-9]|1[0-9]|2[0-3]))*)) (?#day_of_month)(\*|(?:[1-9]|(?:[12][0-9])|3[01])(?:(?:\-(?:[1-9]|(?:[12][0-9])|3[01]))?|(?:\,(?:[1-9]|(?:[12][0-9])|3[01]))*)) (?#month)(\*|(?:[1-9]|1[012]|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)(?:(?:\-(?:[1-9]|1[012]|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC))?|(?:\,(?:[1-9]|1[012]|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC))*)) (?#day_of_week)(\*|(?:[0-6]|SUN|MON|TUE|WED|THU|FRI|SAT)(?:(?:\-(?:[0-6]|SUN|MON|TUE|WED|THU|FRI|SAT))?|(?:\,(?:[0-6]|SUN|MON|TUE|WED|THU|FRI|SAT))*))$')

def is_valid_cron(cron_string):
    return bool(CRON_REGEX.match(cron_string))

if __name__ == '__main__':
    email_data = {
        'to_email': 'test',
        'subject': 'test',
        'content': 'test'
    }
    cron_string = '* * * * *'
    print(schedule_email_cronjob(email_data, cron_string))
