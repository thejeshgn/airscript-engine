import os

# this should operate more like webscript
# and work with non-sendgrid smtp, but for
# now we will assume sendgrid and use api
import requests

# TODO: not fully impelmented, see 
# https://www.webscript.io/documentation#email

def send(T):
    url = "https://sendgrid.com/api/mail.send.json"
    params = {
        'api_user': os.environ.get('SENDGRID_USERNAME'),
        'api_key': os.environ.get('SENDGRID_PASSWORD'),
        'to': T['to'],
        'subject': T['subject'],
        'text': T['text'],
        'from': T['from'],
    }
    requests.post(url, params=params)


