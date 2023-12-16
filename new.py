import pathlib
import textwrap

import PIL.Image

img = PIL.Image.open('meta.jpg')




import google.generativeai as genai

# Used to securely store your API key


from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


GOOGLE_API_KEY="Your api"

genai.configure(api_key=GOOGLE_API_KEY)


for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)


# model = genai.GenerativeModel('gemini-pro')
# response = model.generate_content("Hi how are u")#input question


model = genai.GenerativeModel('gemini-pro-vision')
response = model.generate_content(img)
print(response.text)
