from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import dp, bot


async def quiz2(call: types.CallbackQuery):
    markup1 = InlineKeyboardMarkup()
    button_2 = InlineKeyboardButton('Next', callback_data='button_2')
    markup1.add(button_2)

    question1 = 'Кто из перечисленных ниже изобрел вырезание/копирование и вставку?'
    answers = [
        "Уорд Каннингем",
        "Ларри Теслер",
        "Ли де Форест",
        "Леонар Макс Адлеман"
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question1,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=1,
        explanation="Ларри Теслер и Тим Мотт вместе изобрели концепцию вырезания/копирования и вставки.",
        reply_markup=markup1
    )

async def quiz3(call: types.callback_query):
    question1 = 'Что выведет на экран следующий код?'
    answers = [
        "1 [] 2",
        "1 0 2",
        "1 [2] undefined",
        "0 [1,2] 0",
        "0 [1] 2",
    ]
    photo = open('media/task1.jpg', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question1,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        explanation='В "a" и "c" будут записаны числа. А в "*b" оставшиеся избыток',
    )

async def start_handler(call: types.CallbackQuery):
    photo2 = open('media/mem6.jpg', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo2)


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz2, text="button_1")
    dp.register_callback_query_handler(quiz3, text="button_2")
    dp.register_callback_query_handler(start_handler, text="button")
