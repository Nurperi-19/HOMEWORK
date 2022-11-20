import random
import sqlite3
from config import bot

def sql_create():
    global db, cursor
    db = sqlite3.connect('bot.sqlite3')
    cursor = db.cursor()

    if db:
        print('База данных подключена')

    db.execute("CREATE TABLE IF NOT EXISTS mentors "
               "(id INTEGER PRIMARY KEY, "
               "name TEXT, "
               "direction TEXT, "
               "age INTEGER,"
               "ment_group TEXT)")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO mentors VALUES "
                       "(?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()

async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM mentors").fetchall()
    random_mentor = random.choice(result)
    await bot.send_message(message.from_user.id, f"Имя ментора: {random_mentor[1]} "
                                                 f"\nНаправление: {random_mentor[2]} "
                                                 f"\nВозраст ментора: {random_mentor[3]} "
                                                 f"\nГруппа: {random_mentor[4]}")

async def sql_command_all(message) -> list:
    return cursor.execute("SELECT * FROM mentors").fetchall()

async def sql_command_delete(user_id) -> None:
    cursor.execute("DELETE FROM mentors WHERE id = ?", (user_id, ))
    db.commit()

