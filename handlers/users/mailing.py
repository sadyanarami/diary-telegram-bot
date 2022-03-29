import random

from loader import dp, bot
from aiogram import types

from utils.user_list import *

@dp.message_handler(text='/mail')
async def mailing_users(message: types.Message):
    for user in joinedUsers:
        with open("motivation_phrases.txt", encoding="utf-8") as inp:
            lines = inp.readlines()
        motivation_phrase = random.choice(lines).strip()
        await dp.bot.send_message(user, motivation_phrase)