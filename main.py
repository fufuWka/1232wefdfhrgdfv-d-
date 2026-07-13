import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from config import (
    BOT_TOKEN,
    ADMIN_ID,
    BOT_NAME,
    FREE_SUB,
    PRO_SUB
)

from database import (
    init_db,
    add_user,
    get_user,
    get_users_count,
    set_tariff
)

from keyboards import (
    main_keyboard,
    vpn_keyboard,
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


    username = (
        "@" + message.from_user.username
        if message.from_user.username
        else message.from_user.first_name
    )


    is_admin = (
        message.from_user.id == ADMIN_ID
    )


    await message.answer(
        f"""
🚀 {BOT_NAME}


Привет, {username}! 👋


Это NE_FREE_VPN_bot.

Он может бесплатно предоставить вам VPN.


Будем рады, если воспользуетесь нашим сервисом ❤️


Мои возможности:

⚡ VPN
👤 Профиль
📊 Статистика
🛠 Настройки
❓ Помощь
""",
        reply_markup=main_keyboard(is_admin)
    )



# =========================
# VPN MENU
# =========================


@dp.callback_query(lambda c: c.data == "vpn")
async def vpn_menu(call: CallbackQuery):

    await call.message.edit_text(
        """
⚡ VPN


Выберите тариф:


🆓 FREE

• 3 сервера
• Бесплатный доступ


⭐ PRO

• 8 серверов
• Максимальные возможности
""",
        reply_markup=vpn_keyboard()
    )



# =========================
# FREE
# =========================


@dp.callback_query(lambda c: c.data == "free")
async def free(call: CallbackQuery):

    await set_tariff(
        call.from_user.id,
        "FREE"
    )


    await call.message.edit_text(
        f"""
🆓 NE FREE VPN


Ваш тариф:

FREE


Характеристики:

🌍 Серверов: 3

⚡ Скорость: высокая

🔄 Обновление:
автоматически


Подписка:

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

    await set_tariff(
        call.from_user.id,
        "PRO"
    )


    await call.message.edit_text(
        f"""
⭐ NE FREE VPN PRO


Ваш тариф:

PRO


Характеристики:

🌍 Серверов: 8

⚡ Максимальная скорость

🚀 Приоритетные сервера

🔄 Обновление:
автоматически


Подписка:

{PRO_SUB}


Наш бот:
https://t.me/NE_FREE_VPN_bot
""",
        reply_markup=back_keyboard()
    )



# =========================
# PROFILE
# =========================


@dp.callback_query(lambda c: c.data == "profile")
async def profile(call: CallbackQuery):

    user = await get_user(
        call.from_user.id
    )


    if user:

        await call.message.edit_text(
            f"""
👤 Профиль


Имя:

{user[2]}


Username:

@{user[1] if user[1] else "нет"}


Дата регистрации:

{user[3]}


Тариф:

⭐ {user[4]}


VPN получено:

{user[5]}
""",
            reply_markup=back_keyboard()
        )



# =========================
# STATS
# =========================


@dp.callback_query(lambda c: c.data == "stats")
async def stats(call: CallbackQuery):

    users = await get_users_count()


    await call.message.edit_text(
        f"""
📊 Статистика


👥 Пользователей:

{users}


🟢 Статус:

Онлайн


🚀 NE FREE VPN
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


⚙️ Дополнительные функции:

В разработке 🚧
""",
        reply_markup=back_keyboard()
    )



# =========================
# HELP
# =========================


@dp.callback_query(lambda c: c.data == "help")
async def help_menu(call: CallbackQuery):

    await call.message.edit_text(
        """
❓ Помощь


Раздел находится
в разработке 🚧


Скоро появятся:

• FAQ
• Инструкции
• Поддержка


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

👥 Пользователи

📢 Рассылка

📊 Статистика
""",
        reply_markup=back_keyboard()
    )



# =========================
# BACK
# =========================


@dp.callback_query(lambda c: c.data == "back")
async def back(call: CallbackQuery):

    await call.message.edit_text(
        """
🚀 NE FREE VPN


Выберите действие:
""",
        reply_markup=main_keyboard(
            call.from_user.id == ADMIN_ID
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
