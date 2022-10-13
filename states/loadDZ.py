from aiogram.dispatcher.filters.state import StatesGroup, State


class LoadDz(StatesGroup):
    InLoadDz = State()
    WaitDzPhoto = State()