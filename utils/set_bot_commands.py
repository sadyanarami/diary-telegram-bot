from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("dz", "Получить домашнее задание"),
        types.BotCommand("schedule", "Узнать расписание предметов"),
        types.BotCommand("load_dz", "Загрузить дз (только для админов)"),
    ])