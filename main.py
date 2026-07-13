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
    back_keyboard,
    profile_keyboard
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


    text = f"""
🚀 {BOT_NAME}


Привет, {username}! 👋


Это NE_FREE_VPN_bot.

Он может бесплатно предоставить вам VPN.


Мы рады, что вы пользуетесь нашим сервисом ❤️


Возможности:

⚡ VPN
👤 Профиль
📊 Статистика
🛠 Настройки
❓ Помощь
"""


    await message.answer(
        text,
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
• Автообновление


⭐ PRO

• 8 серверов
• Максимальная скорость
• Приоритет
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


Нажмите кнопку ниже,
чтобы открыть подписку:


Наш бот:
https://t.me/NE_FREE_VPN_bot
""",
        reply_markup=profile_keyboard(FREE_SUB)
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

🔄 Автообновление


Приятного пользования ❤️


Наш бот:
https://t.me/NE_FREE_VPN_bot
""",
        reply_markup=profile_keyboard(PRO_SUB)
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
# STATISTICS
# =========================


@dp.callback_query(lambda c: c.data == "stats")
async def stats(call: CallbackQuery):

    users = await get_users_count()


    await call.message.edit_text(
        f"""
📊 Статистика


👥 Пользователей:

{users}


🟢 Сервис:

Работает


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

Скоро появятся 🚧
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

👥 Пользователи

📢 Рассылка

📊 Статистика

⚙️ Настройки
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
        reply_markup=main_keyboard(is_admin)
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
