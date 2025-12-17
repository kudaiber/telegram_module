from aiogram.fsm.state import State, StatesGroup

# Состояния
class RegisterSG(StatesGroup):
    name = State()
    group = State()
    phone = State()
    confirm = State()
