from fastapi import FastAPI
import asyncio
from bot import run_bot

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Bot is running"}

# Запуск Telegram-бота
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(run_bot())
