import sendgrid
from sendgrid.helpers.mail import Email,  Mail, Content

API_KEY = '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'
SUBJECT = 'Welcome asdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
BODY = 'Hi {}'

sg = sendgrid.SendGridAPIClient(apikey=API_KEY)

def send_email(email, name):
    pass

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    send_email('somebody@gmail.com', 'Some Body')
    print('Done')