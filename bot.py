from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os
from flask import Flask
from threading import Thread


API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
USER_NAME = os.environ.get("USER_NAME")

bot = Client("my_account", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
                           
@bot.on_message(filters.private)
async def msg(_, message):
    btn = [[InlineKeyboardButton("🔍 Search Movies", url=f"https://t.me/{USER_NAME}")]]
    
    await message.reply_text(
        f"<b>🏷 All movies Added .New movies everyday ⬇️⬇️\n\nhttps://t.me/+1Voaor6RVl40OTll\nhttps://t.me/+1Voaor6RVl40OTll\n\nCHHAAVA HINDI 2025 (MULTI - AUDIO HD) ⬇️\nJoin & type 👉 CHHAAVA 2025 ⬇️\nhttps://t.me/+1Voaor6RVl40OTll\nhttps://t.me/+1Voaor6RVl40OTll\n\nCaptain America: Brave New World(MULTI - AUDIO HD) ⬇️https://t.me/+1Voaor6RVl40OTll</b>",
        reply_markup=InlineKeyboardMarkup(btn),
        disable_web_page_preview=True)
    return

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Friend!"

def run():
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))

if __name__ == "__main__":
    t = Thread(target=run)
    t.start()
    bot.run()
