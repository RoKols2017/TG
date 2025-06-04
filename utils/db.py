"""
Модуль для работы с базой данных студентов через SQLAlchemy.
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
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

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', age={self.age}, grade='{self.grade}')>"


def get_engine():
    """
    Возвращает SQLAlchemy engine для текущей среды.
    """
    return create_engine(get_database_url(), echo=False, future=True)


def create_tables():
    """
    Создаёт все таблицы в базе данных (если не существуют).
    """
    engine = get_engine()
    Base.metadata.create_all(engine)


def get_session():
    """
    Возвращает сессию SQLAlchemy для работы с БД.
    """
    engine = get_engine()
    Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    return Session() 