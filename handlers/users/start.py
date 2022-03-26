from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

from utils.user_list import *

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if not message.chat.id in joinedUsers:
        joinedFile = open('user_list.txt', 'a')
        joinedFile.write(message.chat.id + "\n")
        joinedUsers.add(message.chat.id)
    await message.answer(f"Привет, {message.from_user.full_name}! Я бот, который умеет скидывать домашнее задание. Чтобы узнать, что задали на сегодня, напиши /dz")