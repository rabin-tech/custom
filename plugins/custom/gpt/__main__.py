import openai
from userge import userge, Message

openai.api_key = "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"

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
