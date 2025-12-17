# админ меню
from aiogram import Router, types
from aiogram.filters import Command
from config import ADMIN_IDS
import keyboards.admin_keyboards as akb

router = Router()

# Команда для входа в админ
@router.message(Command("admin"))
async def admin_start(message: types.Message):
    if message.from_user.id in ADMIN_IDS:
        await message.answer("Админ-панель:", reply_markup=akb.admin_main_kb())
