
from datetime import datetime
from generators.triviagenerator import TriviaGenerator
from generators.imggen import ImgGen
from scripts.textsender import TextSender
import schedule
import time

current_date = datetime.now().strftime('%B %d')

prompt = f'Present a historical fact that happened on {current_date}.' \
         'Start it off with, "On this day, February 2 in *year this fact takes place*"' \
         ' as the header and end with a short paragraph describing the event.'

if __name__ == '__main__':
    trivia = TriviaGenerator()
    trivia.set_prompt(prompt)
    trivia.generate_text()

    img = ImgGen(trivia.shortened_trivia)

    textsender = TextSender()

    schedule.every().day.at('18:06').do(textsender.send_message, text_input=trivia.trivia_text, img_input=img.output)
    while True:
        schedule.run_pending()
        time.sleep(1)






