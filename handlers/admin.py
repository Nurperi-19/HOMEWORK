from aiogram import Dispatcher, types
from config import dp, bot, ADMINS

async def ban(message: types.Message):
    if message.chat.type == "group":
        if message.from_user.id not in ADMINS:
            await message.answer("Ты не мой БОСС!")
        elif not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
        else:
            await bot.kick_chat_member(message.chat.id,
                                       message.reply_to_message.from_user.id)
            await message.answer(f"{message.from_user.first_name} братан "
                                 f"забанил {message.reply_to_message.from_user.full_name}")
    else:
        await message.answer("Пиши в группе!")

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['pin'], commands_prefix="!")
