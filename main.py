import os

import schedule
import time
from twilio.rest import Client
from datetime import datetime
from pprint import pprint
from triviagenerator import TriviaGenerator
from imggen import ImgGen

current_date = datetime.now().strftime('%B %d')

prompt = f'Present a historical fact that happened on {current_date}.' \
         'Start it off with, "On this day, February 2 in *year this fact takes place*"' \
         ' as the header and end with a short paragraph describing the event.'

trivia = TriviaGenerator()
trivia.set_prompt(prompt)
trivia.generate_text()

img = ImgGen(trivia.trivia_text)





account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


def send_message():
    client.messages \
                .create(
                     body=f"{trivia.trivia_text}",
                     from_='+15074797617',
                     media_url=img.output,
                     to='+17788855315'
                 )

send_message()
# schedule.every().day.at('20:55').do(send_message)
# while True:
#     schedule.run_pending()
#     time.sleep(1)


