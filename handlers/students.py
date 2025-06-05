from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from utils.db import Student, get_async_sessionmaker, create_tables
from utils.services import YandexWeatherService
from utils.formatters import format_weather

router = Router()

class StudentForm(StatesGroup):
    name = State()
    age = State()
    grade = State()
    city = State()

@router.message(Command("add_student"))
async def cmd_add_student(message: types.Message, state: FSMContext):
    """
    Запуск добавления нового студента (FSM).
    """
    await message.answer("Введите имя студента:")
    await state.set_state(StudentForm.name)

@router.message(StudentForm.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text.strip())
    await message.answer("Введите возраст студента:")
    await state.set_state(StudentForm.age)

@router.message(StudentForm.age)
async def process_age(message: types.Message, state: FSMContext):
    try:
        age = int(message.text.strip())
        if not (5 <= age <= 100):
            raise ValueError
    except ValueError:
        await message.answer("Пожалуйста, введите корректный возраст (число от 5 до 100):")
        return
    await state.update_data(age=age)
    await message.answer("Введите класс (например, 5А):")
    await state.set_state(StudentForm.grade)

@router.message(StudentForm.grade)
async def process_grade(message: types.Message, state: FSMContext):
    await state.update_data(grade=message.text.strip())
    await message.answer("Введите город проживания студента:")
    await state.set_state(StudentForm.city)

@router.message(StudentForm.city)
async def process_city(message: types.Message, state: FSMContext):
    city = message.text.strip()
    data = await state.get_data()
    student = Student(
        name=data["name"],
        age=data["age"],
        grade=data["grade"],
        city=city
    )
    sessionmaker = get_async_sessionmaker()
    async with sessionmaker() as session:
        try:
            session.add(student)
            await session.commit()
            await message.answer(
                f"✅ Студент {student.name} ({student.age} лет, {student.grade}, {student.city}) успешно добавлен!"
            )
            weather_service = YandexWeatherService()
            weather_data = await weather_service.get_weather(city)
            if weather_data:
                weather_text = format_weather(city, weather_data)
                await message.answer(weather_text)
            else:
                await message.answer("⚠️ Не удалось получить погоду для указанного города.")
        except Exception as e:
            await session.rollback()
            await message.answer(f"❌ Ошибка при добавлении: {e}")
    await state.clear()

# Автоматически создаём таблицы при первом импорте
import asyncio
asyncio.get_event_loop().run_until_complete(create_tables()) 