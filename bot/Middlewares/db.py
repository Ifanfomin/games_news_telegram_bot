from typing import Dict

from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types

from sqlalchemy.orm import sessionmaker, Session

from bot.Utils.Database.requests import Database


class DatabaseMiddleware(BaseMiddleware):
    def __init__(self, session: sessionmaker[Session]):
        super(DatabaseMiddleware, self).__init__()
        self.session = session

    async def on_process_message(self, message: types.Message, data: Dict):
        db = Database(session=self.session())
        data["db"] = db
        # async with self.session() as session:
        #     db = Database(session=session)

    async def on_process_callback_query(self, call: types.CallbackQuery, data: Dict):
        db = Database(session=self.session())
        data["db"] = db
