from pyrogram import Client, filters
from dotenv import load_dotenv
import os

load_dotenv()

API_ID = int(os.getenv("21397343"))
API_HASH = os.getenv("23f9c6deb3137f7910e0115e993436e0")
BOT_TOKEN = os.getenv("8702357908:AAEtFKi02vDLmB6I6Ia8JvjRmQefPRneGf4")

app = Client(
    "mybot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("Hello! Music Bot is Working")

app.run()
