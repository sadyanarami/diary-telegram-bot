from loader import dp, bot
from aiogram import types

@dp.message_handler(text='/table')
async def send_table(message: types.Message):
    await bot.send_photo(message.chat.id, 'https://ibb.co/yRKn9VG')