import os
import openai
import replicate
import schedule
import time
from twilio.rest import Client
from datetime import datetime
from pprint import pprint

current_date = datetime.now().strftime('%B %d')
current_time = datetime.now().strftime("%H:%M")

openai.api_key = os.environ.get('openai_key')
prompt = f'Present a historical fact that happened on {current_date}.' \
         'Start it off with, "On this day, February 2 in *year this fact takes place*"' \
         ' as the header and end with a short paragraph describing the event.'



response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=500)
open_ai_output = response['choices'][0]['text']
prompt_first_sentence = open_ai_output.split('.', 1)[0]


model = replicate.models.get("stability-ai/stable-diffusion")
version = model.versions.get("db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf")

inputs = {
    'prompt': f'{prompt_first_sentence}',
    'image_dimensions': "768x768",
    'num_outputs': 1,
    'num_inference_steps': 50,
    'guidance_scale': 7.5,
    'scheduler': "DPMSolverMultistep",
}

output = version.predict(**inputs)


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


def send_message():
    client.messages \
                .create(
                     body=f"{open_ai_output}",
                     from_='+15074797617',
                     media_url=output,
                     to='+17788855315'
                 )


schedule.every().day.at('20:55').do(send_message)
while True:
    schedule.run_pending()
    time.sleep(1)


