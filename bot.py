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
        f"<b>🏷 All movies Added .New movies everyday ⬇️⬇️\n\nhttps://t.me/apzmovie_series\nhttps://t.me/apzmovie_series\n\nSQUID GAME SEASON 2(MULTI - AUDIO HD) ⬇️\nJoin & type 👉 SQUID GAME S02 ⬇️\nhttps://t.me/+hWYNt0MArE8zZjhl\n\nPUSHPA 2(MULTI - AUDIO HD) ⬇️https://t.me/+hWYNt0MArE8zZjhl\nSALAAR PART 2(MULTI - AUDIO HD) ⬇️\nhttps://t.me/+hWYNt0MArE8zZjhl</b>",
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
