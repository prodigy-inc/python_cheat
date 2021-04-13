import asyncio

import aiogram
import pyautogui
import keyboard
import telebot
import config

botq = telebot.TeleBot(config.token)


async def waiter():
    while True:
        keyboard.wait('Ctrl + Q')
        print('q')
        x = pyautogui.screenshot('temp.png')
        print(x)

        photo = open('temp.png', 'rb')
        botq.send_photo(f'@{config.channel_nick}', photo)


asyncio.run(waiter())
