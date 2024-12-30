import openai
import os

class TriviaGenerator():


    def __init__(self):
        self.prompt = ''
        self.trivia_text = ''
        openai.api_key = os.environ.get('openai_key')
        self.shortened_trivia = ''

    def set_prompt(self, prompt):
        self.prompt = prompt

    def generate_text(self):
        response = openai.Completion.create(model="text-davinci-003", prompt=self.prompt, temperature=0, max_tokens=500)
        open_ai_output = response['choices'][0]['text']
        self.trivia_text = open_ai_output
        self.shortened_trivia = open_ai_output.split('.', 1)[0]