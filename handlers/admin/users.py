# место просмотра пользователей для админа
from aiogram import Router, types
from aiogram.filters import Command
from config import ADMIN_IDS
import database.queries as rq

router = Router()

@router.message(Command("users"))
async def get_users_list(message: types.Message):
    if message.from_user.id not in ADMIN_IDS: return
    
    users = await rq.get_all_users()
    text = "Пользователи:\n" + "\n".join([f"{u.id}. {u.name}" for u in users])
    await message.answer(text)
