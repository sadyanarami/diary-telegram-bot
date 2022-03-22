from aiogram import types
from aiogram.dispatcher import filters
from loader import dp

@dp.message_handler(filters.Command('load_dz'), filters.AdminFilter())
async def photo_handler(message: types.Message):
    await message.photo[-1].download('downloaded-photo/dz.jpg')
    await message.answer('Фото успешно получено!')

    