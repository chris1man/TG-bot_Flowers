from pyrogram import Client, filters
import os
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Инициализация клиента
bot = Client("MAKI_Flower_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Обработчик команды /start
@bot.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("Добро пожаловать в наш магазин цветов! 🌸")

# Функция для запуска бота
def run_bot():
    print("Запуск Telegram-бота...")
    bot.run()
