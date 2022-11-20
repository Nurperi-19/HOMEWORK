from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, ADMINS
from keyboards.client_kb import submit_markup, cancel_markup
from database.bot_db import sql_command_insert

class FSMAdmin(StatesGroup):
    mentor_id = State()
    name = State()
    direction = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == "private" and message.from_user.id in ADMINS:
        await FSMAdmin.mentor_id.set()
        await message.answer('ID ментора', reply_markup=cancel_markup)
    else:
        await message.answer('Только куратор может заполнить!\n(В личке)')

async def load_mentor_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['mentor_id'] = message.text
    await FSMAdmin.next()
    await message.answer('Имя ментора')

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Направление")

async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMAdmin.next()
    await message.answer("Возраст")

async def load_age(message: types.Message, state: FSMContext):
    try:
        if 5 < int(message.text) < 70:
            async with state.proxy() as data:
                data['age'] = int(message.text)
            await FSMAdmin.next()
            await message.answer("Группа")
        else:
            await message.answer("Пишите свой настоящий возраст!")
    except:
        await message.answer("Пишите свой настоящий возраст!!")

async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["group"] = message.text
        await bot.send_message(message.from_user.id, f"ID ментора: {data['mentor_id']} \nИмя ментора: {data['name']} "
                                                     f"\nНаправление: {data['direction']} \nВозраст ментора: {data['age']} "
                                                     f"\nГруппа: {data['group']}")
    await FSMAdmin.next()
    await message.answer("Правильно?", reply_markup=submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        await sql_command_insert(state)
        await state.finish()
        await message.answer("Ответ записан")
    elif message.text.lower() == 'нет':
        await state.finish()
        await message.answer("Отмена")
    else:
        await message.answer('Пишите "да" или "нет"!')

async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Отмена!")

def register_handlers_fsm_admin(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state="*", commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True), state="*")

    dp.register_message_handler(fsm_start, commands=['mentor'])
    dp.register_message_handler(load_mentor_id, state=FSMAdmin.mentor_id)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)
