from apscheduler.schedulers.blocking import BlockingScheduler
import os

def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print("successfully sent the mail")
    except Exception as inst:
        print(inst)

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
	send_email(os.environ["gmailUser"], os.environ["gmailPassword"],
			'rishabhranawat12345@gmail.com', 'testing cron job', 'hey rish')
	print('This job is run every three minutes.')

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

@sched.scheduled_job('cron', day_of_week='sun', hour=17, minute=48)
def scheduled_email():
	send_email(os.environ["gmailUser"], os.environ["gmailPassword"],
			'rishabhranawat12345@gmail.com', 'testing cron job', 'hey rish')

sched.start()
