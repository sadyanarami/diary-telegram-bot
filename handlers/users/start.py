from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}! Я бот, который умеет скидывать домашнее задание. Чтобы узнать, что задали на сегодня, напиши /dz")

@dp.message_handler()
async def any_text_message(message: types.Message):
    await message.answer('Прости, но такой команды нет. Чтобы узнать список доступных команд, напиши "/"')