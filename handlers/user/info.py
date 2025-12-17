from aiogram import Router, F, types
from aiogram.filters import Command
import keyboards.user_keyboards as kb
from aiogram.fsm.context import FSMContext

router = Router()

# Команда информации
@router.message(Command("info"))
@router.message(F.text == "Информация")
async def info_any_state(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "этот бот был создан для модуля, и сам он умеет создавать профиль сохранять в базу данных, и принимать заявки.\nРазработчик: Бурканов Кудайберди",
        reply_markup=kb.main_kb()
    )
