from aiogram import types

from loader import dp

@dp.message_handler(text="/dz@schooldiary10bot")
async def bot_start(message: types.Message):
    await message.answer("Вот домашнее задание на сегодня:")