import os
from dotenv import load_dotenv

load_dotenv()

# ==========================
# Telegram
# ==========================

BOT_TOKEN = os.getenv("BOT_TOKEN")

ADMIN_ID = int(
    os.getenv(
        "ADMIN_ID",
        "0"
    )
)

BOT_NAME = "NE_FREE_VPN_bot"

BOT_LINK = "https://t.me/NE_FREE_VPN_bot"

# ==========================
# GitHub Gist
# ==========================

FREE_SUB = (
    "https://raw.githubusercontent.com/"
    "fufuWka/1232wefdfhrgdfv-d-/"
    "refs/heads/main/"
    "free.bot"
)

PRO_SUB = (
    "https://raw.githubusercontent.com/"
    "fufuWka/1232wefdfhrgdfv-d-/"
    "refs/heads/main/"
    "pro.bot"
)

# ==========================
# Тарифы
# ==========================

FREE_NAME = "FREE"
FREE_SERVERS = 3

PRO_NAME = "PRO"
PRO_SERVERS = 18

# ==========================
# Поддержка
# ==========================

SUPPORT_TEXT = (
    "Если возникли проблемы с VPN,\n"
    "обновите подписку.\n\n"
    "Если проблема сохраняется,\n"
    "обратитесь в поддержку."
)

# ==========================
# Версия
# ==========================

BOT_VERSION = "v3.0"
