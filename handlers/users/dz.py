import pytesseract
from PIL import Image
from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default import schedule_menu
from loader import dp
from states.schedulestate import OnSchedule


@dp.message_handler(text='/dz')
async def enter_photo_state(message: types.Message):
    await OnSchedule.Q1.set()
    await message.answer("Выберите день недели", reply_markup=schedule_menu)


@dp.message_handler(text="Понедельник", state=OnSchedule.Q1)
async def bot_start(message: types.Message, state: FSMContext):
    img = Image.open('downloaded-photo/monday_dz.jpg')
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    custom_config = r'--oem 3 --psm 6'

    monday_dz = pytesseract.image_to_string(img, lang='rus', config=custom_config)

    await message.answer(monday_dz)
    await state.reset_state()


@dp.message_handler(text="Вторник", state=OnSchedule.Q1)
async def bot_start(message: types.Message, state: FSMContext):
    img = Image.open('downloaded-photo/tuesday_dz.jpg')
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    custom_config = r'--oem 3 --psm 6'

    tuesday_dz = pytesseract.image_to_string(img, lang='rus', config=custom_config)

    await message.answer(tuesday_dz)
    await state.reset_state()


@dp.message_handler(text="Среда", state=OnSchedule.Q1)
async def bot_start(message: types.Message, state: FSMContext):
    img = Image.open('downloaded-photo/wednesday_dz.jpg')
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    custom_config = r'--oem 3 --psm 6'

    wednesday_dz = pytesseract.image_to_string(img, lang='rus', config=custom_config)

    await message.answer(wednesday_dz)
    await state.reset_state()


@dp.message_handler(text="Четверг", state=OnSchedule.Q1)
async def bot_start(message: types.Message, state: FSMContext):
    img = Image.open('downloaded-photo/thursday_dz.jpg')
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    custom_config = r'--oem 3 --psm 6'

    thursday_dz = pytesseract.image_to_string(img, lang='rus', config=custom_config)

    await message.answer(thursday_dz)
    await state.reset_state()


@dp.message_handler(text="Пятница", state=OnSchedule.Q1)
async def bot_start(message: types.Message, state: FSMContext):
    img = Image.open('downloaded-photo/friday_dz.jpg')
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    custom_config = r'--oem 3 --psm 6'

    friday_dz = pytesseract.image_to_string(img, lang='rus', config=custom_config)

    await message.answer(friday_dz)
    await state.reset_state()
