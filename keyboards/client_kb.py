from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2
)

start_button = KeyboardButton("/start")
quiz_button = KeyboardButton("/quiz")

start_markup.add(start_button, quiz_button)

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(KeyboardButton("ДА"), KeyboardButton("НЕТ"))

cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
).add(KeyboardButton("CANCEL"))