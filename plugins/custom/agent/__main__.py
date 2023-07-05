import openai
import os
from userge import userge, Message
from .. import gpt
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.llms import OpenAI


openaiapi = gpt.GPT_KEY
@userge.on_cmd("agent", about={
    'header': "Agent bot by Yagami",
    'usage': "!agent question"})
async def get_answer(message: Message):
          question = message.input_str
          llm = OpenAI(openai_api_key=openaiapi, temperature=0.6)
          os.environ["SERPAPI_API_KEY"] = 'fc952a1dd0e7cb9ee9a90322d550a518a8446fd9d7685929fdd7088f876a07d7'
          tools = load_tools(["wikipedia","llm-math", "serpapi"], llm=llm)
          agent = initialize_agent(
          tools,
          llm,
          agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION
          )
          await response = agent.run(question)
          await message.edit(f"GPT:\n<i>{response}<i>")
