from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

router = Router()

# Команда помощи
@router.message(Command("help"))
@router.message(F.text == "Помощь")
async def cmd_help(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Команды:\n/start - Начало\n/cancel - Отмена\n/info - Информация\n/profile - Мой профиль\n/tickets - Мои заявки\n\n")