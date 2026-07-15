import asyncio

from admin import register_admin

from aiogram import Bot, Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from config import (
    BOT_TOKEN,
    BOT_NAME,
    FREE_SUB,
    PRO_SUB,
    PREMIUM_SUB,
    PRO_KEY,
    ADMINS,
    MODERATORS,
    WL_PS
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
    profile_keyboard,
    settings_keyboard,
    admin_keyboard,
    back_keyboard,
)


bot = Bot(
    token=BOT_TOKEN
)

dp = Dispatcher()
WAITING_PRO_KEY = {}
register_admin(dp)

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
        message.from_user.id in ADMINS
        or
        message.from_user.id in MODERATORS
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

🌍 Серверов: 5 (LTE + Базовые сервера)
⚡ Скорость: До 1 Гб\сек


⭐ PRO

🌍 Серверов: 18 (LTE + Базовые сервера + PRO сервера)
⚡ Максимальная скорость
🚀 Приоритетные сервера
⚡ Скорость: До 10 Гб\сек
🍀 Наилучшая стабильность 
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


Ваш тариф: FREE

Характеристики:

🌍 Серверов: 5 (LTE + Базовые сервера)
⚡ Скорость: высокая

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

    WAITING_PRO_KEY[call.from_user.id] = True

    await call.message.edit_text(
        """
⭐ NE FREE VPN PRO

Для активации PRO

Введите ключ активации следующим сообщением.
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

Имя: {user[2]}

Username: @{user[1] if user[1] else "нет"}

Дата регистрации: {user[3]}

Тариф: ⭐ {user[4]}

VPN получено: {user[5]}
""",
            reply_markup=back_keyboard()
        )

#==========================
# PREMIUM
#==========================

@dp.callback_query(lambda c: c.data == "premium")
async def premium(call: CallbackQuery):

    if call.from_user.id not in WL_PS:

        await call.answer(
            "⛔ Premium доступен только участникам WhiteList.",
            show_alert=True
        )

        return

    await set_tariff(
        call.from_user.id,
        "PREMIUM"
    )

    await call.message.edit_text(
        f"""
💎 NE FREE VPN PREMIUM

Ваш тариф:

PREMIUM


Характеристики

🌍 Все серверы

🚀 Максимальный приоритет

⚡ До 10 Гбит/сек

⭐ Premium поддержка

🎁 Эксклюзивные сервера


Подписка

{PREMIUM_SUB}


Наш бот

https://t.me/NE_FREE_VPN_bot
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

👥 Пользователей: {users}

🟢 Статус северов: 
🇸🇴 LTE - Отлично
🇸🇴 LTE 2 - Хорошо
🇸🇴 LTE 3 - Сбой после DDos
🇷🇺 Russia - Отлично
🇷🇺 Russia - Сбой
🇩🇪 Germany - Отлично
🇦🇹 Austria - Отлично
🇨🇭 Switzerland - Отлично
🇧🇾 Belarus - Хорошо
🇳🇱 Netherlands - Отлично
🇩🇪 Germany 2 - Отлично
🇱🇻 Latvia - Отлично
🇨🇭 Switzerland 2 - Отлично
🇺🇸 United States - Отлично
🇺🇸 United States 2 - Хорошо
🇱🇹 Lithuania - Отлично
🇫🇮 Finland - Хорошо
🇳🇱 Netherlands 2 - Отлично
🇳🇱 Netherlands 3 - Сбой после DDos
🇵🇱 Poland - Отлично
🇫🇷 France - Хорошо
🇪🇪 Estonia - Плохо

Все оплачиваеться благодаря рекламе, спасибо за использование!

🚀 NE FREE VPN
""",
        reply_markup=back_keyboard()
    )




#==========================
# ADMIN
#==========================

@dp.message(Command("admin"))
async def admin_command(message: Message):

    if (
        message.from_user.id
        not in ADMINS
        and
        message.from_user.id
        not in MODERATORS
    ):

        await message.answer(
            "❌ У вас нет доступа."
        )

        return

    users = await get_users_count()

    await message.answer(
        f"""
👑 Панель управления

👥 Пользователей:

{users}

Ваш статус:

{"Администратор" if message.from_user.id in ADMINS else "Модератор"}

Выберите действие.
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


🌐 Язык: 🇷🇺 Русский

🔔 Уведомления: ✅ Включены

⚙️ Дополнительные функции: В разработке 🚧
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

Скоро появятся:

• FAQ
• Инструкции
• Поддержка

Если нашли ошибку, пожалуйста напишите @My_name_is_Sasha

Спасибо за использование ❤️
""",
        reply_markup=back_keyboard()
    )



# =========================
# ADMIN
# =========================


@dp.callback_query(lambda c: c.data == "admin")
async def admin(call: CallbackQuery):

    if (
        call.from_user.id not in ADMINS
        and call.from_user.id not in MODERATORS
    ):

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
        reply_markup=admin_keyboard()
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
    call.from_user.id in ADMINS
    or call.from_user.id in MODERATORS
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

@dp.message()
async def pro_key(message: Message):

    if message.from_user.id not in WAITING_PRO_KEY:
        return

    del WAITING_PRO_KEY[message.from_user.id]

    if message.text == PRO_KEY:

        await set_tariff(
            message.from_user.id,
            "PRO"
        )

        await message.answer(
            f"""
⭐ NE FREE VPN PRO

Ваш тариф:

PRO

🌍 Серверов: 8

⚡ Скорость: Максимальная

Подписка:

{PRO_SUB}
"""
        )

    else:

        await message.answer(
            "❌ Неверный ключ активации."
        )

if __name__ == "__main__":

    asyncio.run(main())
