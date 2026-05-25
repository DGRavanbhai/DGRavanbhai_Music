<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Bold&size=35&pause=1000&color=00FFCC&center=true&vCenter=true&width=900&lines=Telegram+Music+Bot;Pyrogram+Based+Telegram+Bot;Fast+%7C+Powerful+%7C+Secure;Made+With+Python" />

<br>

<img src="https://img.shields.io/github/stars/yourusername/telegram-music-bot?style=for-the-badge">
<img src="https://img.shields.io/github/forks/yourusername/telegram-music-bot?style=for-the-badge">
<img src="https://img.shields.io/github/issues/yourusername/telegram-music-bot?style=for-the-badge">
<img src="https://img.shields.io/github/license/yourusername/telegram-music-bot?style=for-the-badge">

</div>

---

# 🎵 Telegram Music Bot

A powerful Telegram Music Bot built using **Python**, **Pyrogram**, and **Telegram API**.

This bot can play music, respond to commands, and can be deployed easily on cloud hosting platforms.

---

# 🚀 Features

✅ Fast & Powerful Bot  
✅ Telegram Command Support  
✅ Pyrogram Based  
✅ Easy Deployment  
✅ Secure `.env` Variables  
✅ Heroku Deployment  
✅ Render Deployment  
✅ Open Source  
✅ Beginner Friendly  

---

# 📸 Preview

<div align="center">

<img src="https://telegra.ph/file/6f7d1e5bb8f5b7b5f7b2f.jpg" width="700">

</div>

---

# 🤖 Commands

| Command | Description |
|----------|-------------|
| `/start` | Start the bot |
| `/help` | Help menu |
| `/play` | Play music |
| `/pause` | Pause current song |
| `/resume` | Resume music |
| `/skip` | Skip current song |
| `/end` | Stop music |

---

# 📂 Project Structure

```bash
project-folder/
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# ⚡ Requirements

- Python 3.10+
- Telegram Bot Token
- API_ID
- API_HASH

---

# ⚙️ Environment Variables

Create `.env`

```env
API_ID=12345678
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
```

---

# 📜 requirements.txt

```txt
pyrogram
tgcrypto
python-dotenv
```

---

# 🔒 .gitignore

```txt
.env
```

---

# 🧠 main.py

```python
from pyrogram import Client, filters
from dotenv import load_dotenv
import os

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

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
```

---

# ▶️ Run Bot

```bash
python main.py
```

---

# ☁️ Deploy on Heroku

## Create Procfile

```bash
worker: python main.py
```

---

## Login Heroku

```bash
heroku login
```

---

## Create App

```bash
heroku create your-bot-name
```

---

## Add Buildpack

```bash
heroku buildpacks:set heroku/python
```

---

## Deploy

```bash
git add .
git commit -m "Deploy Bot"
git push heroku main
```

---

# ☁️ Deploy on Render

## Build Command

```bash
pip install -r requirements.txt
```

## Start Command

```bash
python main.py
```

---

# ⭐ GitHub Stats

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=yourusername&show_icons=true&theme=tokyonight">

<img src="https://github-readme-streak-stats.herokuapp.com/?user=yourusername&theme=tokyonight">

</div>

---

# 🛡 Security

✅ Never share your:

- BOT_TOKEN
- API_HASH
- `.env` file

---

# 👨‍💻 Developer

<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Bold&size=28&pause=1000&color=00FFCC&center=true&vCenter=true&width=700&lines=Made+With+❤️+By+Your+Name" />

</div>

---

# 🌟 Support

If you like this project:

⭐ Star the repository  
🍴 Fork the repository  
📢 Share with others  

---

# 📜 License

This project is licensed under the MIT License.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00FFCC,100:0066FF&height=120&section=footer"/>

</div>
