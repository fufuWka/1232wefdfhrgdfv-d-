from aiogram.utils.keyboard import InlineKeyboardBuilder


# ==========================
# Главное меню
# ==========================

def main_keyboard(is_admin=False):

    kb = InlineKeyboardBuilder()

    kb.button(
        text="⚡ VPN",
        callback_data="vpn"
    )

    kb.button(
        text="👤 Профиль",
        callback_data="profile"
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

    if is_admin:
        kb.button(
            text="👑 Админ-панель",
            callback_data="admin"
        )

    kb.adjust(2, 2, 2)

    return kb.as_markup()


# ==========================
# VPN
# ==========================

from aiogram.utils.keyboard import InlineKeyboardBuilder


# ==========================
# Главное меню
# ==========================

def main_keyboard(is_admin=False):

    kb = InlineKeyboardBuilder()

    kb.button(
        text="⚡ VPN",
        callback_data="vpn"
    )

    kb.button(
        text="👤 Профиль",
        callback_data="profile"
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

    if is_admin:
        kb.button(
            text="👑 Админ-панель",
            callback_data="admin"
        )

    kb.adjust(2, 2, 2)

    return kb.as_markup()


# ==========================
# VPN
# ==========================

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

    kb.adjust(2, 1)

    return kb.as_markup()


# ==========================
# Кнопка подписки
# ==========================

def profile_keyboard(subscription_url: str):

    kb = InlineKeyboardBuilder()

    kb.button(
        text="📥 Получить подписку",
        url=subscription_url
    )

    kb.button(
        text="🌍 Серверы",
        callback_data="servers"
    )

    kb.button(
        text="◀ Назад",
        callback_data="vpn"
    )

    kb.adjust(1, 1, 1)

    return kb.as_markup()


# ==========================
# Универсальная кнопка назад
# ==========================

def back_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="◀ Назад",
        callback_data="back"
    )

    return kb.as_markup()


# ==========================
# Настройки
# ==========================

def settings_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="🌐 Язык",
        callback_data="language"
    )

    kb.button(
        text="🔔 Уведомления",
        callback_data="notify"
    )

    kb.button(
        text="🎨 Тема",
        callback_data="theme"
    )

    kb.button(
        text="◀ Назад",
        callback_data="back"
    )

    kb.adjust(2, 1, 1)

    return kb.as_markup()


# ==========================
# Админ-панель
# ==========================

def admin_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="👥 Пользователи",
        callback_data="admin_users"
    )

    kb.button(
        text="📊 Статистика",
        callback_data="admin_stats"
    )

    kb.button(
        text="📢 Рассылка",
        callback_data="broadcast"
    )

    kb.button(
        text="⭐ Выдать PRO",
        callback_data="give_pro"
    )

    kb.button(
        text="🔄 Перезапуск",
        callback_data="restart"
    )

    kb.button(
        text="◀ Назад",
        callback_data="back"
    )

    kb.adjust(2, 2, 1, 1)

    return kb.as_markup()


# ==========================
# Кнопка подписки
# ==========================

def profile_keyboard(subscription_url: str):

    kb = InlineKeyboardBuilder()

    kb.button(
        text="📥 Получить подписку",
        url=subscription_url
    )

    kb.button(
        text="🌍 Серверы",
        callback_data="servers"
    )

    kb.button(
        text="◀ Назад",
        callback_data="back"
    )

    kb.adjust(1, 1, 1)

    return kb.as_markup()


# ==========================
# Универсальная кнопка назад
# ==========================

def back_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="◀ Назад",
        callback_data="back"
    )

    return kb.as_markup()


# ==========================
# Настройки
# ==========================

def settings_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="🌐 Язык",
        callback_data="language"
    )

    kb.button(
        text="🔔 Уведомления",
        callback_data="notify"
    )

    kb.button(
        text="🎨 Тема",
        callback_data="theme"
    )

    kb.button(
        text="◀ Назад",
        callback_data="back"
    )

    kb.adjust(2, 1, 1)

    return kb.as_markup()


# ==========================
# Админ-панель
# ==========================

def admin_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="👥 Пользователи",
        callback_data="admin_users"
    )

    kb.button(
        text="📊 Статистика",
        callback_data="admin_stats"
    )

    kb.button(
        text="📢 Рассылка",
        callback_data="broadcast"
    )

    kb.button(
        text="⭐ Выдать PRO",
        callback_data="give_pro"
    )

    kb.button(
        text="🔄 Перезапуск",
        callback_data="restart"
    )

    kb.button(
        text="◀ Назад",
        callback_data="back"
    )

    kb.adjust(2, 2, 1, 1)

    return kb.as_markup()
