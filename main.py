import asyncio
import os

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN не найден")


bot = Bot(token=TOKEN)
dp = Dispatcher()


# =====================
# КНОПКИ
# =====================

def main_menu():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="⚡ VPN",
        callback_data="vpn"
    )

    kb.button(
        text="📊 Статистика",
        callback_data="stats"
    )

    kb.button(
        text="🛠 Настройки",
        callback_data="settings"
    )

    kb.button(
        text="❓ Помощь",
        callback_data="help"
    )

    kb.adjust(2)

    return kb.as_markup()



def vpn_menu():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="🆓 FREE",
        callback_data="free"
    )

    kb.button(
        text="⭐ PRO",
        callback_data="pro"
    )

    kb.button(
        text="◀ Назад",
        callback_data="back"
    )

    kb.adjust(2)

    return kb.as_markup()



def back_button():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="◀ Назад",
        callback_data="back"
    )

    return kb.as_markup()



# =====================
# START
# =====================


@dp.message(Command("start"))
async def start(message: Message):

    username = message.from_user.username

    if username:
        user = "@" + username
    else:
        user = message.from_user.first_name


    text = f"""
🚀 NE_FREE_VPN_bot

Привет, {user}! 👋


Это NE_FREE_VPN_bot.

Он может бесплатно предоставить вам VPN.

Будем рады, если воспользуетесь нашим сервисом!


Мои возможности:

⚡ VPN
📊 Статистика
🛠 Настройки
❓ Помощь
"""


    await message.answer(
        text,
        reply_markup=main_menu()
    )



# =====================
# VPN
# =====================


@dp.callback_query(lambda c: c.data == "vpn")
async def vpn(callback: CallbackQuery):

    await callback.message.edit_text(
        """
🌐 VPN

Выберите тариф:

🆓 FREE
Бесплатный доступ

⭐ PRO
Расширенный доступ
""",
        reply_markup=vpn_menu()
    )



@dp.callback_query(lambda c: c.data == "free")
async def free(callback: CallbackQuery):

    await callback.message.edit_text(
        """
🆓 FREE VPN


Статус:
🟢 Доступен


Серверы:
🌍 Скоро будут добавлены


Конфиг:
⏳ В разработке
""",
        reply_markup=back_button()
    )



@dp.callback_query(lambda c: c.data == "pro")
async def pro(callback: CallbackQuery):

    await callback.message.edit_text(
        """
⭐ PRO VPN


Преимущества:

⚡ Высокая скорость
🌍 Больше серверов
🚀 Приоритет


Статус:
🔒 Требуется подписка
""",
        reply_markup=back_button()
    )



# =====================
# СТАТИСТИКА
# =====================


@dp.callback_query(lambda c: c.data == "stats")
async def stats(callback: CallbackQuery):

    await callback.message.edit_text(
        f"""
📊 Статистика


👤 Пользователь:
{callback.from_user.full_name}


🆔 ID:
{callback.from_user.id}


🌐 VPN использован:
0 раз


⭐ Тариф:
FREE
""",
        reply_markup=back_button()
    )



# =====================
# НАСТРОЙКИ
# =====================


@dp.callback_query(lambda c: c.data == "settings")
async def settings(callback: CallbackQuery):

    await callback.message.edit_text(
        """
🛠 Настройки


🌐 Язык:
🇷🇺 Русский


🔔 Уведомления:
✅ Включены


🔐 Безопасность:
🟢 Активна
""",
        reply_markup=back_button()
    )



# =====================
# ПОМОЩЬ
# =====================


@dp.callback_query(lambda c: c.data == "help")
async def help_menu(callback: CallbackQuery):

    await callback.message.edit_text(
        """
❓ Помощь


Раздел находится в разработке 🚧


Скоро здесь появится:

• FAQ
• Поддержка
• Инструкции
• Новости


Спасибо за использование
NE_FREE_VPN_bot ❤️
""",
        reply_markup=back_button()
    )



# =====================
# НАЗАД
# =====================


@dp.callback_query(lambda c: c.data == "back")
async def back(callback: CallbackQuery):

    await callback.message.edit_text(
        "🚀 Главное меню\n\nВыберите действие:",
        reply_markup=main_menu()
    )



# =====================
# ЗАПУСК
# =====================


async def main():

    print("NE_FREE_VPN_bot запущен!")

    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())
