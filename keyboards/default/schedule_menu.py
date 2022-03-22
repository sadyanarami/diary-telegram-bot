from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

schedule_menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = 'Понедельник'),
            KeyboardButton(text = 'Вторник'),
        ],
        [
            KeyboardButton(text = 'Среда'),
            KeyboardButton(text = 'Четверг'),
        ],
        [
            KeyboardButton(text = 'Пятница'),
        ],
    ],
    resize_keyboard = True
)