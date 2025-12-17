# Обработчик ошибок
from aiogram import Router, types
import logging

router = Router()

@router.error()
async def error_handler(event: types.ErrorEvent):
    logging.error(f"Произошла ошибка: {event.exception}")
    # Можно отправить сообщение админу или юзеру, если нужно
