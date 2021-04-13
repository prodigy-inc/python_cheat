from datetime import datetime

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode
from aiogram.utils import executor

import config

bot = Bot(token=config.token, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(lambda message: message)
async def message_handler(message: types.Message):
    print(message.text)
    with open('file.txt', 'a') as f:
        f.write(f'{message.text}\n')
    pass


async def on_startup(*args, **kwargs):
    date = datetime.now().strftime("%d/%m/%y.%H:%M")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
