import asyncio
import os

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("Нет BOT_TOKEN")


bot = Bot(token=TOKEN)
dp = Dispatcher()


# Клавиатура
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👤 Профиль"),
            KeyboardButton(text="⚙️ Настройки")
        ],
        [
            KeyboardButton(text="❓ Помощь")
        ]
    ],
    resize_keyboard=True
)


# Команда /start
@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\n\n"
        "Я тестовый бот.\n"
        "Выбери действие:",
        reply_markup=menu
    )


# Кнопка профиль
@dp.message(lambda msg: msg.text == "👤 Профиль")
async def profile(message: Message):
    await message.answer(
        f"Твой ID: {message.from_user.id}\n"
        f"Имя: {message.from_user.full_name}"
    )


# Кнопка настройки
@dp.message(lambda msg: msg.text == "⚙️ Настройки")
async def settings(message: Message):
    await message.answer(
        "Настройки пока пустые 😎"
    )


# Кнопка помощь
@dp.message(lambda msg: msg.text == "❓ Помощь")
async def help(message: Message):
    await message.answer(
        "Команды:\n"
        "/start - запуск\n\n"
        "Это тестовый бот."
    )


# Любой другой текст
@dp.message()
async def echo(message: Message):
    await message.answer(
        "Я пока не знаю такую команду 😅"
    )


async def main():
    print("Бот запущен!")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
