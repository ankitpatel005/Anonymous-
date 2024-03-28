from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os
from flask import Flask
from threading import Thread


API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = Client("my_account", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
                           
@bot.on_message(filters.private)
async def msg(_, message):
    btn = [[InlineKeyboardButton("🔍 Search Movies", url=f"https://t.me/flimrobot"),
          InlineKeyboardButton("👥 Request Group", url=f"https://t.me/MovieRequestsGrp")]]
    
    await message.reply_text(
        f"<b>🏷 This bot has been unmaintained for long time. Please refer to @FlimRobot for the latest movies and series.\n\n🏷 এই বটটি দীর্ঘদিন ধরে অপরিচলিত রয়েছে। নতুন সিনেমা অ্যান্ড সিরিজ পেতে এই বটটি ভিসিট করুন @FlimRobot</b>",
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