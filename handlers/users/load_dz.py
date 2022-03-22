import pytesseract
from PIL import Image
from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states.loadDZ import LoadDz


@dp.message_handler(text='/load_dz')
async def enter_photo_state(message: types.Message):
    await message.answer('Загрузите фото')
    await LoadDz.Q1.set()


@dp.message_handler(content_types='photo', state=LoadDz.Q1)
async def enter_photo(message: types.Message, state: FSMContext):
    await message.photo[-1].download('downloaded-photo/dz.jpg')
    await message.answer('Фото успешно получено!')
    await state.reset_state()
