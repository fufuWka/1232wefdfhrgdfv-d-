from aiogram.types import CallbackQuery
from aiogram import Dispatcher

from database import get_users_count
from keyboards import back_keyboard


def register_admin(dp: Dispatcher):

    @dp.callback_query(lambda c: c.data == "admin")
    async def admin_panel(call: CallbackQuery):

        users = await get_users_count()

        text = f"""
👑 Админ-панель


👥 Пользователей:

{users}


🟢 Статус:

Онлайн


Доступные функции:

📊 Статистика

📢 Рассылка

🔑 Управление тарифами

⚙️ Настройки

🚧 Скоро появятся новые возможности.
"""

        await call.message.edit_text(
            text,
            reply_markup=back_keyboard()
        )
