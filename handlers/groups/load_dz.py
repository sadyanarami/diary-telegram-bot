import pytesseract
from PIL import Image
from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states.loadDZ import LoadDz

from keyboards.default import admin_dz_menu


@dp.message_handler(text='/load_dz@schooldiary10bot')
async def enter_photo_state(message: types.Message):
    await message.answer("Выберите день недели", reply_markup=admin_dz_menu)

@dp.message_handler(text="/Понедельник/")
async def get_dz_monday(message: types.Message):
    await message.answer('Отправьте фото')
    await LoadDz.Q1.set()

    @dp.message_handler(content_types='photo', state=LoadDz.Q1)
    async def enter_photo(message: types.Message, state: FSMContext):
        await message.photo[-1].download('downloaded-photo/monday_dz.jpg')
        await message.answer('Фото успешно получено!')
        await state.reset_state()

@dp.message_handler(text="/Вторник/")
async def get_dz_monday(message: types.Message):
    await message.answer('Отправьте фото')
    await LoadDz.Q1.set()

    @dp.message_handler(content_types='photo', state=LoadDz.Q1)
    async def enter_photo(message: types.Message, state: FSMContext):
        await message.photo[-1].download('downloaded-photo/tuesday_dz.jpg')
        await message.answer('Фото успешно получено!')
        await state.reset_state()
    
@dp.message_handler(text="/Среда/")
async def get_dz_monday(message: types.Message):
    await message.answer('Отправьте фото')
    await LoadDz.Q1.set()

    @dp.message_handler(content_types='photo', state=LoadDz.Q1)
    async def enter_photo(message: types.Message, state: FSMContext):
        await message.photo[-1].download('downloaded-photo/wednesday.jpg')
        await message.answer('Фото успешно получено!')
        await state.reset_state()

@dp.message_handler(text="/Четверг/")
async def get_dz_monday(message: types.Message):
    await message.answer('Отправьте фото')
    await LoadDz.Q1.set()

    @dp.message_handler(content_types='photo', state=LoadDz.Q1)
    async def enter_photo(message: types.Message, state: FSMContext):
        await message.photo[-1].download('downloaded-photo/thursday.jpg')
        await message.answer('Фото успешно получено!')
        await state.reset_state()

@dp.message_handler(text="/Пятница/")
async def get_dz_monday(message: types.Message):
    await message.answer('Отправьте фото')
    await LoadDz.Q1.set()

    @dp.message_handler(content_types='photo', state=LoadDz.Q1)
    async def enter_photo(message: types.Message, state: FSMContext):
        await message.photo[-1].download('downloaded-photo/friday.jpg')
        await message.answer('Фото успешно получено!')
        await state.reset_state()