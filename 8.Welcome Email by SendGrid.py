import sendgrid
from sendgrid.helpers.mail import Email,  Mail, Content

API_KEY = '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'
SUBJECT = 'Welcome'

sg = sendgrid.SendGridAPIClient(apikey=API_KEY)

def send_email(email, name):
    BODY = 'Hi {}'.format(name)
    from_email = Email("itvisa1c@gmail.com")
    to_email = Email(email)
    subject = SUBJECT
    content = Content("text/plain", BODY)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())

    print(response.status_code)
    print(response.body)
    print(response.headers)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    send_email('itvisa1c@gmail.com', 'Some Body')
    print('Done')