import time
from datetime import datetime
from multiprocessing import Process
from threading import Thread
from tkinter import *

from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
import asyncio
import pyautogui
import keyboard
import telebot
import config
import config

root = Tk()
sb = Scrollbar(root)
sb.pack(side=RIGHT, fill=Y)
mylist = Listbox(root, yscrollcommand=sb.set)

mylist.pack(side=LEFT)

bot = Bot(token=config.token, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(lambda message: message)
async def message_handler(message: types.Message):
    # print(message.text)
    with open('file.txt', 'a') as f:
        f.write(f'{message.text}\n')


async def on_startup(*args, **kwargs):
    date = datetime.now().strftime("%d/%m/%y.%H:%M")
    print('start')


def work():
    executor.start_polling(dp, on_startup=on_startup)


def upd_text():
    t = ""
    while True:
        with open('file.txt', 'r') as f:
            data = f.read().strip().split()
        try:
            if data[-1] != t:
                t = data[-1]
                mylist.insert(0, data[-1])
            else:
                time.sleep(1)
        except:
            pass
    pass


async def waiter():
    botq = telebot.TeleBot(config.token)
    while True:
        keyboard.wait(config.hotkey)
        print('q')
        x = pyautogui.screenshot('temp.png')
        print(x)

        photo = open('temp.png', 'rb')
        botq.send_photo(f'@{config.channel_nick}', photo)


def work_2():
    asyncio.run(waiter())


def threading():
    # Call work function
    t1 = Process(target=work)
    t1.start()

    t2 = Process(target=work_2)
    t2.start()

    t3 = Thread(target=upd_text)
    t3.start()


if __name__ == '__main__':
    # Set geometry
    root.geometry("400x400")

    threading()

    # Execute Tkinter
    root.mainloop()
