import os
from userge import userge, Message
from .. import gpt
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.llms import OpenAI

@userge.on_cmd("agent", about={
    'header': "Agent bot by Yagami",
    'usage': "!agent question"})
def get_answer(message: Message):
          question = message.input_str
          llm = OpenAI(openai_api_key= gpt.GPT_KEY, temperature=0.6)
          os.environ["SERPAPI_API_KEY"] = gpt.SERPAPI_API_KEY
          tools = load_tools(["wikipedia","llm-math", "serpapi"], llm=llm)
          agent = initialize_agent(
          tools,
          llm,
          agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION
          )
          response = agent.run(question)
          message.edit(f"GPT:\n<i>{response}<i>")
