from prompt_toolkit import prompt
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.formatted_text import HTML
import google.generativeai as genai
import os

bindings = KeyBindings()


@bindings.add('c-v')  # Ctrl+Enter
def _(event):
    event.app.current_buffer.validate_and_handle()


user_phrase = prompt(
    HTML("> <b>Enter the text:</b> "),
    multiline=True,
    key_bindings=bindings
)

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

promt = \
    f"Переведи фразу. \n" \
    f"Следуй при переводе этим правилам: \n" \
    f"Если фраза на анлийском, значит переводи на русский," \
    f"Если фраза на русском, значит переводи на английский. \n" \
    f"Так же если внутри фразы есть скобочки," \
    f"это означает что я указываю тебе контекст фразы," \
    f"то что в скобочках не пиши в своем ответе. \n" \
    f"Фраза: '{user_phrase}' \n"
response = model.generate_content(promt)
print(response.text)
