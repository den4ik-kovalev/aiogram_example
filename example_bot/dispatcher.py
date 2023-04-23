import asyncio

import aiogram
from aiogram.contrib.fsm_storage.memory import MemoryStorage

__all__ = [
    "bot",
    "dp",
    "run_bot"
]

# токен телеграм-бота
TOKEN = "6150883807:AAFWOz1OERSPdYaKFai4AT8Q4yHJLfgn5mE"

# получение объекта Dispatcher для работы с ботом
loop = asyncio.get_event_loop()
bot = aiogram.Bot(TOKEN, parse_mode="HTML")
dp = aiogram.Dispatcher(bot, loop, storage=MemoryStorage())


def run_bot():
    """ Запустить бота """
    aiogram.executor.start_polling(dp)