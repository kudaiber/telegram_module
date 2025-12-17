from sqlalchemy import select, update
from database.db import async_session
from database.models import User, Ticket

async def get_user(tg_id: int):
    async with async_session() as session:
        return await session.scalar(select(User).where(User.telegram_id == tg_id))

async def add_user(tg_id: int, name: str, group: str, phone: str):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == tg_id))
        if not user:
            session.add(User(telegram_id=tg_id, name=name, group=group, phone=phone))
            await session.commit()

async def get_all_users():
    async with async_session() as session:
        result = await session.execute(select(User))
        return result.scalars().all()

async def create_ticket(tg_id: int, text: str, photo: str = None):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == tg_id))
        if user:
            session.add(Ticket(user_id=user.id, text=text, photo=photo))
            await session.commit()
            return True
        return False

async def get_all_tickets(status: str = None):
    async with async_session() as session:
        query = select(Ticket)
        if status:
            query = query.where(Ticket.status == status)
        result = await session.execute(query)
        return result.scalars().all()

async def get_user_tickets(tg_id: int):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == tg_id))
        if user:
            result = await session.execute(select(Ticket).where(Ticket.user_id == user.id))
            return result.scalars().all()
        return []
    result = await session.execute(
        select(Ticket)
        .where(Ticket.user_id == user.id)
        .order_by(Ticket.created_at.desc())
    )
    return result.scalars().all()

    