from aiogram.utils.keyboard import InlineKeyboardBuilder



def main_keyboard(is_admin=False):

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


    if is_admin:

        kb.button(
            text="👑 Админ-панель",
            callback_data="admin"
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
