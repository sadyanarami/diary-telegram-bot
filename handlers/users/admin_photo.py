from aiogram import types
from loader import dp

import pytesseract
from PIL import Image

@dp.message_handler(content_types = 'photo')
async def photo_handler(message: types.Message):
    await message.photo[-1].download('downloaded-photo/dz.jpg')
    await message.answer('Фото успешно получено!')

    img = Image.open('downloaded-photo/dz.jpg')
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    custom_config = r'--oem 3 --psm 6'

    dz = pytesseract.image_to_string(img, lang='rus', config=custom_config)

    await message.reply(dz)