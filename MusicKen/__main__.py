import requests
from pyrogram import Client as Bot
from pytgcalls import idle

from MusicKen.config import API_HASH, API_ID, BG_IMAGE, BOT_TOKEN
from MusicKen.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="MusicKen.modules"),
)
print(f"[INFO]: MUSIC KEN SUDAH AKTIF!")


bot.start()
run()
idle()
