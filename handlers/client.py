from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import dp, bot
from database.bot_db import sql_command_random
from parser import books


async def quiz1(message: types.Message):
    markup1 = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton('Next', callback_data='button_1')
    markup1.add(button_1)

    question1 = 'Какого цвета "черный ящик" в самолете?'
    answers = [
        "красный",
        "черный",
        "оранжевый",
        "белый"
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question1,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2,
        explanation='"Черные ящики" или бортовые самописцы всегда - оранжевого цвета, '
                    'чтобы их легче можно было найти среди обломков самолета.',
        reply_markup=markup1,
    )

async def start_handler(message: types.Message):
    markup2 = InlineKeyboardMarkup()
    button = InlineKeyboardButton('Next', callback_data='button')
    markup2.add(button)
    photo = open('media/mem4.png', 'rb')
    await bot.send_photo(message.from_user.id, photo=photo, reply_markup=markup2)


async def get_random_mentor(message: types.Message):
    await sql_command_random(message)

async def parser_books(message: types.Message):
    items = books.parser()
    for i in items:
        await message.answer(f"{i['link']}\n"
                             f"{i['title']}\n")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['mem'])
    dp.register_message_handler(quiz1, commands=['quiz'])
    dp.register_message_handler(get_random_mentor, commands=['get'])
    dp.register_message_handler(parser_books, commands=['books'])

