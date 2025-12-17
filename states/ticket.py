from aiogram.fsm.state import State, StatesGroup

# Состояния
class TicketSG(StatesGroup):
    text = State()
    photo = State()
