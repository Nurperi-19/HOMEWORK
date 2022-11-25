import aioschedule
from aiogram import types, Dispatcher
from config import bot
import asyncio


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await message.answer('OK')


async def wake_up():
    with open(r'C:\Users\user\Desktop\Alarm Clock.mp3', 'rb') as audio:
        await bot.send_audio(chat_id=chat_id, audio=audio)

async  def check_emails():
    await bot.send_message(chat_id=chat_id, text='Check your email!')



async def scheduler():
    aioschedule.every().day.at('07:00').do(wake_up)
    aioschedule.every().wednesday.at('20:20').do(check_emails)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id, lambda word: 'notify' in word.text)
