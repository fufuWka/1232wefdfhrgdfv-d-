import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import (
    Message,
    CallbackQuery
)
from aiogram.filters import Command

from config import (
    BOT_TOKEN,
    ADMIN_ID,
    FREE_SUB,
    PRO_SUB,
    BOT_NAME
)

from database import (
    init_db,
    add_user,
    get_user
)

from keyboards import (
    main_keyboard,
    back_keyboard
)


bot = Bot(
    token=BOT_TOKEN
)

dp = Dispatcher()



# =========================
# START
# =========================


@dp.message(Command("start"))
async def start(message: Message):

    await add_user(
        message.from_user.id,
        message.from_user.username,
        message.from_user.first_name
    )


    username = message.from_user.username

    if username:
        user = "@" + username
    else:
        user = message.from_user.first_name


    is_admin = (
        message.from_user.id == ADMIN_ID
    )


    text = f"""
🚀 {BOT_NAME}


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
        reply_markup=main_keyboard(
            is_admin
        )
    )



# =========================
# VPN
# =========================


@dp.callback_query(lambda c: c.data == "vpn")
async def vpn(call: CallbackQuery):

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
• Приоритет
""",
        reply_markup=back_keyboard()
    )



# =========================
# FREE
# =========================


@dp.callback_query(lambda c: c.data == "free")
async def free(call: CallbackQuery):

    await call.message.edit_text(
        f"""
🆓 NE FREE VPN


Тариф:

FREE


Характеристики:

🌍 Серверов: 3
⚡ Скорость: высокая
🔄 Обновление: автоматически


Ваша подписка:

{FREE_SUB}


Наш бот:
https://t.me/NE_FREE_VPN_bot
""",
        reply_markup=back_keyboard()
    )



# =========================
# PRO
# =========================


@dp.callback_query(lambda c: c.data == "pro")
async def pro(call: CallbackQuery):

    await call.message.edit_text(
        f"""
⭐ NE FREE VPN PRO


Тариф:

PRO


Характеристики:

🌍 Серверов: 8
⚡ Максимальная скорость
🚀 Приоритетные сервера
🔄 Автообновление


Ваша подписка:

{PRO_SUB}


Наш бот:
https://t.me/NE_FREE_VPN_bot
""",
        reply_markup=back_keyboard()
    )



# =========================
# STATISTICS
# =========================


@dp.callback_query(lambda c: c.data == "stats")
async def stats(call: CallbackQuery):

    user = await get_user(
        call.from_user.id
    )


    tariff = "FREE"


    if user:
        tariff = user[4]


    await call.message.edit_text(
        f"""
📊 Статистика


👤 Пользователь:

{call.from_user.full_name}


🆔 ID:

{call.from_user.id}


⭐ Тариф:

{tariff}


🌐 VPN использовано:

0 раз


🚀 {BOT_NAME}
""",
        reply_markup=back_keyboard()
    )



# =========================
# SETTINGS
# =========================


@dp.callback_query(lambda c: c.data == "settings")
async def settings(call: CallbackQuery):

    await call.message.edit_text(
        """
🛠 Настройки


🌐 Язык:

🇷🇺 Русский


🔔 Уведомления:

✅ Включены


⚙️ Дополнительные настройки:

В разработке 🚧
""",
        reply_markup=back_keyboard()
    )



# =========================
# HELP
# =========================


@dp.callback_query(lambda c: c.data == "help")
async def help(call: CallbackQuery):

    await call.message.edit_text(
        """
❓ Помощь


Раздел находится
в разработке 🚧


Скоро появятся:

• FAQ
• Поддержка
• Инструкции
• Новости


Спасибо за использование ❤️
""",
        reply_markup=back_keyboard()
    )



# =========================
# ADMIN
# =========================


@dp.callback_query(lambda c: c.data == "admin")
async def admin(call: CallbackQuery):

    if call.from_user.id != ADMIN_ID:
        await call.answer(
            "Нет доступа ❌",
            show_alert=True
        )
        return


    await call.message.edit_text(
        """
👑 Админ-панель


🟢 Бот работает


Функции:

📊 Статистика

📢 Рассылка

👥 Пользователи

⚙️ Настройки


Скоро будет больше 🚀
""",
        reply_markup=back_keyboard()
    )



# =========================
# BACK
# =========================


@dp.callback_query(lambda c: c.data == "back")
async def back(call: CallbackQuery):

    is_admin = (
        call.from_user.id == ADMIN_ID
    )


    await call.message.edit_text(
        """
🚀 NE FREE VPN


Выберите действие:
""",
        reply_markup=main_keyboard(
            is_admin
        )
    )



# =========================
# RUN
# =========================


async def main():

    await init_db()

    print(
        "NE_FREE_VPN_bot запущен!"
    )


    await dp.start_polling(bot)



if __name__ == "__main__":

    asyncio.run(main())
