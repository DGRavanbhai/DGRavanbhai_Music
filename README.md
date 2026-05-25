<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Bold&size=35&pause=1000&color=00FFCC&center=true&vCenter=true&width=900&lines=Music+Bot;Telegram+Music+Streaming+Bot;Fast+%7C+Powerful+%7C+Secure;Made+With+Python" />

<br>

<img src="https://img.shields.io/github/stars/DGRavanbhai/music-bot?style=for-the-badge">
<img src="https://img.shields.io/github/forks/DGRavanbhai/music-bot?style=for-the-badge">
<img src="https://img.shields.io/github/issues/DGRavanbhai/music-bot?style=for-the-badge">
<img src="https://img.shields.io/github/license/DGRavanbhai/music-bot?style=for-the-badge">

<br><br>

<img src="https://images.openai.com/static-rsc-4/Xl3OuYfC7ADVvJ4P3k9PhwrHP2k3B6GouMdyj6GM-WhCSpMrG1gYfeSo4RRzpj3sR-Ii_PtDL7oGuzSeO_8RzGASWvlYkQsJ8_NOAjn7ek4KV-a2FUBYV1-_gqlyGvw11hMfrmfAtLaKqtiuNIl_tV1Ubb2kCYcXeOc1NLyAeN1gjHYkMUNnSjfmRReTagyN?purpose=fullsize" width="1000">

<br><br>

<a href="https://t.me/DGRavanbhai">
<img src="https://img.shields.io/badge/Telegram-Owner-blue?style=for-the-badge&logo=telegram">
</a>

<a href="https://t.me/+y9SXssXwKsIzMGRl">
<img src="https://img.shields.io/badge/Join-Telegram%20Group-blue?style=for-the-badge&logo=telegram">
</a>

</div>

---

# 🎵 Music Bot

A powerful Telegram Music Bot built using **Python**, **Pyrogram**, and **Telegram API**.

This bot supports Telegram commands, music playback systems, and cloud deployment.

---

# 📸 Bot Preview

<div align="center">

<img src="https://telegra.ph/file/95d0d2e48a3b93bb6c4fa.jpg" width="800">

</div>

---

# 🚀 Features

✅ Telegram Music Bot  
✅ Fast & Lightweight  
✅ Secure `.env` Variables  
✅ Easy Deployment  
✅ Heroku Support  
✅ Render Support  
✅ Open Source  
✅ Beginner Friendly  
✅ Pyrogram Based  
✅ Telegram Voice Chat Support  
✅ 24/7 Hosting Ready  

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
    "musicbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("🎵 Music Bot is Working!")

app.run()
```

---

# ▶️ Run Bot

```bash
python main.py
```

---

# ☁️ Deploy on Heroku

## Login Heroku

```bash
heroku login
```

---

## Create Procfile

```bash
worker: python main.py
```

---

## Create App

```bash
heroku create music-bot
```

---

## Add Buildpack

```bash
heroku buildpacks:set heroku/python
```

---

## Deploy Bot

```bash
git add .
git commit -m "Deploy Music Bot"
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

# 📢 Telegram Community

<div align="center">

<a href="https://t.me/DGRavanbhai">
<img src="https://img.shields.io/badge/Owner-DGRavanbhai-blue?style=for-the-badge&logo=telegram">
</a>

<br><br>

<a href="https://t.me/+y9SXssXwKsIzMGRl">
<img src="https://img.shields.io/badge/Join%20Our%20Telegram%20Group-Click%20Here-blue?style=for-the-badge&logo=telegram">
</a>

</div>

---

# ⭐ GitHub Stats

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=DGRavanbhai&show_icons=true&theme=tokyonight">

<br><br>

<img src="https://github-readme-streak-stats.herokuapp.com/?user=DGRavanbhai&theme=tokyonight">

</div>

---

# 👨‍💻 Developer

<div align="center">

<a href="https://t.me/DGRavanbhai">
<img src="https://img.shields.io/badge/Telegram-DGRavanbhai-blue?style=for-the-badge&logo=telegram">
</a>

<br><br>

<img src="https://readme-typing-svg.herokuapp.com?font=Bold&size=28&pause=1000&color=00FFCC&center=true&vCenter=true&width=700&lines=Made+With+❤️+By+DGRavanbhai" />

</div>

---

# 🌟 Support

If you like this project:

⭐ Star the repository  
🍴 Fork the repository  
📢 Share with friends  

---

# 📜 License

This project is licensed under the MIT License.

---

# 📞 Contact & Official Links

<div align="center">

<a href="https://t.me/DGRavanbhai">
<img src="https://img.icons8.com/color/96/telegram-app--v1.png" width="80"/>
</a>

&nbsp;&nbsp;&nbsp;

<a href="https://t.me/+y9SXssXwKsIzMGRl">
<img src="https://img.icons8.com/fluency/96/group.png" width="80"/>
</a>

&nbsp;&nbsp;&nbsp;

<a href="https://instagram.com/DGRavanbhai">
<img src="https://img.icons8.com/fluency/96/instagram-new.png" width="80"/>
</a>

<br><br>

<a href="https://t.me/DGRavanbhai">
<img src="https://img.shields.io/badge/Telegram-DGRavanbhai-blue?style=for-the-badge&logo=telegram">
</a>

<br><br>

<a href="https://instagram.com/DGRavanbhai">
<img src="https://img.shields.io/badge/Instagram-DGRavanbhai-E4405F?style=for-the-badge&logo=instagram&logoColor=white">
</a>

<br><br>

<a href="https://t.me/+y9SXssXwKsIzMGRl">
<img src="https://img.shields.io/badge/Join%20Telegram%20Group-Click%20Here-blue?style=for-the-badge&logo=telegram">
</a>

</div>

---

# 🔗 Official Links

<div align="center">

<a href="https://t.me/DGRavanbhai">
<img src="https://img.icons8.com/color/96/telegram-app--v1.png" width="70"/>
</a>

<br>

### [Telegram Owner](https://t.me/DGRavanbhai)

<br>

<a href="https://t.me/+y9SXssXwKsIzMGRl">
<img src="https://img.icons8.com/fluency/96/group.png" width="70"/>
</a>

<br>

### [Telegram Group](https://t.me/+y9SXssXwKsIzMGRl)

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00FFCC,100:0066FF&height=120&section=footer"/>

</div>
