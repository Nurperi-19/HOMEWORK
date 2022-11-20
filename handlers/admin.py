from aiogram import Dispatcher, types
from config import dp, bot, ADMINS
from database.bot_db import sql_command_delete, sql_command_all
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def pin(message: types.Message):
    if message.from_user.id in ADMINS and message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.message_id)

async def delete_data(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer("Только куратор может заполнить!\n(В личке)")
    else:
        mentors = await sql_command_all(message)
        for mentor in mentors:
            await bot.send_message(message.from_user.id, f"Имя ментора: {mentor[1]} "
                                                 f"\nНаправление: {mentor[2]} "
                                                 f"\nВозраст ментора: {mentor[3]} "
                                                 f"\nГруппа: {mentor[4]}",
                                   reply_markup= InlineKeyboardMarkup().add(
                                       InlineKeyboardButton(f'Удалить {mentor[1]}',
                                                            callback_data=f'delete {mentor[0]}')))

async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(call.data.replace('delete ', ''))
    await call.answer(text='Удалено', show_alert=True)
    await bot.delete_message(call.from_user.id, call.message.message_id)

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(pin, commands=['pin'], commands_prefix="!")
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_callback_query_handler(complete_delete, lambda call: call.data and call.data.startswith('delete '))



