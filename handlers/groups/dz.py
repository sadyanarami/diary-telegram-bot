from aiogram import types

from loader import dp

import pytesseract
from PIL import Image

from keyboards.default import dz_menu

@dp.message_handler(text='/dz@schooldiary10bot')
async def enter_photo_state(message: types.Message):
    await message.answer("Выберите день недели", reply_markup=dz_menu)

@dp.message_handler(text="*Понедельник*")
async def bot_start(message: types.Message):
    img = Image.open('downloaded-photo/monday_dz.jpg')
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    custom_config = r'--oem 3 --psm 6'

    monday_dz = pytesseract.image_to_string(img, lang='rus', config=custom_config)

    await message.answer(monday_dz)