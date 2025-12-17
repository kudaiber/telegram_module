# для заявок пользователей
from aiogram import Router, F, types, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states.ticket import TicketSG
import database.queries as rq
import keyboards.user_keyboards as kb
from config import ADMIN_IDS

router = Router()

# Команда создания заявки
@router.message(Command("ticket"))
@router.message(F.text == "Оставить заявку")
async def ticket_start(message: types.Message, state: FSMContext):
    await message.answer("Опишите проблему:", reply_markup=kb.cancel_kb())
    await state.set_state(TicketSG.text)

# Шаги создания заявки
@router.message(TicketSG.text)
async def ticket_text(message: types.Message, state: FSMContext):
    await state.update_data(text=message.text)
    await message.answer("Пришлите фото или напишите 'нет':")
    await state.set_state(TicketSG.photo)

@router.message(TicketSG.photo)
async def ticket_photo(message: types.Message, state: FSMContext, bot: Bot):
    photo_id = message.photo[-1].file_id if message.photo else None
    data = await state.get_data()
    
    await rq.create_ticket(message.from_user.id, data['text'], photo_id)
    await message.answer("Заявка отправлена!", reply_markup=kb.main_kb())
    await state.clear()
    
    for admin in ADMIN_IDS:
        try:
            await bot.send_message(admin, f"Новая заявка от {message.from_user.id}!")
        except: pass

# Команда просмотра заявок
@router.message(Command("tickets"))
@router.message(F.text == "Мои заявки")
async def my_tickets(message: types.Message):
    tickets = await rq.get_user_tickets(message.from_user.id)

    if not tickets:
        await message.answer(
            "У вас пока нет заявок.",
            reply_markup=kb.main_kb()
        )
        return

    text = "Ваши заявки:\n\n"
    for t in tickets:
        text += (
            f"№{t.id}\n"
            f"Статус: {t.status}\n"
            f"{t.text}\n"
            f"{t.created_at:%d.%m.%Y %H:%M}\n\n"
        )
        if t.photo == None:
            text = "Фото: нет\n"
        else:
            if t.photo:
                await message.answer_photo(photo=t.photo, caption=text)
            else:
                await message.answer(text)
            text = ""
    await message.answer(text, reply_markup=kb.main_kb())
