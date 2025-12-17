# Конфиг файл
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
# Превращаем строку в список чисел
ADMIN_IDS = [int(id_str) for id_str in os.getenv("ADMIN_IDS").split(",")]
