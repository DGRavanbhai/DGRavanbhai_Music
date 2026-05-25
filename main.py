from pyrogram import Client, filters
from dotenv import load_dotenv
import os

# Load values from .env
load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Create bot
app = Client(
    "mybot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Start command
@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("Hello! Bot is Working")

# Run bot
app.run()
