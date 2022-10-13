from aiogram import types
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import schedule_menu
from loader import dp


@dp.message_handler(text="/schedule")
async def schedule_message(message: types.Message):
    await message.answer("Выберите день недели", reply_markup=schedule_menu)


@dp.message_handler(text="Понедельник")
async def get_monday(message: types.Message):
    await message.answer('''1.  Разговоры о важном
2. Биология
3. Геометрия
4. Физика
5. Физика
6. Физкультура
7. Экономика''', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="Вторник")
async def get_tuesday(message: types.Message):
    await message.answer('''1. Химия
2. История
3. История
4. Я выбираю
5. Английский язык
6. Геометрия
7. ОБЖ''', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="Среда")
async def get_wednesday(message: types.Message):
    await message.answer('''1. География
2. Обществознание
3. Биология
4. Обществознание
5. Английский язык
6. Литература
7. Факультатив (Шахова)''', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="Четверг")
async def get_thursday(message: types.Message):
    await message.answer('''1. Классный час
2. Физкультура
3. Алгебра
4. Русский язык
5. Литература
6. Алгебра
7. Английский язык
8. Факультатив (Ашихина)''', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="Пятница")
async def get_friday(message: types.Message):
    await message.answer('''1. Родной русский
2. Литература
3. Право
4. Физкультура
5. Алгебра
6. Алгебра
7. Информатика''', reply_markup=ReplyKeyboardRemove())