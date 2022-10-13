from distutils.cmd import Command
import pytesseract
from PIL import Image
from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext

from keyboards.default import dz_menu
from loader import dp
from states.dzstate import OnDz


@dp.message_handler(text='/dz')
async def enter_photo_state(message: types.Message):
    await OnDz.WaitDz.set()
    await message.answer("Выберите день недели", reply_markup=dz_menu)



@dp.message_handler(state=OnDz.WaitDz)
async def bot_start(message: types.Message, state: FSMContext):
    answer = message.text
    translator = {
        "*Понедельник*": 'monday',
        "*Вторник*": 'tuesday',
        "*Среда*": 'wednesday',
        "*Четверг*": 'thursday',
        "*Пятница*": 'friday',
    }
    translator_answer=translator[answer]
    img = Image.open(f'downloaded-photo/{translator_answer}_dz.jpg')
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    custom_config = r'--oem 3 --psm 6'

    dz = pytesseract.image_to_string(img, lang='rus', config=custom_config)

    await message.answer(dz, reply_markup=ReplyKeyboardRemove())
    await state.reset_state()



