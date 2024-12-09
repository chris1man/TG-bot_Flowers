from pyrogram import Client, filters
import asyncio
import os
from dotenv import load_dotenv

# Загрузка переменных окружения
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

# Асинхронный запуск бота
async def run_bot():
    print("Запуск Telegram-бота...")
    await bot.start()
    print("Бот запущен.")
    await asyncio.Event().wait()  # Удерживает приложение активным
