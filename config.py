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
    "https://gist.githubusercontent.com/"
    "fufuWka/58e04a989aea6e1adaf6fe809525148f/"
    "raw/8270fb79876b0cf92e418a60df443729e01aadaf/"
    "FREE_VPN.bot"
)

PRO_SUB = (
    "https://gist.githubusercontent.com/"
    "fufuWka/58e04a989aea6e1adaf6fe809525148f/"
    "raw/8270fb79876b0cf92e418a60df443729e01aadaf/"
    "PRO_VPN.bot"
)

# ==========================
# Тарифы
# ==========================

FREE_NAME = "FREE"
FREE_SERVERS = 3

PRO_NAME = "PRO"
PRO_SERVERS = 8

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
