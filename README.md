# Daily Trivia Gpt
This fun little script combines Chatgpt and stable diffusion to send a text daily using twilio containing a random historical fact that happened on 
this day and a img is generated on that topic.

# How it works
ChatGPT is fed a prompt telling it to construct a paragraph about a historical event that happens on today's date which is stored as a variable.
The first line is split from the body of the 'trivia' and passed into stable diffusion which generates a image. Finally, the 'trivia' and the img are sent using twilio
using the schedule library so that a fact is sent everyday.
