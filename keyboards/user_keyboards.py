# kb для пользователей
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def main_kb():
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Мой профиль"), KeyboardButton(text="Информация")],
        [KeyboardButton(text="Оставить заявку"), KeyboardButton(text="Мои заявки")],
        [KeyboardButton(text="Помощь")]
    ], resize_keyboard=True)

def cancel_kb():
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="/cancel")]], resize_keyboard=True)

def phone_kb():
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="📱 Отправить телефон", request_contact=True)]], resize_keyboard=True)
