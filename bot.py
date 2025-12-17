# Основной файл бота
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from config import BOT_TOKEN
from database.db import engine, Base
from handlers.user import start, profile, info, tickets as user_tickets, help
from handlers.admin import admin_menu, users, tickets as admin_tickets
from handlers import errors

# Установка команд бота
async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Начало работы"),
        BotCommand(command="help", description="Помощь"),
        BotCommand(command="profile", description="Мой профиль"),
        BotCommand(command="tickets", description="Мои заявки"),
        BotCommand(command="info", description="Информация"),
        BotCommand(command="cancel", description="Отмена"),
    ]
    await bot.set_my_commands(commands)

# Главная функция запуска бота
async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    await set_commands(bot)
    # рег. роутеров
    dp.include_router(errors.router)
    # Админка
    dp.include_router(admin_menu.router)
    dp.include_router(users.router)
    dp.include_router(admin_tickets.router)
    # Юзер
    dp.include_router(start.router)
    dp.include_router(profile.router)
    dp.include_router(info.router)
    dp.include_router(user_tickets.router)
    dp.include_router(help.router)
    print("Бот запущен!")
    await dp.start_polling(bot)
    
# вход
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")

