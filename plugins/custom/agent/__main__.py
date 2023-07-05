from pyrogram import filters
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.llms import OpenAI

@userge.on_cmd("agpt", about={
    'header': "Ask any question",
    'description': "Agent gpt by @yagami321"
})
@userge.disable_antiflood
async def ask_question(message: Message):
    question = message.input_str
    llm = OpenAI(openai_api_key='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', temperature=0.6)
    os.environ["SERPAPI_API_KEY"] = 'a2c05da113871302554b44900dd257de7f3312076c9c56797834bc10426aa38e'
    tools = load_tools(["wikipedia", "serpapi"], llm=llm)
    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION
    )
    response = agent.run(question)
    await message.reply(f"Agent:\n<i>{response}<i>")
