import openai
from userge import userge, Message
import os

openai.api_key = os.environ.get("GPT_KEY")

@userge.on_cmd("gpt", about={
    'header': "ChatGPT bot by Yagami",
    'usage': "!gpt question"})
async def get_answer(message: Message):
          question = message.input_str
          response = openai.Completion.create(
          engine="text-davinci-002",
          prompt=(f"{question}\n"),
          max_tokens=4000,
          n=1,
          stop=None,
          temperature=0.7,
      )
          await message.edit(response["choices"][0]["text"])
