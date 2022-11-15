from aiogram import Dispatcher, types
from config import dp, bot, ADMINS

async def pin(message: types.Message):
    if message.from_user.id in ADMINS and message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.message_id)



def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(pin, commands=['pin'], commands_prefix="!")