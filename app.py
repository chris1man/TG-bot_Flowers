from fastapi import FastAPI
import threading
from bot import bot

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Bot is running"}

# Запуск Telegram-бота в отдельном потоке
def start_bot():
    bot.run()

threading.Thread(target=start_bot).start()
