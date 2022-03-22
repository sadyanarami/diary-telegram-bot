from aiogram import types

from loader import dp

import pytesseract
from PIL import Image

@dp.message_handler(text="/dz")
async def bot_start(message: types.Message):
    img = Image.open('downloaded-photo/dz.jpg')
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    custom_config = r'--oem 3 --psm 6'

    dz = pytesseract.image_to_string(img, lang='rus', config=custom_config)

    await message.answer(dz)