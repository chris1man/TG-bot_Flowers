from fastapi import FastAPI
import threading
from bot import run_bot

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Bot is running"}

# Запуск Telegram-бота в отдельном потоке
threading.Thread(target=run_bot, daemon=True).start()
