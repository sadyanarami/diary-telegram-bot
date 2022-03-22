from aiogram import types

from keyboards.default import schedule_menu
from loader import dp


@dp.message_handler(text="/schedule")
async def schedule_message(message: types.Message):
    await message.answer("Выберите день недели", reply_markup=schedule_menu)


@dp.message_handler(text="Понедельник")
async def get_monday(message: types.Message):
    await message.answer('''1. Лит-ра
2. Геометрия
3. Обществознание
4. Обществознание
5. Физика
6. Физика
7. Физкультура''')


@dp.message_handler(text="Вторник")
async def get_monday(message: types.Message):
    await message.answer('''1. Алгебра
2. Алгебра
3. Русский язык
4. Русский ЕГЭ
5. ОБЖ
6. Информатика
7. Английский язык''')


@dp.message_handler(text="Среда")
async def get_monday(message: types.Message):
    await message.answer('''1. Химия
2. Физкультура
3. Русский язык
4. Литература
5. История
6. Экономика
7. Финансовая грамотность''')


@dp.message_handler(text="Четверг")
async def get_monday(message: types.Message):
    await message.answer('''1. Алгебра
2. Алгебра
3. География
4. Биология
5. Английский язык
6. Проект
7. Классный час''')


@dp.message_handler(text="Пятница")
async def get_monday(message: types.Message):
    await message.answer('''1. История
2. Астрономия
3. Право
4. Литература
5. Английский язык
6. Геометрия
7. Физ-ра''')
