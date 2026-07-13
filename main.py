import asyncio
import os

from database import init_db, add_user

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.types import (
    Message,
    CallbackQuery
)
from aiogram.filters import Command

from aiogram.utils.keyboard import InlineKeyboardBuilder


load_dotenv()


TOKEN = os.getenv("BOT_TOKEN")


if not TOKEN:
    raise Exception("BOT_TOKEN не найден")


bot = Bot(TOKEN)

dp = Dispatcher()


# ==========================
# Ссылки подписок
# ==========================

FREE_SUB = (
    "https://gist.githubusercontent.com/"
    "fufuWka/58e04a989aea6e1adaf6fe809525148f/"
    "raw/59f8d78fe298ba2743279f350a4b75b82e4ae8b1/"
    "FREE_VPN.bot"
)


PRO_SUB = (
    "https://gist.githubusercontent.com/"
    "fufuWka/58e04a989aea6e1adaf6fe809525148f/"
    "raw/ff9ef77549fbf3a3c60482bb19817bba14ca1e0d/"
    "PRO_VPN.bot"
)


# ==========================
# Клавиатуры
# ==========================


def main_keyboard():

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



def vpn_keyboard():

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



def back_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="◀ Назад",
        callback_data="back"
    )

    return kb.as_markup()



def subscribe_keyboard(link):

    kb = InlineKeyboardBuilder()

    kb.button(
        text="🔗 Открыть подписку",
        url=link
    )

    kb.button(
        text="◀ Назад",
        callback_data="vpn"
    )

    kb.adjust(1)

    return kb.as_markup()



# ==========================
# START
# ==========================


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
        reply_markup=main_keyboard()
    )



# ==========================
# VPN MENU
# ==========================


@dp.callback_query(lambda c: c.data == "vpn")
async def vpn_menu(call: CallbackQuery):

    await call.message.edit_text(
        """
⚡ VPN


Выберите тариф:


🆓 FREE

• 3 сервера
• Бесплатный доступ
• Автообновление


⭐ PRO

• 8 серверов
• Больше возможностей
• Приоритетные сервера
""",
        reply_markup=vpn_keyboard()
    )



# ==========================
# FREE
# ==========================


@dp.callback_query(lambda c: c.data == "free")
async def free(call: CallbackQuery):

    await call.message.edit_text(
        f"""
🆓 NE FREE VPN


Ваш тариф:

FREE


Характеристики:

🌍 Серверов: 3
⚡ Скорость: высокая
🔄 Обновление: автоматически


Ваша подписка:

Нажмите кнопку ниже 👇


Если что-то не работает —
обновите подписку.


Наш бот:
https://t.me/NE_FREE_VPN_bot
""",
        reply_markup=subscribe_keyboard(FREE_SUB)
    )



# ==========================
# PRO
# ==========================


@dp.callback_query(lambda c: c.data == "pro")
async def pro(call: CallbackQuery):

    await call.message.edit_text(
        f"""
⭐ NE FREE VPN PRO


Ваш тариф:

PRO


Характеристики:

🌍 Серверов: 8
⚡ Максимальная скорость
🚀 Приоритетное подключение
🔄 Автообновление


Ваша подписка:

Нажмите кнопку ниже 👇


Если появились проблемы —
обратитесь в поддержку.


Наш бот:
https://t.me/NE_FREE_VPN_bot
""",
        reply_markup=subscribe_keyboard(PRO_SUB)
    )



# ==========================
# STATS
# ==========================


@dp.callback_query(lambda c: c.data == "stats")
async def stats(call: CallbackQuery):

    await call.message.edit_text(
        f"""
📊 Статистика


👤 Пользователь:

{call.from_user.full_name}


🆔 ID:

{call.from_user.id}


⭐ Тариф:

FREE


🌐 VPN подключений:

0


🚀 NE FREE VPN
""",
        reply_markup=back_keyboard()
    )



# ==========================
# SETTINGS
# ==========================


@dp.callback_query(lambda c: c.data == "settings")
async def settings(call: CallbackQuery):

    await call.message.edit_text(
        """
🛠 Настройки


🌐 Язык:

🇷🇺 Русский


🔔 Уведомления:

✅ Включены


🔐 Безопасность:

🟢 Активна


Раздел настроек находится
в разработке 🚧
""",
        reply_markup=back_keyboard()
    )



# ==========================
# HELP
# ==========================


@dp.callback_query(lambda c: c.data == "help")
async def help(call: CallbackQuery):

    await call.message.edit_text(
        """
❓ Помощь


Раздел находится
в разработке 🚧


Скоро здесь появятся:


• Инструкции
• FAQ
• Поддержка
• Новости


Спасибо за использование ❤️
NE FREE VPN
""",
        reply_markup=back_keyboard()
    )



# ==========================
# BACK
# ==========================


@dp.callback_query(lambda c: c.data == "back")
async def back(call: CallbackQuery):

    await call.message.edit_text(
        """
🚀 NE FREE VPN


Выберите действие:
""",
        reply_markup=main_keyboard()
    )



# ==========================
# RUN
# ==========================


async def main():

    await init_db()

    print("NE_FREE_VPN_bot запущен!")

    await dp.start_polling(bot)



if __name__ == "__main__":

    asyncio.run(main())
