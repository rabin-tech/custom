from userge import Message, userge

@userge.on_cmd("mukul", about={"header": "Mukulize your text"})
async def upper_text(message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text.upper()
        await message.edit(text)

@userge.on_cmd("dukul", about={"header": "Demukulize your text"})
async def lower_text(message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text.lower()
        await message.edit(text)
