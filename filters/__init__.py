from aiogram import Dispatcher

from loader import dp
from .admin_command import IsAdmin
# from .is_admin import AdminFilter


if __name__ == "filters":
    dp.filters_factory.bind(IsAdmin)
