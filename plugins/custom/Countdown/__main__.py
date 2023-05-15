import datetime
from userge import userge, Message

# dictionary to store countdown events and their end times
countdowns = {}

@userge.on_cmd("countdown", about={
    'header': "Set a countdown timer for any event by yagami321",
    'usage': ".countdown [countdown name] [countdown time]",
    'examples': [".countdown New Year 2024-01-01", ".countdown exam remaining 2023-06-10 12:00:00"]
})
async def start_countdown(message: Message):
    try:
        args = message.input_str.split()
        countdown_name = args[0]
        countdown_time = " ".join(args[1:])
        event_time = datetime.datetime.strptime(countdown_time, "%Y-%m-%d %H:%M:%S")
        delta = event_time - datetime.datetime.utcnow()

        # get the replied message and save it as the countdown message
        replied_msg = await message.get_reply_message()
        countdown_msg = replied_msg.text if replied_msg else None

        countdowns[countdown_name] = {
            "end_time": event_time,
            "message": countdown_msg,
            "chat_id": message.chat.id,
            "message_id": None
        }

        while delta.total_seconds() > 0:
            days = delta.days
            hours, remainder = divmod(delta.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            time_remaining = f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
            msg = f"⏳ {countdown_name} countdown: {time_remaining}\n\n{countdown_msg}"
            
            # send the reminder message
            countdown_data = countdowns[countdown_name]
            if countdown_data["message_id"] is None:
                countdown_data["message_id"] = (await userge.send_message(
                    countdown_data["chat_id"], msg)).message_id
            else:
                await userge.edit_message_text(
                    countdown_data["chat_id"], countdown_data["message_id"], text=msg)
                
            await asyncio.sleep(86400)  # send a reminder every 24 hours
            delta = event_time - datetime.datetime.utcnow()
        
        # send the final message once the countdown is finished
        msg = f"🎉 {countdown_name} is here lol!\n\n{countdown_msg}"
        countdown_data = countdowns[countdown_name]
        if countdown_data["message_id"] is None:
            countdown_data["message_id"] = (await userge.send_message(
                countdown_data["chat_id"], msg)).message_id
        else:
            await userge.edit_message_text(
                countdown_data["chat_id"], countdown_data["message_id"], text=msg)

        del countdowns[countdown_name]  # remove the countdown from the dictionary once it's finished
    except Exception as e:
        await message.reply(f"❌ Error: {e}")
