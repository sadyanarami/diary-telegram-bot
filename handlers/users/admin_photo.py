from aiogram import types
from loader import dp

@dp.message_handler(content_types = 'photo')
async def photo_handler(message: types.Message):
    await message.photo[-1].download('downloaded-photo/dz.jpg')
    await message.answer('Фото успешно получено!')

    