from aiogram.fsm.context import FSMContext
from aiogram import Router, F, types
import database.queries as rq

router = Router()

# Команда профиля
from aiogram.filters import Command
@router.message(Command("profile"))
@router.message(F.text == "Мой профиль")
async def show_profile(message: types.Message, state: FSMContext):
    await state.clear()
    user = await rq.get_user(message.from_user.id)
    if user:
        await message.answer(f"Имя: {user.name}\nГруппа: {user.group}\nТел: {user.phone}")
