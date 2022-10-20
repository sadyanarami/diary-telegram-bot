from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext

from keyboards.default import schedule_menu
from loader import dp
from states.loadDZ import LoadDz
from filters import IsAdmin


@dp.message_handler(IsAdmin(), text='/load_dz')
async def enter_photo_state(message: types.Message):
    await message.answer("Выберите день недели", reply_markup=schedule_menu)
    await LoadDz.InLoadDz.set()


@dp.message_handler(state=LoadDz.InLoadDz)
async def get_dz_monday(message: types.Message, state: FSMContext):
    await message.answer('Отправьте фото', reply_markup=ReplyKeyboardRemove())
    answer = message.text
    translator = {
        "Понедельник": 'monday',
        "Вторник": 'tuesday',
        "Среда": 'wednesday',
        "Четверг": 'thursday',
        "Пятница": 'friday',
    }
    await state.update_data(answer1=translator[answer])
    await LoadDz.next()

    @dp.message_handler(content_types='photo', state=LoadDz.WaitDzPhoto)
    async def enter_photo(message: types.Message, state: FSMContext):
        data = await state.get_data()
        answer1 = data.get("answer1")
        await message.photo[-1].download(f'downloaded-photo/{answer1}_dz.jpg')
        await message.answer('Фото успешно получено!')
        await state.reset_state()
