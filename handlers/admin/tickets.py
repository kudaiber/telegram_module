# место обработки заяв для админа
from aiogram import Router, types
from aiogram.filters import Command
from config import ADMIN_IDS
import database.queries as rq

router = Router()

# Команда для получения всех заявок
@router.message(Command("tickets"))
async def get_tickets_list(message: types.Message):
    if message.from_user.id not in ADMIN_IDS: return
    
    tickets = await rq.get_all_tickets()
    for t in tickets:
        text = ""
        if t.photo:
            await message.answer_photo(t.photo)
        else:
            text = "\nФото: нет"
        await message.answer(f"Заявка #{t.id}\n{t.text}\nСтатус: {t.status}\nСоздана: {t.created_at:%d.%m.%Y %H:%M}\nПользователь ID: {t.user_id}" + text)