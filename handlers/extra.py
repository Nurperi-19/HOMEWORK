from aiogram import Dispatcher, types
from config import dp, bot

import random

animated_emojis = ['🏀', '🎲', '🎯', '⚽', '🎳', '🎰']

async def echo(message: types.Message):
    if message.text.startswith('game'):
        await bot.send_message(message.from_user.id, random.choice(animated_emojis))
    elif message.text.isnumeric():
        await bot.send_message(message.from_user.id, int(message.text)**2)
    else:
        await bot.send_message(message.from_user.id, message.text)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
