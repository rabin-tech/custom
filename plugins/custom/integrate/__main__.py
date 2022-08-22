import requests , json
from userge import userge, Message

@userge.on_cmd("integrate", about={
    'header': "Performes integration operations",
    'usage': "!integrate question",
    'example': "!integrate e^x\cos \left(x\right)dx"
})
async def calculus(message: Message):
            value = message.input_str
            query = "integrate" + "%20" + value
            api_address = f"https://api.wolframalpha.com/v2/query?appid=Y98QH3-24PWX83VGA&input={query}&podstate=Step-by-step%20solution&output=json&format=image"
            json_data = requests.get(api_address).json()
            answer = json_data["queryresult"]["pods"][0]["subpods"][1]["img"]["src"]
            answer = answer.replace("sqrt", "√")
            await message.edit(answer)
