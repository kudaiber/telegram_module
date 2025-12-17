# Регистрация пользователя
from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from states.register import RegisterSG
from aiogram.filters import Command
import database.queries as rq
import keyboards.user_keyboards as kb

router = Router()

# Команда старта и регистрации
@router.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext):
    user = await rq.get_user(message.from_user.id)
    if user:
        await message.answer("Вы уже зарегистрированы!", reply_markup=kb.main_kb())
    else:
        await message.answer("Привет! Введите ваше имя:", reply_markup=kb.cancel_kb())
        await state.set_state(RegisterSG.name)

# Регистрация по шагам
@router.message(RegisterSG.name)
async def reg_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите вашу группу:")
    await state.set_state(RegisterSG.group)

@router.message(RegisterSG.group)
async def reg_group(message: types.Message, state: FSMContext):
    await state.update_data(group=message.text)
    await message.answer("Отправьте телефон:", reply_markup=kb.phone_kb())
    await state.set_state(RegisterSG.phone)

@router.message(RegisterSG.phone)
async def reg_phone(message: types.Message, state: FSMContext):
    phone = message.contact.phone_number if message.contact else message.text
    data = await state.get_data()
    await rq.add_user(message.from_user.id, data['name'], data['group'], phone)
    await message.answer("Регистрация завершена!", reply_markup=kb.main_kb())
    await state.clear()

# Команда отмены
@router.message(Command("cancel"))
async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Отменено", reply_markup=kb.main_kb())
