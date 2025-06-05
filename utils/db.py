"""
Модуль для работы с базой данных студентов через асинхронный SQLAlchemy.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import (
    AsyncSession, create_async_engine, async_sessionmaker
)
from sqlalchemy.orm import declarative_base
from config import get_database_url

Base = declarative_base()

class Student(Base):
    """
    Модель студента для таблицы students.
    """
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    grade = Column(String, nullable=False)
    city = Column(String, nullable=False)

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', age={self.age}, grade='{self.grade}', city='{self.city}')>"


def get_async_engine():
    """
    Возвращает асинхронный SQLAlchemy engine для текущей среды.
    """
    db_url = get_database_url()
    # Преобразуем URL для asyncpg, если используется PostgreSQL
    if db_url.startswith("postgresql://"):
        db_url = db_url.replace("postgresql://", "postgresql+asyncpg://")
    elif db_url.startswith("sqlite://"):
        db_url = db_url.replace("sqlite://", "sqlite+aiosqlite://")
    return create_async_engine(db_url, echo=False, future=True)


async def create_tables():
    """
    Асинхронно создаёт все таблицы в базе данных (если не существуют).
    """
    engine = get_async_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


def get_async_sessionmaker():
    """
    Возвращает асинхронный sessionmaker для работы с БД.
    """
    engine = get_async_engine()
    return async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession) 