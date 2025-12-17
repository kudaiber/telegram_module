# kb для админов
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def admin_main_kb():
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="/users"), KeyboardButton(text="/tickets")],
    ], resize_keyboard=True)
