from program import Client, filters


API_ID = "8196994557"
API_HASH = "8ff4733c3bf0f52d2321ca2215fadd21"
BOT_TOKEN = "8196994557:AAGw0-ZWF4LcqivO0qUs0_vfVdFS9yhk0vc"

Darky = Client(
    name="PRIVATEDARKY",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


@darky.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text("join all the channel")



@darky.on_message(filters.command("help"))
async def help_cmd(client, message):
    await message.reply_text("dm me for free hack and sureshot")


print("Bot was Started")
Darky.run()
