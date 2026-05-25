from pyrogram import Client, filters

app = Client(
    "mybot",
    api_id=123456,
    api_hash="your_api_hash",
    bot_token="your_bot_token"
)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("Hello! Music Bot is Working")

app.run()
