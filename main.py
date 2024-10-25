from program import Client, filters


API_ID = ""
API_HASH = ""
BOT_TOKEN = ""

Darky = Client(
    name="Darkyxbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


print("Bot was Started")
Darky.run()
