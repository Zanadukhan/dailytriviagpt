import os
import time
from twilio.rest import Client
from generators.triviagenerator import TriviaGenerator

class TextSender:
    def __init__(self):
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.client = Client(account_sid, auth_token)

    def send_message(self, text_input, img_input):
            self.client.messages.create(body=text_input,
                                        from_='TWILIO_PHONE_NUMBER',
                                        media_url=img_input,
                                        to='YOUR_PHONE_NUMBER')
