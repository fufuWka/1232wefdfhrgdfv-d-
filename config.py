import os
from dotenv import load_dotenv


load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")


ADMIN_ID = int(
    os.getenv(
        "ADMIN_ID",
        0
    )
)


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


BOT_NAME = "NE_FREE_VPN_bot"
