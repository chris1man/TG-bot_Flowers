from pyrogram import Client, filters

API_ID = 28660851
API_HASH = "1d03d41046c819595143a76bcbfea44a"
BOT_TOKEN = "7837921213:AAGdbdqtSKhQ839P5O7c2hQADkxzF3pplug"

bot = Client("flower_shop_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("Добро пожаловать в наш магазин цветов! 🌸")

if __name__ == "__main__":
    bot.run()
