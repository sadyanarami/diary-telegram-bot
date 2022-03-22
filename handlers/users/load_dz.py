from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default import schedule_menu
from loader import dp
from states.loadDZ import LoadDz


@dp.message_handler(text='/load_dz')
async def enter_photo_state(message: types.Message):
    await message.answer("Выберите день недели", reply_markup=schedule_menu)
    await LoadDz.Q1.set()


@dp.message_handler(text="Понедельник", state=LoadDz.Q1)
async def get_dz_monday(message: types.Message):
    await message.answer('Отправьте фото')

    @dp.message_handler(content_types='photo', state=LoadDz.Q1)
    async def enter_photo(message: types.Message, state: FSMContext):
        await message.photo[-1].download('downloaded-photo/monday_dz.jpg')
        await message.answer('Фото успешно получено!')
        await state.reset_state()


@dp.message_handler(text="Вторник", state=LoadDz.Q1)
async def get_dz_monday(message: types.Message):
    await message.answer('Отправьте фото')

    @dp.message_handler(content_types='photo', state=LoadDz.Q1)
    async def enter_photo(message: types.Message, state: FSMContext):
        await message.photo[-1].download('downloaded-photo/tuesday_dz.jpg')
        await message.answer('Фото успешно получено!')
        await state.reset_state()


@dp.message_handler(text="Среда", state=LoadDz.Q1)
async def get_dz_monday(message: types.Message):
    await message.answer('Отправьте фото')

    @dp.message_handler(content_types='photo', state=LoadDz.Q1)
    async def enter_photo(message: types.Message, state: FSMContext):
        await message.photo[-1].download('downloaded-photo/wednesday_dz.jpg')
        await message.answer('Фото успешно получено!')
        await state.reset_state()


@dp.message_handler(text="Четверг", state=LoadDz.Q1)
async def get_dz_monday(message: types.Message):
    await message.answer('Отправьте фото')

    @dp.message_handler(content_types='photo', state=LoadDz.Q1)
    async def enter_photo(message: types.Message, state: FSMContext):
        await message.photo[-1].download('downloaded-photo/thursday_dz.jpg')
        await message.answer('Фото успешно получено!')
        await state.reset_state()


@dp.message_handler(text="Пятница", state=LoadDz.Q1)
async def get_dz_monday(message: types.Message):
    await message.answer('Отправьте фото')

    @dp.message_handler(content_types='photo', state=LoadDz.Q1)
    async def enter_photo(message: types.Message, state: FSMContext):
        await message.photo[-1].download('downloaded-photo/friday_dz.jpg')
        await message.answer('Фото успешно получено!')
        await state.reset_state()
