from aiogram import types

from loader import dp

import pytesseract
from PIL import Image

from keyboards.default import dz_menu

@dp.message_handler(text='/dz')
async def enter_photo_state(message: types.Message):
    await message.answer("Выберите день недели", reply_markup=dz_menu)

@dp.message_handler(text="*Понедельник*")
async def bot_start(message: types.Message):
    img = Image.open('downloaded-photo/monday_dz.jpg')
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    custom_config = r'--oem 3 --psm 6'

    monday_dz = pytesseract.image_to_string(img, lang='rus', config=custom_config)

    await message.answer(monday_dz)

@dp.message_handler(text="*Вторник*")
async def bot_start(message: types.Message):
    img = Image.open('downloaded-photo/tuesday_dz.jpg')
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    custom_config = r'--oem 3 --psm 6'

    tuesday_dz = pytesseract.image_to_string(img, lang='rus', config=custom_config)

    await message.answer(tuesday_dz)

@dp.message_handler(text="*Среда*")
async def bot_start(message: types.Message):
    img = Image.open('downloaded-photo/wednesday_dz.jpg')
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    custom_config = r'--oem 3 --psm 6'

    wednesday_dz = pytesseract.image_to_string(img, lang='rus', config=custom_config)

    await message.answer(wednesday_dz)

@dp.message_handler(text="*Четверг*")
async def bot_start(message: types.Message):
    img = Image.open('downloaded-photo/thursday_dz.jpg')
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    custom_config = r'--oem 3 --psm 6'

    thursday_dz = pytesseract.image_to_string(img, lang='rus', config=custom_config)

    await message.answer(thursday_dz)

@dp.message_handler(text="*Пятница*")
async def bot_start(message: types.Message):
    img = Image.open('downloaded-photo/friday_dz.jpg')
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    custom_config = r'--oem 3 --psm 6'

    friday_dz = pytesseract.image_to_string(img, lang='rus', config=custom_config)

    await message.answer(friday_dz)