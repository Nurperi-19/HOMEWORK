from aiogram import Dispatcher, types
from config import dp, bot, ADMINS

async def ban(message: types.Message):
    if message.from_user.id not in ADMINS:
        pass

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['pin'], commands_prefix="!")
