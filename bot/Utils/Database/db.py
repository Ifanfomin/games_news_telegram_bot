# Подключение к базе данных PostgreSQL
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, MetaData, Table, Column, Text, Integer, BLOB, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

from bot.config import config


DATABASE_URL = f"postgresql+asyncpg://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@postgres:5432/{config.POSTGRES_DB}"  # postgres - имя сервиса в docker-compose.uml

# Создание движка подключения
engine = create_async_engine(DATABASE_URL, echo=True)
# engine = create_engine(DATABASE_URL)


metadata = MetaData()

users = Table(
    "users", metadata,
    Column("user_id", Text(), primary_key=True),
    Column("username", Text()),
    Column("name", Text()),
    Column("bought", Text()),
    Column("genres", Text()),  # головоломки:4,стратегии:2,рогалики:13,кооп:7
)

games = Table(
    "games", metadata,
    Column("id", Integer(), primary_key=True, autoincrement=True),
    Column("image", Text()),
    Column("name", Text()),
    Column("developer", Text()),
    Column("price", Text()),
    Column("genre", Text()),
    Column("date", Text()),  # DD.MM.YYYY
    Column("alone", Text()),
    Column("koop", Text()),
    Column("description", Text()),
    Column("sysreq", Text()),
    Column("popularity", Integer())
)

# metadata.create_all(engine)
async def init_models():
    async with engine.begin() as conn:
        # синхронный вызов create_all оборачивается в run_sync
        await conn.run_sync(Base.metadata.create_all)


# Базовый класс для декларативных моделей
Base = declarative_base()

# session = async_sessionmaker(bind=engine)
session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

    


